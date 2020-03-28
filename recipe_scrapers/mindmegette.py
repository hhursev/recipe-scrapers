from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string
import json


class Mindmegette(AbstractScraper):

    @classmethod
    def host(self):
        return 'mindmegette.hu'

    def title(self):
        return self.soup.find('h1', {'class': 'title'}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find('span', {'class': 'time'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredient"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions = self.soup.find('ul', {'itemprop': 'instructions'}).findAll('li')
        # instructions_json = json.loads(self.soup.findAll('ul', {'itemprop': 'instructions'}).text)

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
