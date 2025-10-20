import json
import os
from apis.apollo_api import fetch_from_apollo
from apis.crunchbase_api import fetch_from_crunchbase
from apis.serpapi_jobs import fetch_hiring_signals
from utils.data_merger import merge_companies
from utils.confidence_score import compute_confidence

def load_icp(path="config/icp_config.json"):
    with open(path,"r") as f:
        return json.load(f)

def run_agent():
    print(" Running ProspectSearchAgent...")
    
    icp = load_icp()
    
    # fetch mock data
    apollo = fetch_from_apollo(icp)
    crunchbase = fetch_from_crunchbase(icp)
    hiring = fetch_hiring_signals(icp)
    
    # merge & dedupe
    merged = merge_companies(apollo, crunchbase, hiring)
    
    # compute confidence
    for c in merged:
        c["confidence"] = compute_confidence(c, icp)
    
    # sort by confidence
    merged.sort(key=lambda x: x["confidence"], reverse=True)
    
    # save output
    os.makedirs("output", exist_ok=True)
    with open("output/results.json","w") as f:
        json.dump(merged, f, indent=2)
    
    print(f" Done! Results saved in output/results.json")
    print("Top companies:")
    for c in merged[:5]:
        print(f"{c['company_name']} — Confidence: {c['confidence']}")

if __name__ == "__main__":
    run_agent()
