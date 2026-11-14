# FoodReach

A Streamlit workspace for restaurant teams to organize local SEO and
answer-engine visibility work.

## Status

The app includes an editable, session-only restaurant profile and 10 sample
keywords. The Map Board compares the restaurant marker with nearby hotspot
areas. It starts with illustrative sample points; teams can upload aggregated
hotspot data using a CSV with `latitude`, `longitude`, and `weight` columns
(optional `area`). Do not upload individual customer addresses. Visibility
checks and competitor comparisons also start with sample values. The app does
not fetch live results, call an AI service, or publish content.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

Keep API keys out of source control. When an AI integration is added, load its
key from an environment variable or Streamlit secrets.

## Run the smoke tests

```powershell
python -m unittest discover -s tests
```

## Project layout

```text
app.py                         FoodReach navigation and shared session state
app_pages/                     Individual workflow screens
  map_board.py                 Restaurant and hotspot map
page_one_builder/
  sample_data.py               Explicitly illustrative starter data
tests/
  test_app.py                  Page navigation and profile form checks
docs/
  challenge_4_page_one_builder.md
```

## Next increments

1. Load and select restaurants from the event CSV.
2. Connect verified buyer-area or search-interest datasets.
3. Generate, validate, and edit keyword ideas using an AI provider.
4. Persist profiles, research, checks, and plans beyond a browser session.
5. Export the content drafts and 30-day plan for review.
