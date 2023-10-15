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
        return self.soup.find("meta", {"property": "og:title"})["content"]

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
        preparation_div = self.soup.find("div", id="preparationSteps")
        instructions = preparation_div.find("span", itemprop="text").find_all("p")
        instruction_texts = [instruction.get_text() for instruction in instructions]
        normalized_texts = [normalize_string(text) for text in instruction_texts]
        joined_instructions = "\n".join(filter(None, normalized_texts))
        return joined_instructions

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
