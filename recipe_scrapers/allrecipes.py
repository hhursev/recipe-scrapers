from ._abstract import AbstractScraper


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'
