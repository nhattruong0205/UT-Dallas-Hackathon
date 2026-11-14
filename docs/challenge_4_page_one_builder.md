# LLMSOFTWARE x UT DALLAS HACKATHON • CHALLENGE 4
# Page One Builder: 10 Keywords on Google Maps (SEO + AEO)
**Sat, Nov 14, 2026 • ECSS 2.410 • Build 2:15–4:15 PM (2 hours) • Code due 4:15 PM • Demos 4:20 PM**

---

### First 15 minutes: get set up
1. **Sit with your team (1–4 people).** Pick one person to share screen during the demo.
2. **Open Google Colab:** go to `colab.research.google.com`, sign in with any Google account, click **New notebook**.
3. Create the free accounts listed below for your challenge. If a sign-up gets stuck (for example on phone verification), go to the **help desk for a backup key**. Don't lose more than 10 minutes on sign-ups.
4. Download the event data from the link on your check-in card.

---

## The problem
When someone nearby searches "biryani near me", the top 3 restaurants on Google Maps get most of the calls and orders. Today people also ask AI assistants like ChatGPT and Google's AI Overviews where to eat. Most small restaurants don't know which searches they should win, or what to fix to get there.

## What you're building (core, 2 hours)
A tool called **Page One Builder**. Pick one of the sample restaurants (or a real Dallas-area restaurant) and:
1. **Find 10 keywords** it should rank for, in 3–4 groups: dish ("chettinad chicken Richardson"), cuisine plus area ("South Indian lunch Plano") and need ("halal biryani near UTD", "late night Indian food"). Say why each matters.
2. **Check where it stands today** for each keyword in three places: the Google Maps top 3 (local SEO), the first page of Google (SEO) and AI answers (AEO).
3. **Find the gaps:** compare its Google Business Profile with whoever is winning each keyword: categories, menu items, photos, review count and rating, words in reviews, hours, website, posts.
4. **Generate the fixes, ready to paste:** a better business description, 4 weekly Google posts, keyword-rich menu descriptions, one web page per keyword group, 5 FAQ answers, the schema code, and a text message asking real customers for a review.

**Stretch goal:** a rank tracker: a map grid showing the restaurant's rank for each keyword from points 1, 3 and 5 miles away.

---

## SEO vs AEO in one table

| | What it means for a restaurant | What your tool produces |
| :--- | :--- | :--- |
| **Local SEO (Maps)** | Google Business Profile matches the keywords | Categories, description, menu items, photo ideas and posts with the keywords; review requests to real customers |
| **SEO (website)** | A web page for each keyword group | Title tag, meta description, H1, 300–500 words, menu with prices, address and hours |
| **AEO (AI answers)** | AI assistants can find, trust and quote the facts | FAQ answers ("Is the biryani halal?"), schema markup, the same name, address and phone everywhere |

### Example output (illustrative)

| Keyword | Maps today | Page 1? | AI names it? | Biggest gap vs top 3 |
| :--- | :--- | :--- | :--- | :--- |
| halal biryani near UTD | #9 | No | No | No "halal" in profile or menu |
| chettinad chicken Richardson | #4 | Yes (#7) | Yes | 12 photos vs 140 for #1 |
| South Indian lunch Plano | not top 20 | No | No | No lunch hours or lunch menu |

---

## What we give you

| Item | What's in it |
| :--- | :--- |
| `restaurants.csv` | 2–3 sample restaurants: name, address, cuisine, website, menu link |
| Backup AI key | Help desk |

---

## Accounts you need

### Gemini API key (free)
1. Go to `aistudio.google.com` and sign in with a Google account.
2. Click **Get API key**, then **Create API key**. Copy the key.
3. In Colab, click the **key icon (Secrets)** in the left sidebar, add a secret named `GEMINI_API_KEY`, paste the key and turn on notebook access. On a laptop, put it in a `.env` file instead.

```python
!pip install -q google-genai
from google import genai
from google.colab import userdata          # on a laptop: os.getenv("GEMINI_API_KEY")
load_dotenv()

client = genai.Client(api_key=userdata.get("GEMINI_API_KEY"))
reply = client.models.generate_content(
    model="gemini-2.5-flash",              # or the current Flash model listed in AI Studio
    contents="Say hello to the UTD hackathon in one sentence.")
print(reply.text)
```

OpenAI works too if you already have an account with billing. It is not free, so ask the help desk for a backup key if you want it.

---

## Rank Checking & Execution Plan

No paid SEO tools. You check rankings by searching yourself (see below). Optional: free accounts on ChatGPT, Perplexity or Gemini to run the AI-answer check.

### How to check rankings by hand
1. Open a **private / incognito window** so your own history doesn't change the results.
2. Search each keyword on `google.com/maps` and note the restaurant's position (or "not in top 20") and who is #1–#3.
3. Search the same keyword on `google.com` and note whether the restaurant's website appears on page 1.
4. Ask ChatGPT, Gemini or Perplexity the keyword as a question ("Where can I get halal biryani near UTD?") and note whether the restaurant is named.
5. Split the 10 keywords between teammates: this takes about 20 minutes.

### Step-by-step plan

| Time | Step | Done when |
| :--- | :--- | :--- |
| **0:00–0:15** | Setup, Gemini key, pick the restaurant | Gemini replies in your notebook |
| **0:15–0:35** | Keyword engine: Gemini proposes 20 keywords; your team picks the best 10 | 10 keywords in groups, with reasons |
| **0:35–1:00** | Rank and AI-answer check (by hand, split across the team) | The table is filled in |
| **1:00–1:25** | Gap analysis vs the top 3 for each keyword | Biggest gap per keyword |
| **1:25–1:50** | Content generator: profile text, posts, web pages, FAQ, schema, review text | Everything ready to paste |
| **1:50–2:00** | Put it together as the 30-day plan; rehearse | Plan and code link ready |

---

## Starter code

### 1. Keyword engine
```python
import json
r = {"name": "Sample Chettinad Kitchen", "cuisine": "South Indian (Chettinad)",
     "address": "Richardson, TX 75080", "menu": "chicken biryani, chettinad chicken, dosa, parotta",
     "features": "halal, lunch buffet, open till 11 PM, near UT Dallas"}
prompt = f"""You are a local SEO expert. Restaurant: {r}.
Suggest 20 search keywords real people in this area type into Google Maps or ask AI assistants for a restaurant like this. Group them as dish, cuisine+area, or need. For each give: keyword, group, why it matters (1 line), estimated intent (high/medium/low).
Return JSON: a list of objects."""
reply = client.models.generate_content(model="gemini-2.5-flash", contents=prompt,
                                       config={"response_mime_type": "application/json"})
keywords = json.loads(reply.text)
for k in keywords: print(k)
```

### 2. Schema markup for AEO (put it in the website's `<head>`)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Sample Chettinad Kitchen",
  "servesCuisine": ["South Indian", "Chettinad", "Halal"],
  "address": {"@type": "PostalAddress", "streetAddress": "[street]", "addressLocality": "Richardson",
              "addressRegion": "TX", "postalCode": "75080"},
  "telephone": "[phone]",
  "openingHours": "Mo-Su 11:00-23:00",
  "menu": "https://[website]/menu",
  "acceptsReservations": "False"
}
</script>
```
Add a second block with `"@type": "FAQPage"` listing your 5 FAQ questions and answers. Ask Gemini to generate both blocks from your restaurant data, then check them with Google's free Rich Results Test.

---

## Rules & Guidelines

> **Rules: honest methods only**
> Follow Google's guidelines. No fake clicks, fake visits, fake searches, fake reviews, or asking only happy customers for reviews (review gating). Ideas that try to trick the ranking are disqualified. Don't edit any real business's Google listing during the event. Real ranking changes take weeks, so judges score your tool and the quality of what it produces, not ranking changes today.

> **Keys rule (judges check this)**
> Never type an API key, camera URL or password into your code or notebook text. Use Colab **Secrets** or a `.env` file, and add `.env` to `.gitignore`. A team whose submitted code contains a key loses points. All backup keys are turned off after the event.

---

## Submission, Demo & Scoring

### What to submit by 4:15 PM
1. **A link to your code:** GitHub repo (public or shared with `support@llmsoftware.com`), a shared Colab link, or a zip at the help desk. No keys inside.
2. **Your 10-keyword table, the gap analysis, and the 30-day plan with all generated content (one doc or PDF).**
3. **Your team sheet:** each member's name, UTD email, and whether you want an internship or full-time role.

### Demo (2 minutes at your judging table)
1. One sentence: the problem you solved.
2. Show it working live (not slides).
3. One sentence: what you would build next.

### How you're scored (100 points)

| Criterion | Points | What judges look for |
| :--- | :--- | :--- |
| **It works** | 30 | Live demo; the core challenge is done end to end |
| **Real-world usefulness** | 25 | Would a restaurant owner pay for this tomorrow? |
| **Use of AI** | 20 | AI does the hard part well and handles messy input |
| **Engineering quality** | 15 | Clean code, no keys in it, and the team can explain it |
| **Stretch goal and polish** | 10 | Went beyond the core with a clear experience |

*Questions during the event: raise your hand or visit the help desk. After the event: `support@llmsoftware.com`.*