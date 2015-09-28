from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class JamieOliver(AbstractScraper):

    @classmethod
    def host(self):
        return 'jamieoliver.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find('div', {'class': 'time'}))

    def ingredients(self):
        ul = self.soup.find('ul', {'class', 'ingred-list'})
        ingredients_html = ul.findAll('li')

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('div', {'class': 'instructions-wrapper'})
        return normalize_string(instructions_html.get_text())
