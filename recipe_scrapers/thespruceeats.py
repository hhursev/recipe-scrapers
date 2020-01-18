import json
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class TheSpruceEats(AbstractScraper):

    @classmethod
    def host(self):
        return 'thespruceeats.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'li',
            {'class': 'total-time'}
        ).get_text())

    def yields(self):
        return get_yields(json.loads(
            self.soup.find(
                'script',
                {'type': 'application/ld+json'}
            ).get_text()
        ).get('mainEntity').get('recipeYield'))

    def ingredients(self):
        ingredients = self.soup.find(
            'ul',
            {'class': "ingredient-list"}
        ).find_all(
            'li',
            {'class': 'simple-list__item'}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            'section',
            {'class': 'section--instructions'}
        ).find_all('li')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

    def ratings(self):
        return round(float(json.loads(
            self.soup.find(
                'script',
                {'type': 'application/ld+json'}
            ).get_text()
        ).get('mainEntity').get('aggregateRating').get('ratingValue')), 2)
