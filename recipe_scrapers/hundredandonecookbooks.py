from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class HundredAndOneCookbooks(AbstractScraper):

    @classmethod
    def host(self):
        return '101cookbooks.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(self.soup.find(
            'span',
            {'class': 'preptime'})
        )

    def ingredients(self):
        ingredients = self.soup.find(
            'div',
            {'id': 'recipe'}
        ).find('blockquote').find('p')
        return ingredients.get_text().split('\n')

    def instructions(self):
        instructions = self.soup.find(
            'div',
            {'id': 'recipe'}
        ).find('blockquote').find_next_siblings()

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
