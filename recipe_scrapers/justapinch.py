from ._site_recipe_fallback import SiteRecipeFallbackScraper


class JustAPinch(SiteRecipeFallbackScraper):
    _site_name = "Just A Pinch"

    @classmethod
    def host(cls):
        return "justapinch.com"
