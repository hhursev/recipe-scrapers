from ._site_recipe_fallback import SiteRecipeFallbackScraper


class Dancyu(SiteRecipeFallbackScraper):
    _site_name = "Dancyu"

    @classmethod
    def host(cls):
        return "dancyu.jp"
