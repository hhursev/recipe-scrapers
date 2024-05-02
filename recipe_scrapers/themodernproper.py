# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class TheModernProper(AbstractScraper):
    @classmethod
    def host(cls):
        return "themodernproper.com"
