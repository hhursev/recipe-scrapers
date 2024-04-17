# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class StrongrFastr(AbstractScraper):
    @classmethod
    def host(cls):
        return "strongrfastr.com"

    def category(self):
        return self.schema.category()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def site_name(self):
        return "Strongr Fastr"
