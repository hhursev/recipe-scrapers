from ._abstract import AbstractScraper
from ._utils import normalize_string


class Epicurious(AbstractScraper):

    @classmethod
    def host(self):
        return 'epicurious.com'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        return 0

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('li', {'class':
            'preparation-step'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])

    def rating(self):
        return float(self.soup.find('span',
                     {'class': 'rating'})
                     .get_text().split('/')[0]) / 4

    def reviews(self):
        reviews = self.soup.findAll('div', {'class': "review-text"})
        reviews = [rev.get_text() for rev in reviews]
        return reviews
