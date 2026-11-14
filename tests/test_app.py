import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"
PAGE_FILES = [
    "overview.py",
    "restaurant_profile.py",
    "map_board.py",
    "keyword_research.py",
    "visibility_checks.py",
    "gap_analysis.py",
    "content_studio.py",
    "action_plan.py",
]


class PageOneBuilderAppTests(unittest.TestCase):
    def test_seeded_keywords_visibility_and_gap_records(self) -> None:
        app = AppTest.from_file(str(APP_PATH)).run()

        keywords = app.session_state["keyword_rows"]
        gaps = app.session_state["gap_analysis"]
        self.assertEqual(len(keywords), 10)
        self.assertEqual(
            [row["keyword"] for row in keywords],
            [
                "chettinad chicken Richardson",
                "chicken biryani Richardson",
                "dosa Richardson TX",
                "parotta Dallas",
                "South Indian restaurant Richardson",
                "South Indian lunch Plano",
                "Indian lunch buffet Richardson",
                "halal biryani near UTD",
                "late night Indian food Richardson",
                "Indian food near UTD",
            ],
        )
        self.assertEqual(
            [row["keyword"] for row in gaps],
            [row["keyword"] for row in keywords],
        )
        self.assertTrue(
            all(
                row["maps_rank"] != "Not checked"
                and row["google_page_one"] in {"Yes", "No"}
                and row["ai_mentioned"] in {"Yes", "No"}
                and row["notes"]
                for row in keywords
            )
        )
        self.assertTrue(
            all(
                row["competitor"]
                and row["gap"]
                and row["priority"] in {"High", "Medium", "Low"}
                for row in gaps
            )
        )

    def test_workflow_pages_render(self) -> None:
        app = AppTest.from_file(str(APP_PATH)).run()
        self.assertFalse(app.exception)

        for page_file in PAGE_FILES:
            with self.subTest(page=page_file):
                app.switch_page(f"app_pages/{page_file}").run()
                self.assertFalse(app.exception)

    def test_profile_form_saves_session_values(self) -> None:
        app = AppTest.from_file(str(APP_PATH)).run()
        app.switch_page("app_pages/restaurant_profile.py").run()

        for field, value in zip(
            app.text_input,
            ["Test Bistro", "Tamil", "Plano, TX", "https://example.test"],
        ):
            field.set_value(value)
        app.button[0].click().run()

        self.assertEqual(
            app.session_state["restaurant_profile"],
            {
                "name": "Test Bistro",
                "cuisine": "Tamil",
                "city": "Plano, TX",
                "website": "https://example.test",
                "latitude": 32.986,
                "longitude": -96.75,
            },
        )
        self.assertFalse(app.exception)


if __name__ == "__main__":
    unittest.main()
