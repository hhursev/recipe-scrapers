from ._site_recipe_fallback import SiteRecipeFallbackScraper


class ImbibeMagazine(SiteRecipeFallbackScraper):
    _site_name = "Imbibe Magazine"

    @classmethod
    def host(cls):
        return "imbibemagazine.com"
