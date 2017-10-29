from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class BonAppetit(AbstractScraper):

    @classmethod
    def host(self):
        return 'bonappetit.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return 0

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'class': "ingredient"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('div', {'class':
            'steps-wrapper'}).findAll('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
