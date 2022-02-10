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
        content = self.soup.find("ol", {"itemprop": "recipeInstructions"}).findAll(
            "div", {"itemprop": "itemListElement"}
        )
        res = ""
        for i in content:
            steps = i.findAll("span", {"itemprop": "text"})
            for step in steps:
                res += normalize_string(step.text) + "\n"
        return res

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
