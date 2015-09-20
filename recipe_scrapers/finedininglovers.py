from ._abstract import AbstractScraper

from ._consts import TIME_REGEX


class FineDiningLovers(AbstractScraper):

    @classmethod
    def host(self):
        return 'finedininglovers.com'

    def publisher_site(self):
        return 'https://finedininglovers.com/'

    def title(self):
        return self.soup.find('h3', {'itemprop': 'name'}).get_text()

    def total_time(self):
        try:
            time = self.soup.find('time', {'itemprop': 'prepTime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span or no time regex match
            return 0

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})
        return [
            ingredient.find('a').get_text(strip=True)
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('div', {'itemprop': 'recipeInstructions'})
        return '\n'.join(
            [
                instruction.get_text(strip=True)
                for instruction in instructions_html
            ])
