from recipe_scrapers import scrape_me

# Initialize the scraper
scraper = scrape_me(
    "https://thekitchencommunity.org/sauces-that-go-with-philly-cheesesteak/"
)

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
]

for method in methods:
    try:
        result = getattr(scraper, method)()
        print(f"{method.capitalize()}: {result}")
    except Exception as e:
        print(f"Error while getting {method}: {e}")
