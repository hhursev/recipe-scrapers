from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class AllRecipesBr(AbstractScraper):
    """
    AlLRecipes Brazillian version
    """

    @classmethod
    def host(self):
        return 'allrecipes.com.br'

    def title(self):
        return normalize_string(self.soup.find('h1').get_text())

    def total_time(self):
        return get_minutes(
            self.soup.find('div', {'class': 'stat1'})
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'span',
            {'itemprop': 'ingredients'}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def yields(self):
        return 0

    def instructions(self):
        instructions = self.soup.find(
            'ol', {'itemprop': 'recipeInstructions'}
        ).findAll('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
