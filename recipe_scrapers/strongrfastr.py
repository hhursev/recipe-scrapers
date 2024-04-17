# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class StrongrFastr(AbstractScraper):
    @classmethod
    def host(cls):
        return "strongrfastr.com"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def site_name(self):
        return "Strongr Fastr"
