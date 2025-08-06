from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException, StaticValueException
from ._utils import normalize_string


class Rezeptwelt(AbstractScraper):
    @classmethod
    def host(cls):
        return "rezeptwelt.de"

    def site_name(self):
        raise StaticValueException(return_value="Rezeptwelt")

    def author(self):
        return normalize_string(self.soup.find("span", {"id": "viewRecipeAuthor"}).text)

    def instructions(self):
        container = self.soup.find("div", id="preparationSteps").find(
            "span", itemprop="text"
        )
        instructions = [
            normalize_string(paragraph.text) for paragraph in container.find_all("p")
        ]
        return "\n".join(filter(None, instructions))

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
