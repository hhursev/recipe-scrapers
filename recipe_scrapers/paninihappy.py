from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class PaniniHappy(AbstractScraper):

    @classmethod
    def host(self):
        return 'paninihappy.com'

    def title(self):
        return self.soup.find(
            'h1',
            {'class': 'entry-title'}
        ).get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span',
            {'class': 'duration'})
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "ingredient"}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'li',
            {'class': 'instruction'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
