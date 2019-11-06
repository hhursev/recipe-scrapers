from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class PaniniHappy(AbstractScraper):

    @classmethod
    def host(self):
        return 'paninihappy.com'

    def title(self):
        return self.soup.find(
            'h1',
            {'class': 'entry-title'}
        ).get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span',
            {'class': 'duration'})
        )

    def yields(self):
        return get_yields(self.soup.find(
            'span',
            {'class': 'yield'})
        )

    def image(self):
        image = self.soup.find(
            'img',
            {'class': 'post_image', 'src': True}
        )
        return image['src'] if image else None

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
            {'class': 'instruction'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
