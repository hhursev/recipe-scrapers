from urllib.request import urlopen
from recipe_scrapers import scrape_html

url = "https://www.xiachufang.com/recipe/100403615"
html = urlopen(url).read().decode("utf-8")  # retrieves the recipe webpage HTML
scraper = scrape_html(html, org_url=url)

# Extract recipe information
scraper.title()
scraper.instructions()
scraper.links()
scraper.to_json()
scraper.nutrients()

# To see all available methods
help(scraper)
