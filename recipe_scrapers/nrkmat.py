from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException
from ._grouping_utils import group_ingredients


class NRKMat(AbstractScraper):
    @classmethod
    def host(cls):
        return "nrk.no"

    def author(self):
        return (
            self.soup.find("span", {"class": "caption-cite"})
            .getText()
            .replace("Kilde: ", "")
        )

    def yields(self):
        try:
            return self.schema.yields()
        except SchemaOrgException:
            return None

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h4.recipe-meta-title",
            "ul.recipe-list:not(.recipe-list-meta) > li",
        )
