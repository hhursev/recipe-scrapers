from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class KeyToMyLime(AbstractScraper):
    @classmethod
    def host(cls):
        return "keytomylime.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mv-create-ingredients h3",
            ".mv-create-ingredients ul li",
        )
