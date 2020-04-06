# delish.py
# Written by J. Kwon
# Freely released the code to recipe_scraper group
# March 1st, 2020
# ==========================================================
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields

class Delish(AbstractScraper):

    @classmethod
    def host(self):
        return 'delish.com'

    def title(self):
        return normalize_string(self.soup.find('h1').get_text())

    # Return total time to complete dish in minutes (includes prep time)
    def total_time(self):
        total_time_class = self.soup.find(
            'span',
            {'class': 'total-time-amount'}
        )
        return get_minutes(total_time_class)

    def yields(self):
        yields_class = self.soup.find(
            'span',
            {'class': 'yields-amount'}
        )

        return get_yields(yields_class)

    def image(self):
        try:
            # Case when image is at the top of the recipe content div
            image = self.soup.find(
                'div',
                {'class': "content-lede-image-wrap aspect-ratio-1x1"}
            ).find(
                'img'
            )
            return image['data-src'] if image else None

        except Exception:
            # If the image is not at the top, it will be found at the
            # bottom of the recipe content div
            image = self.soup.find(
                'picture'
            )
            return image.find('source')['data-srcset'] if image else None

    def ingredients(self):
        ingredients = self.soup.findAll(
            'div',
            {'class': 'ingredient-item'}
        )
        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            'ol'
        ).findAll(
            'li'
        )
        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
