from ._site_recipe_fallback import SiteRecipeFallbackScraper


class OliveTomato(SiteRecipeFallbackScraper):
    _site_name = "Olive Tomato"

    @classmethod
    def host(cls):
        return "olivetomato.com"
