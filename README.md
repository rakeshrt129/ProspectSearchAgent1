ProspectSearchAgent – AI-Powered B2B Prospect Finder:

ProspectSearchAgent is an AI-assisted data enrichment tool designed to automatically discover B2B companies and decision-makers in the USA that match a given Ideal Customer Profile (ICP).
It integrates multiple public and free-trial APIs like Apollo, Crunchbase, Hunter.io, and SerpAPI to collect, merge, and enrich firmographic and contact-level data — all in one place.

Project Overview:

This project was built as part of a technical assignment where the goal was to design an autonomous prospecting agent that:

Accepts ICP parameters (like revenue, industry, geography, tech stack).

Fetches company and contact data from multiple APIs.

Detects signals such as funding, hiring trends, and tech stack.

Returns a deduplicated and enriched JSON output with a confidence score.

Features:

AI-assisted development — built using tools like Cursor and ChatGPT for rapid coding.
Multi-API integration — connects with:

Apollo API → company + contact info

Crunchbase API → funding & company details

Hunter.io API → email verification

SerpAPI → hiring or signal extraction from job postings
 ICP-based filtering — allows flexible search by industry, revenue range, keywords, and location.
 Merging and deduplication — intelligently combines results across sources.
 Confidence scoring — assigns a score based on data completeness and signal strength.
 JSON output — neatly structured for easy export or downstream use.

 Example ICP Input:
{
  "revenue_min": 20000000,
  "revenue_max": 200000000,
  "industry": ["B2B Software", "FinTech"],
  "geography": ["USA"],
  "employee_count_min": 100,
  "keywords": ["AI", "data analytics", "automation", "machine learning"],
  "signals": {
    "funding": true,
    "hiring_data_roles": true,
    "tech_stack": ["Snowflake", "AWS"]
  }
}


Example Output
[
  {
    "company_name": "DataIQ Inc",
    "domain": "dataiq.com",
    "revenue": 75000000,
    "industry": "Software",
    "funding_stage": "Series B",
    "contacts": [
      {
        "name": "Sarah Green",
        "title": "VP Data Science",
        "email": "sarah@dataiq.com",
        "linkedin": "https://linkedin.com/in/sarahgreen"
      }
    ],
    "signals": {
      "recent_hiring": true,
      "new_funding": true
    },
    "source": ["Apollo", "Crunchbase"],
    "confidence": 0.92
  }
]


Tech Stack:
 _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
| Function                 | Technology / API    | Notes                               |
| ------------------------ | ------------------- | ----------------------------------- |
| Core Language            | Python 3.10+        | Async API calls and data processing |
| Company & Contact Search | Apollo.io API       | Rich company and contact data       |
| Funding & Firmographics  | Crunchbase API      | Funding stage, size, and location   |
| Hiring Signals           | SerpAPI             | Scrapes job listings                |
| Email Verification       | Hunter.io           | Checks email validity               |
| Storage                  | JSON / CSV / SQLite | Output persistence                  |
| Version Control          | Git + GitHub        | Code management                     |
 --------------------------  -------------------   ------------------------------------


API Setup:

Create .env file in your project root:

APOLLO_API_KEY=your_apollo_key
CRUNCHBASE_API_KEY=your_crunchbase_key
HUNTER_API_KEY=your_hunter_key
SERPAPI_KEY=your_serpapi_key

Keep your keys private — never commit .env to GitHub.

