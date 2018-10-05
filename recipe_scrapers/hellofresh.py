from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class HelloFresh(AbstractScraper):

    @classmethod
    def host(self):
        return 'hellofresh.co.uk'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return sum([
            get_minutes(element)
            for element in self.soup.findAll(
                'div',
                {'class': 'fela-1anpune'})
        ])

    def ingredients(self):
        ingredients = self.soup.findAll(
            'div',
            {'class': 'fela-xkmok4'}
        )

        result = []

        for ingredient in ingredients:
            result.append(' '.join(
                ingredient_part.get_text()
                for ingredient_part in ingredient.findAll('p')
            ).strip())

        return result

    def instructions(self):
        instructions = self.soup.findAll(
            'div',
            {'class': 'fela-1qsq4x8'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
