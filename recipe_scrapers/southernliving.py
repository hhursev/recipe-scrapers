# mypy: disallow_untyped_defs=False

from recipe_scrapers._exceptions import SchemaOrgException

from ._abstract import AbstractScraper
from ._utils import get_yields


class SouthernLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "southernliving.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        try:
            schema_yield = self.schema.yields()
            if schema_yield:
                return schema_yield
        except SchemaOrgException:
            pass

        for servings_div in self.soup.find_all(
            "div", class_="mntl-recipe-details__item"
        ):
            label_text = servings_div.find(
                "div", class_="mntl-recipe-details__label"
            ).get_text(strip=True)
            if label_text in ["Servings:", "Yield:"]:
                servings_element = servings_div.find(
                    "div", class_="mntl-recipe-details__value"
                )
                return get_yields(servings_element)

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def description(self):
        return self.schema.description()
