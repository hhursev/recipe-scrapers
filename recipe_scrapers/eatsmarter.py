from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException


class Eatsmarter(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"eatsmarter.{domain}"

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
