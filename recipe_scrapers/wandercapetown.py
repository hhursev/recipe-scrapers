from ._site_recipe_fallback import SiteRecipeFallbackScraper


class WanderCapeTown(SiteRecipeFallbackScraper):
    _site_name = "Wander Cape Town"

    @classmethod
    def host(cls):
        return "wandercapetown.com"
