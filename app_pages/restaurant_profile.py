import streamlit as st

st.session_state.setdefault(
    "restaurant_profile",
    {
        "name": "",
        "cuisine": "",
        "city": "",
        "website": "",
        "latitude": 32.9860,
        "longitude": -96.7500,
    },
)

st.subheader("Restaurant profile")
st.write("Enter the business facts that will inform keyword ideas and future content.")
profile = st.session_state.restaurant_profile

with st.form("restaurant_profile_form"):
    name = st.text_input("Restaurant name", value=profile.get("name", ""))
    cuisine = st.text_input("Cuisine", value=profile.get("cuisine", ""))
    city = st.text_input("City or service area", value=profile.get("city", ""))
    website = st.text_input("Website (optional)", value=profile.get("website", ""))
    latitude = st.number_input(
        "Map latitude",
        min_value=-90.0,
        max_value=90.0,
        value=float(profile.get("latitude", 32.9860)),
        step=0.0001,
        format="%.6f",
    )
    longitude = st.number_input(
        "Map longitude",
        min_value=-180.0,
        max_value=180.0,
        value=float(profile.get("longitude", -96.7500)),
        step=0.0001,
        format="%.6f",
    )
    submitted = st.form_submit_button("Save profile", type="primary")

if submitted:
    st.session_state.restaurant_profile = {
        "name": name.strip(),
        "cuisine": cuisine.strip(),
        "city": city.strip(),
        "website": website.strip(),
        "latitude": latitude,
        "longitude": longitude,
    }
    st.success("Restaurant profile saved for this session.")
