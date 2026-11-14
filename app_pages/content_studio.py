import streamlit as st

from page_one_builder.sample_data import get_default_content_assets

st.session_state.setdefault("restaurant_profile", {"name": "Restaurant", "cuisine": "", "city": "", "website": ""})
st.session_state.setdefault("content_assets", get_default_content_assets("Restaurant", "Local cuisine", "Local area"))

st.subheader("Content studio")
st.write("Review and edit the sample content for the selected restaurant.")

if st.button("Regenerate sample drafts"):
    profile = st.session_state.restaurant_profile
    st.session_state.content_assets = get_default_content_assets(
        profile.get("name", "Restaurant"),
        profile.get("cuisine", "Local cuisine"),
        profile.get("city", "Local area"),
    )
    st.success("Drafts refreshed.")

content = st.session_state.content_assets

with st.container(border=True):
    st.markdown("### Business description")
    st.text_area("Edit description", value=content.get("business_description", ""), key="business_description")

with st.container(border=True):
    st.markdown("### Four weekly Google posts")
    for idx, post in enumerate(content.get("weekly_posts", []), start=1):
        st.text_area(f"Week {idx} post", value=post, key=f"weekly_post_{idx}")

with st.container(border=True):
    st.markdown("### FAQ answers")
    for idx, faq in enumerate(content.get("faq", []), start=1):
        st.text_area(f"FAQ {idx}", value=faq, key=f"faq_{idx}")

with st.container(border=True):
    st.markdown("### Schema markup")
    st.code(content.get("schema", "{}"), language="json")

with st.container(border=True):
    st.markdown("### Review request")
    st.text_area("Customer review text", value=content.get("review_request", ""), key="review_request")

if st.button("Save content updates"):
    st.session_state.content_assets = {
        "business_description": st.session_state.get("business_description", ""),
        "weekly_posts": [
            st.session_state.get(f"weekly_post_{idx}", "") for idx in range(1, 5)
        ],
        "faq": [st.session_state.get(f"faq_{idx}", "") for idx in range(1, 6)],
        "schema": st.session_state.get("content_assets", {}).get("schema", "{}"),
        "review_request": st.session_state.get("review_request", ""),
    }
    st.success("Content saved for this session.")
