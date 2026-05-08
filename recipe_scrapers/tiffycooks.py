from ._site_recipe_fallback import SiteRecipeFallbackScraper


class TiffyCooks(SiteRecipeFallbackScraper):
    _site_name = "Tiffy Cooks"

    @classmethod
    def host(cls):
        return "tiffycooks.com"
