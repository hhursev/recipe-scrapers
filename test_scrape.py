#!/usr/bin/env python3
"""
Test script for scraping a recipe URL and outputting JSON.
Usage: python test_scrape.py <url>
"""

import json
import sys

from recipe_scrapers import scrape_html


def main():
    if len(sys.argv) != 2:
        print("Usage: python test_scrape.py <url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]

    try:
        import requests
    except ImportError:
        print("Error: requests is required. Install with: pip install requests", file=sys.stderr)
        sys.exit(1)

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.0"
            )
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        html = response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        scraper = scrape_html(html, url)
    except Exception as e:
        print(f"Error: could not find a scraper for this site: {e}", file=sys.stderr)
        sys.exit(1)

    data = {
        "title": scraper.title(),
        "total_time": scraper.total_time(),
        "yields": scraper.yields(),
        "ingredients": scraper.ingredients(),
        "instructions": scraper.instructions(),
        "image": scraper.image(),
        "author": scraper.author(),
        "canonical_url": scraper.canonical_url(),
    }

    # Optional fields — not all scrapers implement these
    optional_fields = [
        "cuisine",
        "category",
        "cook_time",
        "prep_time",
        "ratings",
        "ratings_count",
        "description",
        "nutrients",
    ]

    for field in optional_fields:
        try:
            data[field] = getattr(scraper, field)()
        except Exception:
            pass

    print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
