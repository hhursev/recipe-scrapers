from ._abstract import AbstractScraper

from ._consts import TIME_REGEX, HTML_SYMBOLS


class SimplyRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'simplyrecipes.com'

    def publisher_site(self):
        return 'http://www.simplyrecipes.com/'

    def title(self):
        return self.soup.find('h1').get_text()

    def prep_time(self):
        try:
            time = self.soup.find('span', {'class': 'preptime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span with class prep-time / cook-time
            return 0

    def cook_time(self):
        try:
            time = self.soup.find('span', {'class': 'cooktime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span with class prep-time / cook-time
            return 0

    def total_time(self):
        return self.prep_time() + self.cook_time()

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'class': "ingredient"})
        return [
            ingredient.get_text(strip=True).replace(HTML_SYMBOLS, ' ')
            for ingredient in ingredients_html
        ]

    def instructions(self):
        instructions_html = self.soup.find('div', {'itemprop': 'recipeInstructions'}).findAll('p')

        return '\n'.join(
            [instruction.get_text() for instruction in instructions_html]
        ).strip()
