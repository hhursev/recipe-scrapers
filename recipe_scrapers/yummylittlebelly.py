from ._site_recipe_fallback import SiteRecipeFallbackScraper


class YummyLittleBelly(SiteRecipeFallbackScraper):
    _site_name = "Yummy Little Belly"

    @classmethod
    def host(cls):
        return "yummylittlebelly.com"
