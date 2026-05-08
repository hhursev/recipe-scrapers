from ._site_recipe_fallback import SiteRecipeFallbackScraper


class TheAge(SiteRecipeFallbackScraper):
    _site_name = "The Age"

    @classmethod
    def host(cls):
        return "edition.theage.com.au"
