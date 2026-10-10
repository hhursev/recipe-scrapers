# Supported Websites

!!! success "Join Our Community"
    🌟 Want to add your favorite recipe site? We'd love your help!

    - 📖 Check our [contributing guidelines](../contributing/home.md)
    - 🐛 Found a bug? [Open an issue](https://github.com/hhursev/recipe-scrapers/issues)
    - 🚀 Ready to contribute? [Submit a pull request](../contributing/setup.md)!

```python exec="on"
import sys
sys.path.insert(0, '.')
from recipe_scrapers import SCRAPERS

sites = sorted(SCRAPERS.keys())

print(f"## What we offer?")
print(f"We currently support over **{len(sites)} popular recipe websites** out of the box! And with our `wild_mode` option, you can potentially scrape many more sites that follow common patterns - making this probably the most extensive recipe scraping library available.\n")
print(f"## Supported Sites List\n")
print("\n".join(f"- [{host}](https://{host}/)" for host in sites))
```

!!! note "Recipe images on budapestcookingclass.com"
    This site's page-wide image metadata can include unrelated cooking-class photos.
    Its scraper defaults to the recipe's Schema.org image, even when higher-quality
    image selection is enabled globally. Pass `best_image=True` to `scrape_html` to
    opt into page-wide image selection for this site.
