from ._abstract import AbstractScraper
from ._utils import normalize_string, get_minutes


class NIHHealthyEating(AbstractScraper):

    @classmethod
    def host(self):
        return 'healthyeating.nhlbi.nih.gov'

    def title(self):
        return self.soup.h1.get_text().strip()

    def total_time(self):
        time_table = self.soup.find(
            'table',
            {'class': 'recipe_time_table'}
        )

        return sum([
            get_minutes(td)
            for td in time_table.find_all('td')
        ])

    def ingredients(self):
        ingredients = self.soup.find(
            'div',
            {'id': "ingredients"}
        ).findAll('p')

        return [
            normalize_string(paragraph.get_text())
            for paragraph in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            'div',
            {'id': "recipe_directions"}
        ).findAll(
            'div',
            {'class': 'steptext'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])
