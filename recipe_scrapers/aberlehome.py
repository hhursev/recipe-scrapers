# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class AberleHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "aberlehome.com"
