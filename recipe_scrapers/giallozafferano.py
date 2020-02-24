from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class GialloZafferano(AbstractScraper):

    @classmethod
    def host(self):
        return 'ricette.giallozafferano.it'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        possible_time_info_elements = self.soup.findAll(
            'span',
            {'class': 'gz-name-featured-data'}
        )

        return sum([
            get_minutes(element)
            for element in possible_time_info_elements
        ])

    def yields(self):
        possible_yields_info_elements = self.soup.findAll(
            'span',
            {'class': 'gz-name-featured-data'}
        )
        for element in possible_yields_info_elements:
            if 'persone' in element.get_text():
                return get_yields(element)
        return ""

    def ingredients(self):
        ingredients = self.soup.findAll(
            'dd',
            {'class': "gz-ingredient"}
        )

        if not ingredients:
            ingredients = self.soup.findAll(
                'li',
                {'class': "gz-ingredient"}
            )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):

        instructions = self.soup.findAll(
            'div',
            {'class': 'gz-content-recipe-step'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

    def ratings(self):
        return round(float(
            self.soup.find(
                'div',
                {'class': 'gz-rating-panel rating_panel'}
            ).get('data-content-rate').replace(',', '.')
        ), 2)
