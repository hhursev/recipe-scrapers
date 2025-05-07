from ._abstract import AbstractScraper


class SteamyKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "steamykitchen.com"

    def ratings(self):
        # Schema has no ratings and I can't see any near the recipe
        return None
