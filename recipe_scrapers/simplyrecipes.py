from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class SimplyRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'simplyrecipes.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return sum([
            get_minutes(self.soup.find(
                'span',
                {'class': 'preptime'})
            ),

            get_minutes(self.soup.find(
                'span',
                {'class': 'cooktime'})
            )
        ])

    def yields(self):
        return get_yields(self.soup.find(
            'span',
            {'class': 'yield'})
        )

    def ingredients(self):
        ingredients = self.soup.find(
            'div',
            {'class': 'recipe-ingredients'}
        ).findAll('li')

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions_html = self.soup.find(
            'div',
            {'class': 'instructions'}
        ).findAll('p')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
