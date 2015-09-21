from ._abstract import AbstractScraper

from ._consts import TIME_REGEX
from ._utils import normalize_string


class BBCFood(AbstractScraper):

    @classmethod
    def host(self):
        return 'bbc.co.uk'

    def publisher_site(self):
        return 'http://bbc.co.uk/'

    def title(self):
        return self.soup.find('div', {'class': 'article-title'}).find('h1').get_text()

    def prep_time(self):
        try:
            time = self.soup.find('span', {'class': 'prepTime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span or no time regex match
            return 0

    def cook_time(self):
        try:
            time = self.soup.find('span', {'class': 'cookTime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span or no time regex match
            return 0

    def total_time(self):
        return self.prep_time() + self.cook_time()

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
