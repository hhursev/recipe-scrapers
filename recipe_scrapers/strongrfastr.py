# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class StrongrFastr(AbstractScraper):
    @classmethod
    def host(cls):
        return "strongrfastr.com"

    def category(self):
        return self.schema.category()

    def cuisine(self):
        return self.schema.cuisine()

    def site_name(self):
        return "Strongr Fastr"
