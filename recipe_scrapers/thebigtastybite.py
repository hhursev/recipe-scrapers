from ._site_recipe_fallback import SiteRecipeFallbackScraper


class TheBigTastyBite(SiteRecipeFallbackScraper):
    _site_name = "The Big Tasty Bite"

    @classmethod
    def host(cls):
        return "thebigtastybite.com"
