from ._abstract import AbstractScraper
from ._utils import normalize_string, get_minutes


class TheHappyFoodie(AbstractScraper):
    @classmethod
    def host(self):
        return 'thehappyfoodie.co.uk'

    def title(self):
        return self.soup.find('h1', {'class': 'main-title'}).get_text()

    def total_time(self):
        total_time = self.soup.find(
            'div', {'class': 'recipe__data__total-time'}
        )

        if total_time is not None:
            return get_minutes(total_time)
        else:
            times = []
            for name in ('prep', 'cook'):
                time = self.soup.find(
                    'div', {'class': 'recipe__data__{name}-time'.format(name)}
                )
                times.append(get_minutes(time))
            return sum(times)

    def ingredients(self):
        ingredients = self.soup.find(
            'table', {'class': 'recipe__ingredients-table'}
        ).findAll('tr')

        ingredients = [
            (
                ingredient.find(
                    'td', {'class': 'recipe__ingredients__amount'}
                ).get_text(),
                ingredient.find(
                    'td', {'class': 'recipe__ingredients__name'}
                ).get_text(),
            )
            for ingredient in ingredients
        ]

        return [
            normalize_string(f'{amount} {name}') for amount, name in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find(
            'div', {'class': 'recipe__instructions'}
        ).findAll('p')

        return '\n'.join(
            normalize_string(instruction.get_text())
            for instruction in instructions
        )
