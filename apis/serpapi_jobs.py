def fetch_hiring_signals(icp):
    """
    Mock function to fetch hiring/job signals.
    """
    print(" Fetching mock hiring signals from SerpAPI...")
    
    mock_hiring = [
        {
            "company_name": "DataIQ Inc",
            "recent_hiring": True,
            "roles": ["Data Engineer", "ML Engineer"],
            "source": ["SerpAPI"]
        },
        {
            "company_name": "Finlytix Corp",
            "recent_hiring": False,
            "roles": [],
            "source": ["SerpAPI"]
        }
    ]
    
    return mock_hiring
