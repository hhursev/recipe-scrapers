from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class Cucchiaio(AbstractScraper):

    @classmethod
    def host(self):
        return 'cucchiaio.it'

    def title(self):
        return self.soup.find('h1').get_text().strip()

    def total_time(self):
        possible_time_info_elements = self.soup.findAll(
            'span',
            {'class': 'scheda-def'}
        )

        return sum([
            get_minutes(element)
            for element in possible_time_info_elements
        ])

    # def yields(self):
    #     possible_yields_info_elements = self.soup.findAll(
    #         'span',
    #         {'class': 'gz-name-featured-data'}
    #     )
    #     for element in possible_yields_info_elements:
    #         if 'persone' in element.get_text():
    #             return get_yields(element)
    #     return ""

    def ingredients(self):
        ingredients = self.soup.find('ul', {'class': 'ingredients-list'}).findAll(
            'li'
        )

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):

        instructions = self.soup.findAll(
            'div',
            {'class': 'recipe_procedures'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

    # def ratings(self):
    #     """
    #     The average rating is expressed in yellow stars icons
    #     or
    #     in the ld+json script
    #
    #     :return:
    #     """
    #     return sum(float(
    #         self.soup.find(
    #             'div',
    #             {'class': 'voto-box'}
    #         ).get('data-content-rate').replace(',', '.')
    #     ), 2)

    def steps(self):
        """
        Text and Image of the instructions steps

        Try to fetch it from an hypothetical step structure
        based on cucchiaio.it
        :return array of steps: [{"texts": [], "images": []}]
        """
        steps = []
        steps_containers = self.soup.findAll('div', {'class': 'recipe_procedures'})
        for step_elem in steps_containers:
            step = {"texts": [], "images": []}
            texts = step_elem.findAll('p')
            step["texts"] = texts
            images = step_elem.findAll(
                'img',
                {'src': True}
            )
            step["images"] = images
            steps.append(step)
        return steps
