# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class StrongrFastr(AbstractScraper):
    @classmethod
    def host(cls):
        return "strongrfastr.com"


    def description(self):
        return self.schema.description()

    def site_name(self):
        return "Strongr Fastr"
