import streamlit as st

from page_one_builder.sample_data import (
    SAMPLE_GAP_ANALYSIS,
    SAMPLE_KEYWORDS,
    SAMPLE_RESTAURANT,
    get_default_action_plan,
    get_default_content_assets,
)


def clear_widget_values(*prefixes: str) -> None:
    for key in list(st.session_state.keys()):
        if any(str(key).startswith(prefix) for prefix in prefixes):
            del st.session_state[key]


def seed_session_state() -> None:
    st.session_state.setdefault("restaurant_profile", SAMPLE_RESTAURANT.copy())
    st.session_state.restaurant_profile.setdefault(
        "latitude", SAMPLE_RESTAURANT.get("latitude", 32.9860)
    )
    st.session_state.restaurant_profile.setdefault(
        "longitude", SAMPLE_RESTAURANT.get("longitude", -96.7500)
    )
    st.session_state.setdefault(
        "keyword_rows", [row.copy() for row in SAMPLE_KEYWORDS]
    )
    existing_keywords = st.session_state.keyword_rows
    legacy_keywords = {
        "chettinad chicken Richardson",
        "South Indian lunch Plano",
        "halal biryani near UTD",
    }
    if {row.get("keyword") for row in existing_keywords} == legacy_keywords:
        previous_rows = {row["keyword"]: row for row in existing_keywords}
        st.session_state.keyword_rows = [
            {
                **row.copy(),
                **{
                    key: previous_rows[row["keyword"]][key]
                    for key in ("maps_rank", "google_page_one", "ai_mentioned", "notes")
                    if row["keyword"] in previous_rows
                    and key in previous_rows[row["keyword"]]
                },
            }
            for row in SAMPLE_KEYWORDS
        ]
    sample_keyword_names = {row["keyword"] for row in SAMPLE_KEYWORDS}
    placeholder_notes = {
        "",
        "Check how this dish is described in the Google Business Profile.",
        "Look for lunch hours, lunch menu, and nearby area signals.",
        "Check if halal wording appears in menu items and review text.",
    }
    if (
        {row.get("keyword") for row in st.session_state.keyword_rows}
        == sample_keyword_names
        and all(
            row.get("maps_rank", "Not checked") == "Not checked"
            and row.get("google_page_one", "Not checked") == "Not checked"
            and row.get("ai_mentioned", "Not checked") == "Not checked"
            and row.get("notes", "") in placeholder_notes
            for row in st.session_state.keyword_rows
        )
    ):
        clear_widget_values(
            "maps_rank_",
            "google_page_one_",
            "ai_mentioned_",
            "visibility_notes_",
        )
        sample_rows_by_keyword = {
            row["keyword"]: row for row in SAMPLE_KEYWORDS
        }
        for row in st.session_state.keyword_rows:
            sample_row = sample_rows_by_keyword[row["keyword"]]
            row.update(
                {
                    key: sample_row[key]
                    for key in (
                        "maps_rank",
                        "google_page_one",
                        "ai_mentioned",
                        "notes",
                    )
                }
            )
    st.session_state.setdefault(
        "visibility_checks",
        {
            row["keyword"]: {
                "maps_rank": row.get("maps_rank", "Not checked"),
                "google_page_one": row.get("google_page_one", "Not checked"),
                "ai_mentioned": row.get("ai_mentioned", "Not checked"),
                "notes": row.get("notes", ""),
            }
            for row in st.session_state.keyword_rows
        },
    )
    for row in st.session_state.keyword_rows:
        keyword = row["keyword"]
        st.session_state["visibility_checks"].setdefault(
            keyword,
            {
                "maps_rank": row.get("maps_rank", "Not checked"),
                "google_page_one": row.get("google_page_one", "Not checked"),
                "ai_mentioned": row.get("ai_mentioned", "Not checked"),
                "notes": row.get("notes", ""),
            },
        )
    st.session_state.setdefault(
        "gap_analysis", [row.copy() for row in SAMPLE_GAP_ANALYSIS]
    )
    legacy_competitors = {"Biryani Point", "Chettinad House", "Little Chennai"}
    if any(
        row.get("competitor") in legacy_competitors
        for row in st.session_state.gap_analysis
    ):
        st.session_state.gap_analysis = [
            row.copy() for row in SAMPLE_GAP_ANALYSIS
        ]
    if (
        {row.get("keyword") for row in st.session_state.gap_analysis}
        == sample_keyword_names
        and all(
            not row.get("competitor") and not row.get("gap")
            for row in st.session_state.gap_analysis
        )
    ):
        clear_widget_values("gap_keyword_", "gap_competitor_", "gap_detail_", "gap_priority_")
        st.session_state.gap_analysis = [
            row.copy() for row in SAMPLE_GAP_ANALYSIS
        ]
    profile = st.session_state.restaurant_profile
    st.session_state.setdefault(
        "content_assets",
        get_default_content_assets(
            profile.get("name", "Restaurant"),
            profile.get("cuisine", "Local cuisine"),
            profile.get("city", "Local area"),
        ),
    )
    st.session_state.setdefault(
        "action_plan",
        get_default_action_plan(
            profile.get("name", "Restaurant"),
            st.session_state.keyword_rows,
        ),
    )


st.set_page_config(page_title="FoodReach", layout="wide")
seed_session_state()

st.title("FoodReach")
st.caption("Local SEO + AEO workspace for independent restaurants")

with st.sidebar:
    st.caption("Challenge 4 - Team 14")

page = st.navigation(
    [
        st.Page("app_pages/overview.py", title="Overview", icon=":material/home:"),
        st.Page(
            "app_pages/restaurant_profile.py",
            title="Restaurant profile",
            icon=":material/storefront:",
        ),
        st.Page(
            "app_pages/map_board.py",
            title="Map board",
            icon=":material/map:",
            help="View the restaurant and nearby activity hotspots on a distance-based local map.",
        ),
        st.Page(
            "app_pages/keyword_research.py",
            title="Keyword research",
            icon=":material/search:",
        ),
        st.Page(
            "app_pages/visibility_checks.py",
            title="Visibility checks",
            icon=":material/visibility:",
        ),
        st.Page(
            "app_pages/gap_analysis.py",
            title="Gap analysis",
            icon=":material/compare_arrows:",
        ),
        st.Page(
            "app_pages/content_studio.py",
            title="Content studio",
            icon=":material/edit_document:",
        ),
        st.Page(
            "app_pages/action_plan.py",
            title="30-day plan",
            icon=":material/calendar_month:",
        ),
    ],
    position="sidebar",
)

page.run()
