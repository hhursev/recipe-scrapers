from ._abstract import AbstractScraper

# from ._consts import TIME_REGEX
from ._utils import normalize_string


class BonAppetit(AbstractScraper):

    @classmethod
    def host(self):
        return 'bonappetit.com'

    def publisher_site(self):
        return 'http://bonappetit.com/'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return 0

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
