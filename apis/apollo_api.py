import json

def fetch_from_apollo(icp):
    """
    Mock function to fetch companies and contacts from Apollo.
    """
    print(" Fetching mock companies from Apollo...")
    
    mock_companies = [
        {
            "company_name": "DataIQ Inc",
            "domain": "dataiq.com",
            "revenue": 75000000,
            "industry": "B2B Software",
            "employee_count": 150,
            "contacts": [
                {
                    "name": "Sarah Green",
                    "title": "VP Data Science",
                    "email": "sarah@dataiq.com",
                    "linkedin": "linkedin.com/in/sarahgreen"
                }
            ],
            "source": ["Apollo"]
        },
        {
            "company_name": "Finlytix Corp",
            "domain": "finlytix.com",
            "revenue": 50000000,
            "industry": "FinTech",
            "employee_count": 120,
            "contacts": [
                {
                    "name": "John Smith",
                    "title": "Head of Analytics",
                    "email": "john@finlytix.com",
                    "linkedin": "linkedin.com/in/johnsmith"
                }
            ],
            "source": ["Apollo"]
        }
    ]
    
    return mock_companies
