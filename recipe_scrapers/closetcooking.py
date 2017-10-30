from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class ClosetCooking(AbstractScraper):

    @classmethod
    def host(self):
        return 'closetcooking.com'

    def title(self):
        return normalize_string(self.soup.find('h2', {'class': 'post-title'}).get_text())

    def total_time(self):
        return get_minutes(self.soup.find(itemprop='totalTime').next_sibling)

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('li', {'itemprop': 'recipeInstructions'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
