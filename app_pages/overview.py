import streamlit as st

st.session_state.setdefault("restaurant_profile", {"name": "Restaurant", "cuisine": "", "city": "", "website": ""})
st.session_state.setdefault("keyword_rows", [])
st.session_state.setdefault("visibility_checks", {})
st.session_state.setdefault("content_assets", {})

profile = st.session_state.restaurant_profile
keywords = st.session_state.keyword_rows

checked_keywords = sum(
    1
    for row in keywords
    if row.get("maps_rank") not in (None, "Not checked")
    or row.get("google_page_one") not in (None, "Not checked")
    or row.get("ai_mentioned") not in (None, "Not checked")
)

st.subheader("Your local search workspace")
st.write(
    "Use this dashboard to plan the restaurant’s search visibility across Maps, Google Search, and AI-powered answer engines."
)

metric_columns = st.columns(4)
metric_columns[0].metric("Restaurant", profile.get("name") or "Not set")
metric_columns[1].metric("Keywords", len(keywords))
metric_columns[2].metric("Completed checks", f"{checked_keywords} / {len(keywords) or 1}")
metric_columns[3].metric("Content assets", len(st.session_state.get("content_assets", {})))

st.subheader("Workflow")
workflow_columns = st.columns(3)
workflow_columns[0].info("1 - Define the restaurant and service area")
workflow_columns[1].info("2 - Research keywords and capture visibility")
workflow_columns[2].info("3 - Find gaps and prepare improvements")

st.subheader("Priority snapshot")
priority_keywords = keywords[:3] if keywords else []
if priority_keywords:
    for row in priority_keywords:
        st.markdown(f"- **{row['keyword']}** — {row['group']} / {row['intent']} intent")
else:
    st.info("Add a few keyword opportunities to build the action plan.")

