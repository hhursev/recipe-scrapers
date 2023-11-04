# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException
from ._utils import normalize_string


class Rezeptwelt(AbstractScraper):
    @classmethod
    def host(cls):
        return "rezeptwelt.de"

    def author(self):
        return normalize_string(self.soup.find("span", {"id": "viewRecipeAuthor"}).text)

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        container = self.soup.find("div", id="preparationSteps").find(
            "span", itemprop="text"
        )
        instructions = [
            normalize_string(paragraph.text) for paragraph in container.find_all("p")
        ]
        return "\n".join(filter(None, instructions))

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        try:
            return self.schema.cuisine()
        except SchemaOrgException:
            return None

    def description(self):
        return self.schema.description().replace(
            " Mehr Thermomix ® Rezepte auf www.rezeptwelt.de", ""
        )

    def language(self):
        return self.soup.find("meta", {"property": "og:locale"})["content"]
