def fetch_from_crunchbase(icp):
    """
    Mock function to fetch funding info from Crunchbase.
    """
    print(" Fetching mock funding info from Crunchbase...")
    
    mock_funding = [
        {
            "company_name": "DataIQ Inc",
            "funding_stage": "Series B",
            "funding_amount": 25000000,
            "recent_funding": True,
            "source": ["Crunchbase"]
        },
        {
            "company_name": "Finlytix Corp",
            "funding_stage": "Series A",
            "funding_amount": 15000000,
            "recent_funding": True,
            "source": ["Crunchbase"]
        }
    ]
    
    return mock_funding
