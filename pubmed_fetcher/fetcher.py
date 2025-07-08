from typing import List, Dict, Optional
import requests
from xml.etree import ElementTree as ET
from pubmed_fetcher.utils import is_non_academic, get_company_name, extract_email

def fetch_pubmed_ids(query: str, debug: bool = False) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 100}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        ids = data.get("esearchresult", {}).get("idlist", [])
        if debug:
            print(f"Fetched {len(ids)} PubMed IDs for query: '{query}'")
        return ids
    except Exception as e:
        print(f"Error fetching PubMed IDs: {e}")
        return []

def fetch_paper_details(pubmed_id: str, debug: bool = False) -> Dict[str, str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "id": pubmed_id, "retmode": "xml"}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        article = root.find(".//PubmedArticle")
        if article is None:
            raise ValueError("No PubmedArticle found")

        title = article.findtext(".//ArticleTitle", "").strip()
        pub_date = article.findtext(".//PubDate/Year", "") or "N/A"

        authors: List[str] = []
        companies: List[str] = []
        email: Optional[str] = ""

        for author in article.findall(".//Author"):
            affiliation = author.findtext(".//AffiliationInfo/Affiliation", "") or ""
            fore_name = author.findtext("ForeName", "") or ""
            last_name = author.findtext("LastName", "") or ""
            name = f"{fore_name} {last_name}".strip()

            if is_non_academic(affiliation):
                if name:
                    authors.append(name)
                companies.append(get_company_name(affiliation))
            if not email:
                email = extract_email(affiliation)

        return {
            "PubmedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": "; ".join(authors) or "N/A",
            "Company Affiliation(s)": "; ".join(companies) or "N/A",
            "Corresponding Author Email": email or "N/A",
        }

    except Exception as e:
        if debug:
            print(f"Error processing PubMed ID {pubmed_id}: {e}")
        return {
            "PubmedID": pubmed_id,
            "Title": "Error",
            "Publication Date": "Error",
            "Non-academic Author(s)": "Error",
            "Company Affiliation(s)": "Error",
            "Corresponding Author Email": "Error",
        }
