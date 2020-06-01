from ._abstract import AbstractScraper


class MyRecipes(AbstractScraper):
    
    @classmethod
    def host(self):
        return 'myrecipes.com'
        