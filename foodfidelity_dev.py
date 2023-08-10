from recipe_scrapers import scrape_me

# Initialize the scraper
scraper = scrape_me("https://www.foodfidelity.com/citrus-israeli-couscous/")

methods = [
    "title",
    "instructions",
    "host",
    "total_time",
    "image",
    "ingredients",
    "yields",
    "ratings",
    "cuisine",
    "description",
    "author",
    "ingredient_groups",
]

for method in methods:
    try:
        result = getattr(scraper, method)()
        print(f"{method.capitalize()}: {result}")
    except Exception as e:
        print(f"Error while getting {method}: {e}")
