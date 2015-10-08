from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class Cookstr(AbstractScraper):

    @classmethod
    def host(self):
        return 'cookstr.com'

    def title(self):
        return normalize_string(self.soup.find('h1', {'id': 'recipe_title'}).get_text())

    def total_time(self):
        recipe_info = self.soup.find('ul', {'id': 'recipe-info-attrs'})
        return sum([get_minutes(li) for li in recipe_info.findAll('li')])

    def ingredients(self):
        ingredients_html = self.soup.find('span', {'class': "recipe_structure_ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html.findAll('li')
        ]

    def instructions(self):

        instructions_html = self.soup.find('div', {'class': 'recipe_structure_directions'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html.findAll('p')
        ])
