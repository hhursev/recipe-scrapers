from ._site_recipe_fallback import SiteRecipeFallbackScraper


class Instructables(SiteRecipeFallbackScraper):
    _site_name = "Instructables"

    @classmethod
    def host(cls):
        return "instructables.com"
