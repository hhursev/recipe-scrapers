from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TudoGostoso(AbstractScraper):

    @classmethod
    def host(self):
        return 'tudogostoso.com.br'

    def title(self):
        return normalize_string(self.soup.find('h1').get_text())

    def total_time(self):
        return get_minutes(
            self.soup.find('time', {'itemprop': 'totalTime'})
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'span',
            {'class': "p-ingredient"}
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            'div',
            {'class': 'instructions'}
        ).find_all('span')

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
