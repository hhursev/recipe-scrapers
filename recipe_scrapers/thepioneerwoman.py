from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class ThePioneerWoman(AbstractScraper):

    @classmethod
    def host(self):
        return 'thepioneerwoman.com'

    def title(self):
        return self.soup.find('h3', {'class': 'recipe-title'}).get_text()

    def total_time(self):
        return sum([
            get_minutes(dd)
            for dd in self.soup.find('div', {'class': 'recipe-summary-time'}).findAll('dd')
        ])

    def ingredients(self):
        ingredients_html = self.soup.find('ul', {'class': "list-ingredients"}).findAll('li')

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('div', {'class': 'panel-body'})[-1]

        return normalize_string(instructions_html.get_text()).replace('.', '.\n')
