from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class ACoupleCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return 'acouplecooks.com'

    def title(self):
        return self.soup.find(
            'h2',
            {'class': 'tasty-recipes-title'}
        ).get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span',
            {'class': 'tasty-recipes-cook-time'})
        )

    def yields(self):
        return get_yields(self.soup.find(
            'span',
            {'class': 'tasty-recipes-yield'}).span
        )

    def ingredients(self):
        return [
            normalize_string(child.text)
            for child in self.soup.find(
                'div',
                {'class': 'tasty-recipes-ingredients'}
            ).ul.children
        ]

    def instructions(self):
        return "\n".join([
            instruction.text for instruction in
            self.soup.find(
                'div',
                {'class': 'tasty-recipes-instructions'}
            ).ol.children
        ])
