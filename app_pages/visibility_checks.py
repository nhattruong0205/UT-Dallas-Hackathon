import streamlit as st

st.session_state.setdefault("keyword_rows", [])

st.subheader("Visibility checks")
st.write(
    "Review the example Maps, Google Search, and AI-answer observations for each keyword. Replace them with your own manual checks when using this for a real restaurant."
)

with st.form("visibility_checks_form"):
    for index, row in enumerate(st.session_state.keyword_rows):
        st.markdown(f"### {row.get('keyword', f'Keyword {index + 1}')}")
        st.selectbox(
            "Maps position",
            options=[
                "Not checked",
                "#1",
                "#2",
                "#3",
                "Top 3",
                "#4-10",
                "#11-20",
                "Not in top 20",
            ],
            index=[
                "Not checked",
                "#1",
                "#2",
                "#3",
                "Top 3",
                "#4-10",
                "#11-20",
                "Not in top 20",
            ].index(row.get("maps_rank", "Not checked")),
            key=f"maps_rank_{index}",
        )
        st.selectbox(
            "Google page 1",
            options=["Not checked", "Yes", "No"],
            index=["Not checked", "Yes", "No"].index(row.get("google_page_one", "Not checked")),
            key=f"google_page_one_{index}",
        )
        st.selectbox(
            "Named by AI",
            options=["Not checked", "Yes", "No"],
            index=["Not checked", "Yes", "No"].index(row.get("ai_mentioned", "Not checked")),
            key=f"ai_mentioned_{index}",
        )
        st.text_area(
            "Evidence notes",
            value=row.get("notes", ""),
            key=f"visibility_notes_{index}",
        )
        st.divider()

    submitted = st.form_submit_button("Save visibility checks", type="primary")

if submitted:
    for index, row in enumerate(st.session_state.keyword_rows):
        row["maps_rank"] = st.session_state.get(f"maps_rank_{index}", row.get("maps_rank", "Not checked"))
        row["google_page_one"] = st.session_state.get(f"google_page_one_{index}", row.get("google_page_one", "Not checked"))
        row["ai_mentioned"] = st.session_state.get(f"ai_mentioned_{index}", row.get("ai_mentioned", "Not checked"))
        row["notes"] = st.session_state.get(f"visibility_notes_{index}", row.get("notes", "")).strip()
    st.success("Visibility checks saved.")

if not st.session_state.keyword_rows:
    st.info("Add keyword opportunities from the keyword research page to begin checking visibility.")
