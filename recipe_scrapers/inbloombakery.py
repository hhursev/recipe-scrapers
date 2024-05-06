# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class InBloomBakery(AbstractScraper):
    @classmethod
    def host(cls):
        return "inbloombakery.com"
