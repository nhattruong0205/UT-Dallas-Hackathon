import csv
import html
import io
import math

import streamlit as st

from page_one_builder.sample_data import SAMPLE_BUYER_HOTSPOTS


def parse_hotspot_csv(uploaded_file) -> list[dict]:
    try:
        contents = uploaded_file.getvalue().decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise ValueError("Upload a UTF-8 encoded CSV file.") from error

    reader = csv.DictReader(io.StringIO(contents))
    required_columns = {"latitude", "longitude", "weight"}
    if reader.fieldnames is None or not required_columns.issubset(reader.fieldnames):
        raise ValueError(
            "The CSV needs latitude, longitude, and weight columns. "
            "An area column is optional."
        )

    hotspots = []
    for row_number, row in enumerate(reader, start=2):
        try:
            latitude = float(row["latitude"])
            longitude = float(row["longitude"])
            weight = float(row["weight"])
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"Row {row_number} must contain numeric latitude, longitude, and weight values."
            ) from error
        if (
            not math.isfinite(latitude)
            or not math.isfinite(longitude)
            or not math.isfinite(weight)
        ):
            raise ValueError(f"Row {row_number} must contain finite numeric values.")
        if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
            raise ValueError(f"Row {row_number} has coordinates outside valid ranges.")
        if weight <= 0:
            raise ValueError(f"Row {row_number} weight must be greater than zero.")
        hotspots.append(
            {
                "area": (row.get("area") or "").strip() or f"Hotspot {row_number - 1}",
                "latitude": latitude,
                "longitude": longitude,
                "weight": weight,
            }
        )

    if not hotspots:
        raise ValueError("The uploaded CSV has headers but no hotspot rows.")
    return hotspots


def distance_in_miles(
    latitude_a: float,
    longitude_a: float,
    latitude_b: float,
    longitude_b: float,
) -> float:
    earth_radius_miles = 3958.8
    lat_a = math.radians(latitude_a)
    lat_b = math.radians(latitude_b)
    delta_lat = math.radians(latitude_b - latitude_a)
    delta_lon = math.radians(longitude_b - longitude_a)
    haversine = (
        math.sin(delta_lat / 2) ** 2
        + math.cos(lat_a) * math.cos(lat_b) * math.sin(delta_lon / 2) ** 2
    )
    return 2 * earth_radius_miles * math.asin(math.sqrt(haversine))


def build_local_heatmap(
    hotspots: list[dict],
    restaurant_name: str,
    restaurant_latitude: float,
    restaurant_longitude: float,
    radius_miles: int,
    view: str,
) -> str:
    width = 960
    height = 560
    padding = 70
    center_x = width / 2
    center_y = height / 2
    scale = min(
        (width - 2 * padding) / (radius_miles * 2),
        (height - 2 * padding) / (radius_miles * 2),
    )
    center_latitude_radians = math.radians(restaurant_latitude)
    visible_hotspots = []
    for hotspot in hotspots:
        x_miles = (
            (hotspot["longitude"] - restaurant_longitude)
            * 69.0
            * math.cos(center_latitude_radians)
        )
        y_miles = (hotspot["latitude"] - restaurant_latitude) * 69.0
        distance = math.hypot(x_miles, y_miles)
        if distance <= radius_miles:
            visible_hotspots.append((hotspot, x_miles, y_miles, distance))

    html_parts = [
        '<div role="img" aria-label="Local hotspot heatmap around the restaurant" '
        f'style="position:relative;width:100%;height:{height}px;overflow:hidden;'
        'border-radius:16px;background-color:#f3f6fa;'
        f'background-image:linear-gradient(to right,#dbe3ec 1px,transparent 1px),'
        f'linear-gradient(to bottom,#dbe3ec 1px,transparent 1px);'
        f'background-size:{2*scale:.1f}px {2*scale:.1f}px;'
        f'background-position:center center;">',
        '<div style="position:absolute;left:50%;top:16px;transform:translateX(-50%);'
        'color:#526176;font:14px sans-serif;white-space:nowrap;">'
        "Approximate local-area grid - not a street map</div>",
    ]

    for ring_miles in (1, 3, 5, 10):
        if ring_miles <= radius_miles:
            ring_size = ring_miles * scale * 2
            html_parts.append(
                f'<div aria-hidden="true" style="position:absolute;left:50%;top:50%;'
                f'width:{ring_size:.1f}px;height:{ring_size:.1f}px;'
                'transform:translate(-50%,-50%);border:1px dashed #718096;'
                'border-radius:50%;"></div>'
            )

    show_hotspots = view in {"Restaurant + hotspots", "Buyer hotspots"}
    show_restaurant = view in {"Restaurant + hotspots", "Restaurant location"}
    if show_hotspots and visible_hotspots:
        max_weight = max(item[0]["weight"] for item in visible_hotspots)
        min_weight = min(item[0]["weight"] for item in visible_hotspots)
        for hotspot, x_miles, y_miles, distance in visible_hotspots:
            ratio = (
                (hotspot["weight"] - min_weight) / (max_weight - min_weight)
                if max_weight > min_weight
                else 0.5
            )
            if ratio < 0.5:
                blend = ratio * 2
                red = int(40 + 215 * blend)
                green = int(110 + 90 * blend)
                blue = int(220 - 170 * blend)
            else:
                blend = (ratio - 0.5) * 2
                red = int(255 - 35 * blend)
                green = int(200 - 160 * blend)
                blue = int(50 - 10 * blend)
            color = f"rgb({red},{green},{blue})"
            x = center_x + x_miles * scale
            y = center_y - y_miles * scale
            radius = (0.35 + 0.35 * ratio) * scale
            left = x / width * 100
            top = y / height * 100
            title = html.escape(
                f'{hotspot["area"]} - activity weight {hotspot["weight"]:g} - {distance:.1f} mi away',
                quote=True,
            )
            html_parts.extend(
                [
                    f'<div title="{title}" style="position:absolute;left:{left:.2f}%;'
                    f'top:{top:.2f}%;width:{radius*2:.1f}px;height:{radius*2:.1f}px;'
                    f'transform:translate(-50%,-50%);border-radius:50%;'
                    f'background:radial-gradient(circle,{color} 0%,'
                    f'{color} 24%,transparent 72%);"></div>',
                    f'<div title="{title}" style="position:absolute;left:{left:.2f}%;'
                    f'top:{top:.2f}%;width:10px;height:10px;transform:translate(-50%,-50%);'
                    f'border:2px solid white;border-radius:50%;background:{color};"></div>',
                ]
            )

    if show_restaurant:
        restaurant_label = html.escape(restaurant_name, quote=True)
        html_parts.extend(
            [
                '<div title="Restaurant location" style="position:absolute;left:50%;top:50%;'
                'width:18px;height:18px;transform:translate(-50%,-50%);'
                'border:4px solid white;border-radius:50%;background:#1478e8;'
                'box-shadow:0 1px 5px #475569;"></div>',
                '<div style="position:absolute;left:calc(50% + 15px);top:calc(50% - 9px);'
                'color:#124b85;font:bold 14px sans-serif;white-space:nowrap;'
                'padding:3px 6px;border-radius:5px;background:rgba(255,255,255,.9);'
                f'">{restaurant_label}</div>',
            ]
        )

    html_parts.extend(
        [
            '<div style="position:absolute;left:50%;bottom:12px;transform:translateX(-50%);'
            'color:#526176;font:12px sans-serif;">West &lt;- distance from restaurant -&gt; East</div>',
            '<div style="position:absolute;left:10px;top:50%;transform:translateY(-50%);'
            'color:#526176;font:12px sans-serif;writing-mode:vertical-rl;'
            'rotate:180deg;">South to North</div>',
            "</div>",
        ]
    )
    return "".join(html_parts)


profile = st.session_state.get("restaurant_profile", {})
restaurant_latitude = float(profile.get("latitude", 32.9860))
restaurant_longitude = float(profile.get("longitude", -96.7500))

st.subheader("Map board")
st.write(
    "See where nearby customer interest is concentrated. Being closer can help local relevance, but it does not guarantee a recommendation."
)

uploaded_file = st.file_uploader(
    "Upload aggregated buyer or search-interest hotspots",
    type=["csv"],
    help="Required columns: latitude, longitude, weight. Optional: area. Use aggregated locations, not individual customer addresses.",
)
sample_csv = (
    "latitude,longitude,weight,area\n"
    "32.9865,-96.7505,10,UT Dallas campus\n"
    "32.9850,-96.7130,8,CityLine\n"
)
st.download_button(
    "Download CSV template",
    data=sample_csv,
    file_name="foodreach-hotspots-template.csv",
    mime="text/csv",
)

hotspots = [dict(row) for row in SAMPLE_BUYER_HOTSPOTS]
data_is_valid = True
if uploaded_file is not None:
    try:
        hotspots = parse_hotspot_csv(uploaded_file)
    except ValueError as error:
        st.error(str(error))
        data_is_valid = False
    else:
        st.success("Using your uploaded aggregated hotspot data.")

if data_is_valid:
    view = st.segmented_control(
        "Map view",
        options=[
            "Restaurant + hotspots",
            "Restaurant location",
            "Buyer hotspots",
        ],
        default="Restaurant + hotspots",
        required=True,
        key="map_view",
    )
    radius_miles = st.segmented_control(
        "Nearby area",
        options=[1, 3, 5, 10],
        default=5,
        format_func=lambda miles: f"{miles} mi",
        required=True,
    )
    visible_hotspots = [
        hotspot
        for hotspot in hotspots
        if distance_in_miles(
            restaurant_latitude,
            restaurant_longitude,
            hotspot["latitude"],
            hotspot["longitude"],
        )
        <= radius_miles
    ]
    map_svg = build_local_heatmap(
        visible_hotspots,
        profile.get("name", "Restaurant"),
        restaurant_latitude,
        restaurant_longitude,
        radius_miles,
        view,
    )
    st.html(map_svg, width="stretch")
    st.caption(
        "Blue marker: restaurant. Blue/green is lower activity; yellow/red is higher."
    )

    if visible_hotspots:
        strongest_hotspot = max(visible_hotspots, key=lambda hotspot: hotspot["weight"])
        strongest_distance = distance_in_miles(
            restaurant_latitude,
            restaurant_longitude,
            strongest_hotspot["latitude"],
            strongest_hotspot["longitude"],
        )
        metric_columns = st.columns(3)
        metric_columns[0].metric("Nearby hotspot areas", len(visible_hotspots))
        metric_columns[1].metric("Highest activity area", strongest_hotspot["area"])
        metric_columns[2].metric(
            "Distance from restaurant", f"{strongest_distance:.1f} mi"
        )
        st.subheader("Nearby areas")
        for hotspot in sorted(
            visible_hotspots,
            key=lambda row: row["weight"],
            reverse=True,
        )[:5]:
            hotspot_distance = distance_in_miles(
                restaurant_latitude,
                restaurant_longitude,
                hotspot["latitude"],
                hotspot["longitude"],
            )
            st.markdown(
                f"- **{hotspot['area']}** - weight {hotspot['weight']:g}, "
                f"{hotspot_distance:.1f} mi from the restaurant"
            )

        far_threshold = max(2.0, radius_miles / 2)
        far_areas = []
        for hotspot in visible_hotspots:
            far_distance = distance_in_miles(
                restaurant_latitude,
                restaurant_longitude,
                hotspot["latitude"],
                hotspot["longitude"],
            )
            if far_distance >= far_threshold:
                far_areas.append((hotspot, far_distance))

        st.subheader("Growing visibility in farther areas")
        if far_areas:
            st.write(
                f"These areas are {far_threshold:g}+ miles out. People there are less likely to "
                "find or choose you by default, so give them a specific reason to."
            )
            for hotspot, far_distance in sorted(
                far_areas, key=lambda item: item[0]["weight"], reverse=True
            )[:5]:
                if far_distance >= 7:
                    tip = (
                        "Treat as a destination trip: promote a signature dish or weekend special, "
                        "and run a catering or group-order offer."
                    )
                elif far_distance >= 4:
                    tip = (
                        "Turn on delivery or pickup-ahead for this area, and add a "
                        "'free delivery over $X' or first-order offer."
                    )
                else:
                    tip = (
                        "Add this area name to your Google Business Profile posts and menu "
                        "descriptions, and ask local customers there for reviews."
                    )
                st.markdown(
                    f"- **{hotspot['area']}** ({far_distance:.1f} mi, weight {hotspot['weight']:g}): {tip}"
                )
            st.markdown(
                "**Across all farther areas**\n"
                "- Set your Google Business Profile service area and delivery radius to include them.\n"
                "- Post area-specific updates (events, specials) and use the area name in photo captions and alt text.\n"
                "- List on delivery apps with a delivery radius that reaches these areas.\n"
                "- Partner with nearby offices, schools, apartment complexes, or community groups for catering and group orders.\n"
                "- Collect reviews that mention the neighborhood or what people traveled for.\n"
                "- Run a small, area-targeted local ad or social campaign and track which areas respond."
            )
        else:
            st.info(
                "No hotspots are far enough out in this view. Widen the nearby area to see suggestions for farther neighborhoods."
            )
    else:
        st.info("No hotspot rows fall within this distance. Try a wider area.")
