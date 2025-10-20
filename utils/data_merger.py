def dedupe_contacts_by_email(contacts):
    seen = set()
    out = []
    for c in contacts:
        email = (c.get("email") or "").lower()
        if email and email not in seen:
            seen.add(email)
            out.append(c)
        elif not email:
            weak = (c.get("name","") + "|" + c.get("title","")).lower()
            if weak and weak not in seen:
                seen.add(weak)
                out.append(c)
    return out

def merge_companies(apollo, crunchbase, hiring):
    """
    Merge companies from multiple sources, deduplicate, and attach signals.
    """
    merged = []
    crunch_index = {c["company_name"].lower(): c for c in crunchbase}
    hiring_index = {c["company_name"].lower(): c for c in hiring}
    
    for comp in apollo:
        key = comp["company_name"].lower()
        # attach funding
        fund = crunch_index.get(key)
        if fund:
            comp["funding_stage"] = fund.get("funding_stage")
            comp["funding_amount"] = fund.get("funding_amount")
            comp.setdefault("signals", {})["recent_funding"] = fund.get("recent_funding")
            comp["source"].extend(fund.get("source", []))
        # attach hiring
        hire = hiring_index.get(key)
        if hire:
            comp.setdefault("signals", {})["recent_hiring"] = hire.get("recent_hiring")
            comp["signals"]["roles"] = hire.get("roles")
            comp["source"].extend(hire.get("source", []))
        # dedupe contacts
        comp["contacts"] = dedupe_contacts_by_email(comp["contacts"])
        comp["source"] = list(set(comp["source"]))
        merged.append(comp)
    return merged
