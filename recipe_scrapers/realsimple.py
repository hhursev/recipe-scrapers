from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class RealSimple(AbstractScraper):

    @classmethod
    def host(self):
        return 'realsimple.com'

    def title(self):
        return self.soup.find('h1').get_text(strip=True)

    def total_time(self):
        return get_minutes(self.soup.findAll('div', {'class': 'recipe-meta-item'})[1])

    def ingredients(self):
        ingredients_html = self.soup.find('div', {'class':
            "ingredients"}).findAll('li')

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('div', {'class':
            'step'})

        return '\n'.join([
            normalize_string(instruction.find('p').get_text())
            for instruction in instructions_html
        ])
