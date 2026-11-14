"""Sample data and generation helpers for the FoodReach app."""

SAMPLE_RESTAURANT = {
    "name": "Sample Chettinad Kitchen",
    "cuisine": "South Indian (Chettinad)",
    "city": "Richardson, TX",
    "website": "https://example.com",
    "latitude": 32.9860,
    "longitude": -96.7500,
}

SAMPLE_BUYER_HOTSPOTS = [
    {"area": "UT Dallas campus", "latitude": 32.9865, "longitude": -96.7505, "weight": 10},
    {"area": "UT Dallas north", "latitude": 32.9910, "longitude": -96.7510, "weight": 8},
    {"area": "North Richardson", "latitude": 33.0020, "longitude": -96.7350, "weight": 7},
    {"area": "CityLine", "latitude": 32.9850, "longitude": -96.7130, "weight": 8},
    {"area": "Spring Creek", "latitude": 33.0100, "longitude": -96.7400, "weight": 6},
    {"area": "Richardson Heights", "latitude": 32.9630, "longitude": -96.7390, "weight": 5},
    {"area": "West Richardson", "latitude": 32.9860, "longitude": -96.7770, "weight": 6},
    {"area": "Plano south", "latitude": 33.0180, "longitude": -96.7520, "weight": 5},
    {"area": "Renner and Central", "latitude": 32.9990, "longitude": -96.7140, "weight": 7},
    {"area": "Campbell corridor", "latitude": 32.9760, "longitude": -96.7330, "weight": 6},
]

SAMPLE_KEYWORDS = [
    {
        "keyword": "chettinad chicken Richardson",
        "group": "Dish",
        "why_it_matters": "Signature dish; few local competitors claim it, so it's the easiest to win.",
        "intent": "High",
        "maps_rank": "#2",
        "google_page_one": "Yes",
        "ai_mentioned": "Yes",
        "notes": "Strong local fit for a signature dish; add a detailed menu description and current photo.",
    },
    {
        "keyword": "chicken biryani Richardson",
        "group": "Dish",
        "why_it_matters": "Biggest Indian dish search; searchers are ready to order now.",
        "intent": "High",
        "maps_rank": "#4-10",
        "google_page_one": "Yes",
        "ai_mentioned": "No",
        "notes": "Popular dish search; make ordering details and menu information easy to find.",
    },
    {
        "keyword": "dosa Richardson TX",
        "group": "Dish",
        "why_it_matters": "Marks it as South Indian, setting it apart from North Indian places.",
        "intent": "High",
        "maps_rank": "#3",
        "google_page_one": "Yes",
        "ai_mentioned": "Yes",
        "notes": "Good South Indian differentiator; include available dosa varieties in the menu.",
    },
    {
        "keyword": "parotta Dallas",
        "group": "Dish",
        "why_it_matters": "Niche dish few menus list, so it's easy to rank with good menu text.",
        "intent": "Medium",
        "maps_rank": "Not in top 20",
        "google_page_one": "No",
        "ai_mentioned": "No",
        "notes": "Niche dish with room to improve menu coverage and local visibility.",
    },
    {
        "keyword": "South Indian restaurant Richardson",
        "group": "Cuisine + area",
        "why_it_matters": "Main category search that new residents and students use.",
        "intent": "High",
        "maps_rank": "#4-10",
        "google_page_one": "Yes",
        "ai_mentioned": "Yes",
        "notes": "Useful cuisine-and-city phrase; keep the profile and website details consistent.",
    },
    {
        "keyword": "South Indian lunch Plano",
        "group": "Cuisine + area",
        "why_it_matters": "Captures the nearby Plano office lunch crowd.",
        "intent": "High",
        "maps_rank": "#11-20",
        "google_page_one": "No",
        "ai_mentioned": "No",
        "notes": "Lunch opportunity in a nearby market; highlight verified weekday hours.",
    },
    {
        "keyword": "Indian lunch buffet Richardson",
        "group": "Cuisine + area",
        "why_it_matters": "Real buffet feature; buffet searchers are already deciding where to eat.",
        "intent": "High",
        "maps_rank": "#3",
        "google_page_one": "Yes",
        "ai_mentioned": "Yes",
        "notes": "Buffet searches show strong intent; make availability and schedule clear.",
    },
    {
        "keyword": "halal biryani near UTD",
        "group": "Need",
        "why_it_matters": "Many halal-observant students; 'halal' decides where they eat.",
        "intent": "High",
        "maps_rank": "#4-10",
        "google_page_one": "Yes",
        "ai_mentioned": "Yes",
        "notes": "Dietary details matter; confirm them before adding halal claims to public content.",
    },
    {
        "keyword": "late night Indian food Richardson",
        "group": "Need",
        "why_it_matters": "Open till 11 PM, later than most competitors.",
        "intent": "Medium",
        "maps_rank": "#11-20",
        "google_page_one": "No",
        "ai_mentioned": "No",
        "notes": "Late-hour opportunity; keep closing time accurate wherever it appears.",
    },
    {
        "keyword": "Indian food near UTD",
        "group": "Need",
        "why_it_matters": "Campus traffic, and the question students ask AI assistants.",
        "intent": "High",
        "maps_rank": "#2",
        "google_page_one": "Yes",
        "ai_mentioned": "Yes",
        "notes": "Campus-area opportunity; make directions and distance easy to understand.",
    },
]

SAMPLE_GAP_ANALYSIS = [
    {
        "keyword": "chettinad chicken Richardson",
        "competitor": "Sample Competitor A",
        "gap": "Competitor menu features the signature dish clearly; add a fuller menu description and current photo.",
        "priority": "High",
    },
    {
        "keyword": "chicken biryani Richardson",
        "competitor": "Sample Competitor B",
        "gap": "Competitor has a dedicated biryani page; add menu details, ordering links, and current photos.",
        "priority": "High",
    },
    {
        "keyword": "dosa Richardson TX",
        "competitor": "Sample Competitor C",
        "gap": "Competitor explains dosa varieties; describe available options and serving style on the menu.",
        "priority": "High",
    },
    {
        "keyword": "parotta Dallas",
        "competitor": "Sample Competitor A",
        "gap": "Competitor includes parotta in its menu; add a clear description and dish photo.",
        "priority": "Medium",
    },
    {
        "keyword": "South Indian restaurant Richardson",
        "competitor": "Sample Competitor C",
        "gap": "Competitor uses consistent cuisine details on its profile and website; align those business facts.",
        "priority": "High",
    },
    {
        "keyword": "South Indian lunch Plano",
        "competitor": "Sample Competitor D",
        "gap": "Competitor highlights lunch hours and weekday options; make verified lunch details easier to find.",
        "priority": "High",
    },
    {
        "keyword": "Indian lunch buffet Richardson",
        "competitor": "Sample Competitor B",
        "gap": "Competitor lists buffet availability and hours; publish accurate buffet days, hours, and menu details.",
        "priority": "High",
    },
    {
        "keyword": "halal biryani near UTD",
        "competitor": "Sample Competitor E",
        "gap": "Competitor provides clear dietary information; confirm halal details before publishing any claim.",
        "priority": "High",
    },
    {
        "keyword": "late night Indian food Richardson",
        "competitor": "Sample Competitor D",
        "gap": "Competitor shows its closing time clearly; verify and consistently publish late-night hours.",
        "priority": "Medium",
    },
    {
        "keyword": "Indian food near UTD",
        "competitor": "Sample Competitor E",
        "gap": "Competitor makes directions easy to find; clarify the route and distance from campus.",
        "priority": "High",
    },
]


def get_default_content_assets(restaurant_name: str, cuisine: str, city: str) -> dict:
    return {
        "business_description": (
            f"{restaurant_name} serves {cuisine} in {city}, bringing bold flavors, fresh ingredients, "
            "and a warm neighborhood dining experience to local guests. Our menu highlights house specialties, "
            "family-style meals, and convenient options for lunch, dinner, and special occasions."
        ),
        "weekly_posts": [
            "This week we are spotlighting our signature dishes and fresh lunch specials for nearby diners.",
            "We are sharing quick updates on our menu favorites, service hours, and family-friendly dining options.",
            "Looking for a flavorful local meal? Explore our menu and see what guests are ordering this week.",
            "We are proud to serve the community with fresh ingredients, welcoming service, and delicious dishes.",
        ],
        "faq": [
            "Q: Do you offer vegetarian options? A: Yes, we offer a range of vegetarian dishes and appetizers.",
            "Q: Is the food family-friendly? A: Yes, we serve casual dining favorites suitable for families and groups.",
            "Q: Do you offer lunch specials? A: Yes, lunch favorites are available during the week and are ideal for a quick local meal.",
            "Q: Do you have takeout or delivery? A: We offer convenient takeout options and can help guests with ordering questions.",
            "Q: Are you near the local community? A: We are proud to serve guests in the Richardson / Plano area and nearby neighborhoods.",
        ],
        "schema": (
            '{"@context": "https://schema.org", "@type": "Restaurant", "name": "Sample Chettinad Kitchen", '
            '"servesCuisine": ["South Indian", "Chettinad"], "address": {"@type": "PostalAddress", '
            '"addressLocality": "Richardson", "addressRegion": "TX"}, "telephone": "[phone]", '
            '"openingHours": "Mo-Su 11:00-23:00", "menu": "https://example.com/menu"}'
        ),
        "review_request": (
            "Hi! If you enjoyed your meal, we would really appreciate a quick review. "
            "A few words about the food, service, or atmosphere helps other local diners discover us."
        ),
    }


def get_default_action_plan(restaurant_name: str, keywords: list[dict]) -> list[dict]:
    priority_keywords = ", ".join(row["keyword"] for row in keywords[:3])
    return [
        {
            "week": "Week 1",
            "title": "Verify core business facts",
            "action": f"Confirm {restaurant_name} name, cuisine, hours, menu highlights, and service area so the profile and content stay consistent.",
        },
        {
            "week": "Week 2",
            "title": "Fix the biggest keyword gaps",
            "action": f"Prioritize the highest-intent searches: {priority_keywords}. Update the profile, menu language, and website headings to match these terms.",
        },
        {
            "week": "Week 3",
            "title": "Publish local trust signals",
            "action": "Add fresh photos, review requests, and optimized posts that explain menu items, lunch offers, and dietary attributes.",
        },
        {
            "week": "Week 4",
            "title": "Measure and improve",
            "action": "Review ranking changes, AI mentions, and search visibility, then refine the next keyword list and content improvements.",
        },
    ]

