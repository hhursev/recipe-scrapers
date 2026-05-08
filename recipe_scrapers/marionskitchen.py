from ._site_recipe_fallback import SiteRecipeFallbackScraper


class MarionsKitchen(SiteRecipeFallbackScraper):
    _site_name = "Marion's Kitchen"

    @classmethod
    def host(cls):
        return "marionskitchen.com"
