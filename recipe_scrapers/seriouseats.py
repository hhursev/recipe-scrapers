from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class SeriousEats(AbstractScraper):

    @classmethod
    def host(self):
        return 'seriouseats.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.findAll(
            'span',
            {'class': 'info'}
        )[2])

    def yields(self):
        return get_yields(self.soup.find(
            'span',
            {
                'class': 'info yield'
            }))

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "ingredient"}
        )
        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'li',
            {'class': 'recipe-procedure'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

    def ratings(self):
        rating = self.soup.find("meta", {"property": "og:rating"})
        rating = round(float(rating['content']), 2) if rating and rating['content'] else -1.0
        return rating
