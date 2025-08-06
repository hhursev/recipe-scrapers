from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._grouping_utils import group_ingredients


class TheKitchn(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchn.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".Recipe__ingredientsGroupName",
            ".Recipe__ingredient",
        )

    def site_name(self):
        raise StaticValueException(return_value="The Kitchn")
