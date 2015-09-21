from ._abstract import AbstractScraper

from ._consts import TIME_REGEX
from ._utils import normalize_string


class PaniniHappy(AbstractScraper):

    @classmethod
    def host(self):
        return 'paninihappy.com'

    def publisher_site(self):
        return 'http://paninihappy.com/'

    def title(self):
        return self.soup.find('h1', {'class': 'entry-title'}).get_text()

    def total_time(self):
        try:
            time = self.soup.find('span', {'class': 'duration'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span or no time regex match
            return 0

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'class': "ingredient"})

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
