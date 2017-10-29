from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TwoPeasAndTheirPod(AbstractScraper):

    @classmethod
    def host(self):
        return 'twopeasandtheirpod.com'

    def title(self):
        return self.soup.find('h2', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return get_minutes(self.soup.find('meta', {'itemprop':
            'totalTime'}).parent)

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop':
            'ingredients'})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('div', {'class': 'instructions'}).findAll(['p', 'li'])

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
