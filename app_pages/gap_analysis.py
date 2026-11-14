import streamlit as st

st.session_state.setdefault("gap_analysis", [])

st.subheader("Gap analysis")
st.write(
    "Review the example competitor comparisons for each selected keyword. The competitor names are fictional; replace the examples with public listing observations before making business decisions."
)

comparison_areas = st.columns(3)
comparison_areas[0].markdown("**Business profile**\n\nCategories - hours - website")
comparison_areas[1].markdown("**Menu and media**\n\nMenu coverage - photos - posts")
comparison_areas[2].markdown("**Reputation signals**\n\nReview count - rating - review themes")

existing_rows = {
    row.get("keyword"): row for row in st.session_state.gap_analysis
}
st.session_state.gap_analysis = [
    existing_rows.get(
        keyword_row["keyword"],
        {
            "keyword": keyword_row["keyword"],
            "competitor": "",
            "gap": "",
            "priority": keyword_row.get("intent", "Medium"),
        },
    )
    for keyword_row in st.session_state.get("keyword_rows", [])
]

with st.form("gap_analysis_form"):
    rows = st.session_state.gap_analysis
    if not rows:
        st.info("Add keywords before recording competitor comparisons.")
    for index, row in enumerate(rows):
        st.markdown(f"### {row.get('keyword', f'Keyword {index + 1}')}")
        st.text_input(
            "Keyword",
            value=row.get("keyword", ""),
            key=f"gap_keyword_{index}",
            disabled=True,
        )
        st.text_input(
            "Top competitor",
            value=row.get("competitor", ""),
            placeholder="Enter a competitor you observed in search results",
            key=f"gap_competitor_{index}",
        )
        st.text_area(
            "Observed gap and evidence",
            value=row.get("gap", ""),
            placeholder="For example: competitor has a menu page for this dish; include the URL or observation date.",
            key=f"gap_detail_{index}",
        )
        priority = st.selectbox(
            "Priority",
            options=["High", "Medium", "Low"],
            index=["High", "Medium", "Low"].index(row.get("priority", "High")),
            key=f"gap_priority_{index}",
        )
        st.divider()
    submitted = st.form_submit_button("Save gap analysis", type="primary")

if submitted:
    updated_rows = []
    for index, row in enumerate(st.session_state.gap_analysis):
        updated_rows.append(
            {
                "keyword": st.session_state.get(f"gap_keyword_{index}", row.get("keyword", "")).strip(),
                "competitor": st.session_state.get(f"gap_competitor_{index}", row.get("competitor", "")).strip(),
                "gap": st.session_state.get(f"gap_detail_{index}", row.get("gap", "")).strip(),
                "priority": st.session_state.get(f"gap_priority_{index}", row.get("priority", "High")),
            }
        )
    st.session_state.gap_analysis = [item for item in updated_rows if item["keyword"] or item["competitor"]]
    st.success("Gap analysis saved.")

if st.session_state.gap_analysis:
    st.subheader("Current comparison notes")
    for row in st.session_state.gap_analysis:
        if row.get("competitor") or row.get("gap"):
            st.markdown(
                f"- **{row.get('keyword', 'Keyword')}** vs "
                f"**{row.get('competitor') or 'competitor not recorded'}** — "
                f"{row.get('priority', 'High')} priority: "
                f"{row.get('gap') or 'No evidence recorded.'}"
            )
