import streamlit as st

st.session_state.setdefault("keyword_rows", [])

st.subheader("Keyword research")
st.write("Organize opportunities by dish, cuisine + area, or customer need.")

if st.button("Add keyword row"):
    st.session_state.keyword_rows.append(
        {
            "keyword": "New restaurant keyword",
            "group": "Dish",
            "why_it_matters": "Add a short reason for why this keyword matters to nearby diners.",
            "intent": "Medium",
            "maps_rank": "Not checked",
            "google_page_one": "Not checked",
            "ai_mentioned": "Not checked",
            "notes": "",
        }
    )

with st.form("keyword_form"):
    for index, row in enumerate(st.session_state.keyword_rows):
        st.markdown(f"### Keyword {index + 1}")
        keyword = st.text_input(
            "Keyword",
            value=row.get("keyword", ""),
            key=f"keyword_name_{index}",
        )
        group = st.selectbox(
            "Group",
            options=["Dish", "Cuisine + area", "Need"],
            index=["Dish", "Cuisine + area", "Need"].index(row.get("group", "Dish")),
            key=f"keyword_group_{index}",
        )
        why = st.text_area(
            "Why it matters",
            value=row.get("why_it_matters", ""),
            key=f"keyword_why_{index}",
        )
        intent = st.selectbox(
            "Intent",
            options=["High", "Medium", "Low"],
            index=["High", "Medium", "Low"].index(row.get("intent", "Medium")),
            key=f"keyword_intent_{index}",
        )
        notes = st.text_area(
            "Notes",
            value=row.get("notes", ""),
            key=f"keyword_notes_{index}",
        )
        st.caption("Visibility status is managed on the next page.")
        st.divider()

    submitted = st.form_submit_button("Save keyword list", type="primary")

if submitted:
    updated_rows = []
    for index, row in enumerate(st.session_state.keyword_rows):
        updated_rows.append(
            {
                "keyword": st.session_state.get(f"keyword_name_{index}", row.get("keyword", "")).strip(),
                "group": st.session_state.get(f"keyword_group_{index}", row.get("group", "Dish")),
                "why_it_matters": st.session_state.get(f"keyword_why_{index}", row.get("why_it_matters", "")).strip(),
                "intent": st.session_state.get(f"keyword_intent_{index}", row.get("intent", "Medium")),
                "maps_rank": row.get("maps_rank", "Not checked"),
                "google_page_one": row.get("google_page_one", "Not checked"),
                "ai_mentioned": row.get("ai_mentioned", "Not checked"),
                "notes": st.session_state.get(f"keyword_notes_{index}", row.get("notes", "")).strip(),
            }
        )
    st.session_state.keyword_rows = [item for item in updated_rows if item["keyword"]]
    st.success("Keyword list updated.")
