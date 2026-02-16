from pathlib import Path
from recipe_scrapers import scrape_html
import json
import sys
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
            print("Usage: python populate_json_by_scraper.py <scraper test folder name>")
            sys.exit(1)

    folder_name = str(sys.argv[1])
    class_name = folder_name.rsplit(".", 1)[0]
    parent_path = Path('../tests').parent.resolve()
    test_path = Path(f"{parent_path}/tests/test_data/{folder_name}")

    print(f"Populating .temp.json files for scraper: {class_name}...")
    print(f"Looking for HTML files in {test_path}...")    
    
    for f in test_path.glob("*.testhtml"): 
        print(f"Processing {f}...")

        html = Path(f"{parent_path}/tests/test_data/{folder_name}/{f.name}").read_text(encoding="utf-8")
        soup = BeautifulSoup(html, "html.parser")
        url = soup.find("meta", property="og:url").get("content")

        print(f"Scraping {url}...")
        scraper = scrape_html(html, url)
        with open(f"{parent_path}/tests/test_data/{folder_name}/{f.stem}.temp.json", "w+", encoding="utf-8") as f:
            json.dump(scraper.to_json(), f, indent=2, ensure_ascii=False)
        
        print(f"Completed processing {url}")

if __name__ == "__main__":
    main()