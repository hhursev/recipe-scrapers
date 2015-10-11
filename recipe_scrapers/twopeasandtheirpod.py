from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class TwoPeasAndTheirPod(AbstractScraper):

    @classmethod
    def host(self):
        return 'twopeasandtheirpod.com'

    def title(self):
        return self.soup.find('h2').get_text()

    def total_time(self):
        return get_minutes(self.soup.find('span', {'class': 'cooktime'}))

    def ingredients(self):
        ingredients_html = self.soup.find('div', {'class': 'ingredient'}).findAll('p')
        ingredients_flatten = []
        for ingredient in ingredients_html:
            ingredients_flatten.extend(ingredient.get_text().split('\n'))

        return [
            normalize_string(ingredient)
            for ingredient in ingredients_flatten
            if ingredient[0].isdigit()
        ]

    def instructions(self):
        instructions_html = self.soup.find('div', {'class': 'instructions'}).findAll(['p', 'li'])

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
