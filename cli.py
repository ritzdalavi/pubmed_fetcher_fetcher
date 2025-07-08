import argparse
import csv
from pubmed_fetcher.fetcher import fetch_pubmed_ids, fetch_paper_details

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers by query")
    parser.add_argument("query", help="Search query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logs")
    parser.add_argument("-f", "--file", help="Filename to save results (CSV)")

    args = parser.parse_args()
    ids = fetch_pubmed_ids(args.query, args.debug)
    results = [fetch_paper_details(i, args.debug) for i in ids]

    if args.file:
        with open(args.file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
        if args.debug: print(f"Saved results to {args.file}")
    else:
        for r in results:
            print(r)
