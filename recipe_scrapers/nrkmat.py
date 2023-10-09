# mypy: allow-untyped-defs

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

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def yields(self):
        try:
            return self.schema.yields()
        except SchemaOrgException:
            return None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h4.recipe-meta-title",
            "ul.recipe-list:not(.recipe-list-meta) > li",
        )

    def instructions(self):
        return self.schema.instructions()

    def description(self):
        return self.schema.description()
