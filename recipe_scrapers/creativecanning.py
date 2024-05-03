# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class CreativeCanning(AbstractScraper):
    @classmethod
    def host(cls):
        return "practicalselfreliance.com"
