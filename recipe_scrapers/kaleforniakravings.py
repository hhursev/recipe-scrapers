from ._site_recipe_fallback import SiteRecipeFallbackScraper


class KaleforniaKravings(SiteRecipeFallbackScraper):
    _site_name = "Kalefornia Kravings"

    @classmethod
    def host(cls):
        return "kaleforniakravings.com"
