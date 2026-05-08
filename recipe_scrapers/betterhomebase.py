from ._site_recipe_fallback import SiteRecipeFallbackScraper


class BetterHomebase(SiteRecipeFallbackScraper):
    _site_name = "Better Homebase"

    @classmethod
    def host(cls):
        return "betterhomebase.com"
