from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string
import json


class GialloZafferano(AbstractScraper):

    @classmethod
    def host(self):
        return 'ricette.giallozafferano.it'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find('li', {'class': 'preptime'})) +\
            get_minutes(self.soup.find('li', {'class': 'cooktime'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('dd', {'class': "ingredient"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_json = json.loads(
            self.soup.find('script', {
                'type': 'application/ld+json'}).text).get('recipeInstructions')

        return '\n'.join([
            normalize_string(instruction)
            for instruction in instructions_json
        ])
