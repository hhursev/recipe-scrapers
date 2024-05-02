# mypy: disallow_untyped_defs=False

from ._abstract import AbstractScraper


class BettyBossi(AbstractScraper):
    """Scrape BettyBossi.ch recipes."""

    @classmethod
    def host(cls):
        return "bettybossi.ch"
