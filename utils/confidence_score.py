def compute_confidence(company, icp):
    """
    Simple heuristic score:
    0.4 * industry_match + 0.3 * funding + 0.2 * hiring + 0.1 * keyword match
    """
    industry_list = [i.lower() for i in icp.get("industry",[])]
    keywords = [k.lower() for k in icp.get("keywords",[])]
    
    industry_match = 1.0 if company.get("industry","").lower() in industry_list else 0.0
    funding_signal = 1.0 if company.get("signals",{}).get("recent_funding") else 0.0
    hiring_signal = 1.0 if company.get("signals",{}).get("recent_hiring") else 0.0
    keyword_match = 1.0 if any(k in company.get("company_name","").lower() for k in keywords) else 0.0
    
    score = 0.4*industry_match + 0.3*funding_signal + 0.2*hiring_signal + 0.1*keyword_match
    return round(score,3)
