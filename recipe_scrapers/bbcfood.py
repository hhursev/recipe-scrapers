from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class BBCFood(AbstractScraper):

    @classmethod
    def host(self):
        return 'bbc.co.uk'

    def title(self):
        return self.soup.find('div', {'class': 'article-title'}).find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find('span', {'class': 'prepTime'})) +\
               get_minutes(self.soup.find('span', {'class': 'cookTime'}))

    def ingredients(self):
        ingredients_html = self.soup.findAll('p', {'class': "ingredient"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('li', {'class': 'instruction'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
