from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class BBCGoodFood(AbstractScraper):

    @classmethod
    def host(self):
        return 'bbcgoodfood.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return sum([
            get_minutes(self.soup.find(
                'span',
                {'class': 'recipe-details__cooking-time-prep'}
            ).find('span')),

            get_minutes(self.soup.find(
                'span',
                {'class': 'recipe-details__cooking-time-cook'}
            ).find('span'))
        ])

    def ingredients(self):
        ingredients = self.soup.find(
            'section',
            {'id': "recipe-ingredients"}
        ).findAll('li')

        return [
            normalize_string(
                '{normal_text}{tooltip_text}'.format(
                    normal_text=ingredient.find(text=True),
                    tooltip_text=ingredient.find('a').get_text() if ingredient.find('a') is not None else ''
                )
            )
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            'section',
            {'id': 'recipe-method'}
        ).findAll('li')

        instructions_string = '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

        instructions_string += '\n' + normalize_string(
            self.soup.find(
                'section',
                {'id': 'recipe-method'}
            ).get_text()
        )

        return normalize_string(instructions_string)
