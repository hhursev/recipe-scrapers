from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class FoodRepublic(AbstractScraper):

    @classmethod
    def host(self):
        return 'foodrepublic.com'

    def title(self):
        return self.soup.find('h3', {'class': 'recipe-title'}).get_text()

    def total_time(self):
        return sum([
            get_minutes(self.soup.find(
                'li',
                {'class': 'prep-time'})
            ),

            get_minutes(self.soup.find(
                'li',
                {'class': 'cook-time'})
            )
        ])

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'itemprop': "recipeIngredient"}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            'div',
            {'class': 'directions'}
        ).findAll('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
