from ._abstract import AbstractScraper


class BettyBossi(AbstractScraper):
    """Scrape BettyBossi.ch recipes."""

    @classmethod
    def host(cls):
        return "bettybossi.ch"

    def site_name(self):
        """Self-titled website"""
        return self.author()
