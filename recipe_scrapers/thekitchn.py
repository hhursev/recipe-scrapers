from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class TheKitchn(AbstractScraper):

    @classmethod
    def host(self):
        return 'thekitchn.com'

    def title(self):
        return self.soup.find(
            'h2',
            {'class': 'Recipe__title'}
        ).get_text()

    def total_time(self):
        elements = self.soup.findAll(
            'p',
            {'class': 'Recipe__time-label'}
        )
        return sum([get_minutes(element) for element in elements])

    def yields(self):
        return get_yields(
            self.soup.find(
                'span',
                {'class': 'Recipe__yield-entry'}
            )
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': 'Recipe__ingredient'}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'li',
            {'class': 'Recipe__instruction-step'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
