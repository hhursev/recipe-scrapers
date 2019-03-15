from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class Yummly(AbstractScraper):

    @classmethod
    def host(self):
        return 'yummly.com'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        return get_minutes(
            self.soup.find('div', {'class': 'recipe-summary-item unit'})
        )

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'class': "IngredientLine"}
        )

        return [
            ' '.join([
                normalize_string(span.get_text())
                for span in ingredient.select("""
                    span[class^=amount],
                    span[class^=unit],
                    span[class^=ingredient]""")
            ])
            for ingredient in ingredients
        ]

    def instructions(self):
        """
        Yummly does not provide instructions on it's page.
        It has a link that redirects to original website.
        """
        return ''
