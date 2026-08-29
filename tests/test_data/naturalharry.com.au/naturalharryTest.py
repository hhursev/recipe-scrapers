import os

from recipe_scrapers import scrape_html

# Define the path to your test HTML file
test_html_path = os.path.join(
    "tests", "test_data", "naturalharry.com", "naturalharry.testhtml"
)

# Read the test HTML content
with open(test_html_path, "rb") as file:
    html_content = file.read()

# The URL used during scraper generation
url = "https://naturalharry.com.au/crispy-cauli-tacos-with-tangy-chipotle-mayo/"

# Create a scraper instance using the test HTML
scraper = scrape_html(html_content.decode("utf-8"), url)

# Print the outputs of scraper methods
print("----- NaturalHarry Scraper Test Output -----\n")
print("Title:", scraper.title())
print("\nAuthor:", scraper.author())
print("\nTotal Time (minutes):", scraper.total_time())
print("\nYields:", scraper.yields())
print("\nIngredients:")
for ingredient in scraper.ingredients():
    print(f" - {ingredient}")
print("\nInstructions:", scraper.instructions())
print("\nImage URL:", scraper.image())
print("\nDescription:", scraper.description())
print("\n----- End of Output -----")
