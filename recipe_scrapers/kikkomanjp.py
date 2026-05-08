from ._site_recipe_fallback import SiteRecipeFallbackScraper


class KikkomanJP(SiteRecipeFallbackScraper):
    _site_name = "Kikkoman"

    @classmethod
    def host(cls):
        return "kikkoman.co.jp"
