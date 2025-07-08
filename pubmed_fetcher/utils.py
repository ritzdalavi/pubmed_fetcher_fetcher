import re

def is_non_academic(affiliation: str) -> bool:
    return not any(
        keyword in affiliation.lower()
        for keyword in ["university", "college", "institute", "school", "hospital"]
    )

def get_company_name(affiliation: str) -> str:
    return affiliation.strip().split(",")[0]

def extract_email(text: str) -> str:
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group(0) if match else ""
