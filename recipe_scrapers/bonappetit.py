from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class BonAppetit(AbstractScraper):

    @classmethod
    def host(self):
        return 'bonappetit.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find('span', {'itemprop': 'totalTime'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('span', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('div', {'class': 'prep-steps'}).findAll('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
