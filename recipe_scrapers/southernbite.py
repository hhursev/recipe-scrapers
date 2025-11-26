from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients, IngredientGroup
class SouthernBite(AbstractScraper):
    @classmethod
    def host(cls):
        return "southernbite.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def image(self):
        # Schema.org provides multiple image URLs; pick the first
        images = self.schema.data.get("image")
        if isinstance(images, list) and images:
            return images[0]
        if isinstance(images, str):
            return images
        return ""

    def ingredients(self):
        return self.schema.ingredients()
    
    def ingredient_groups(self):
        # Pass the list of ingredient strings and the parsed soup object
        return group_ingredients(
            self.ingredients(),          # list[str]
            self.soup,                   # BeautifulSoup object
            "h4.wprm-recipe-group-name", # selector for group headings
            "li.wprm-recipe-ingredient"  # selector for ingredient items
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()
    
    def yields(self):
        y = self.schema.data.get("recipeYield")
        if isinstance(y, list):
            # Prefer the second entry if available
            return y[1].strip() if len(y) > 1 else y[0].strip()
        if isinstance(y, str):
            return y.strip()
        return ""

    def description(self):
        # Prefer schema.org description if present, else fallback to meta tag
        desc = self.schema.data.get("description")
        if desc:
            return desc.strip()
        meta = self.soup.find("meta", attrs={"name": "description"})
        return meta["content"].strip() if meta and meta.get("content") else ""
