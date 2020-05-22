from ._abstract import AbstractScraper
from ._utils import get_yields
from ._decorators import Decorators


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'

    @Decorators.schema_org_priority
    def yields(self):
        return get_yields(self.soup.find(
            'div',
            {'class': 'recipe-adjust-servings__original-serving'}
        ))
