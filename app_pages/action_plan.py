import streamlit as st

from page_one_builder.sample_data import get_default_action_plan

st.session_state.setdefault("restaurant_profile", {"name": "Restaurant", "cuisine": "", "city": "", "website": ""})
st.session_state.setdefault("keyword_rows", [])
st.session_state.setdefault("gap_analysis", [])
st.session_state.setdefault("action_plan", [])

profile = st.session_state.restaurant_profile
keywords = st.session_state.keyword_rows

if not st.session_state.action_plan:
    st.session_state.action_plan = get_default_action_plan(
        profile.get("name", "Restaurant"),
        keywords,
    )

st.subheader("30-day action plan")
st.write("Turn the findings into a realistic, owner-approved monthly workflow.")

priority_keywords = keywords[:3] if keywords else []
if priority_keywords:
    st.markdown("### Priority keywords")
    for row in priority_keywords:
        st.markdown(f"- **{row.get('keyword', 'Keyword')}** — {row.get('group', 'Keyword')} / {row.get('intent', 'Medium')} intent")

st.markdown("### Weekly plan")
for item in st.session_state.action_plan:
    st.markdown(f"**{item['week']} — {item['title']}**")
    st.write(item["action"])

if st.session_state.gap_analysis:
    st.markdown("### Gaps to address first")
    for row in st.session_state.gap_analysis:
        st.markdown(f"- **{row.get('keyword', 'Keyword')}**: {row.get('gap', 'No gap noted.')}")

if st.button("Refresh plan"):
    st.session_state.action_plan = get_default_action_plan(
        profile.get("name", "Restaurant"),
        keywords,
    )
    st.success("Plan refreshed from the current profile and keyword list.")
