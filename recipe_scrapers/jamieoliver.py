from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class JamieOliver(AbstractScraper):

    @classmethod
    def host(self):
        return 'jamieoliver.com'

    def publisher_site(self):
        return 'http://jamieoliver.com/'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return sum([get_minutes(td) for td in self.soup.findAll('td', {'valign': 'top'})])

    def ingredients(self):
        article = self.soup.find('article', {'class', 'ingredients'})
        ingredients_html = article.findAll('li')

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('p', {'class': 'instructions'})
        return normalize_string(instructions_html.get_text())
