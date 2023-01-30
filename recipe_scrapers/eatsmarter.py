# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException


class Eatsmarter(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"eatsmarter.{domain}"

    def title(self):
        return self.schema.title()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        try:
            return self.schema.cook_time()
        except SchemaOrgException:
            return None

    def prep_time(self):
        try:
            return self.schema.prep_time()
        except SchemaOrgException:
            return None
