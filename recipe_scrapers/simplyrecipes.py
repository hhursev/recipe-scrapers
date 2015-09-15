from functools import reduce

from ._abstract import AbstractScraper

from .consts import TIME_REGEX, HTML_SYMBOLS


class SimplyRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'simplyrecipes.com'

    def publisher_site(self):
        return 'http://www.simplyrecipes.com/'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        try:
            prep_time = self.soup.find('span', {'class': 'preptime'}).get_text()
            cook_time = self.soup.find('span', {'class': 'cooktime'}).get_text()
            matched_preptime = TIME_REGEX.search(prep_time)
            matched_cooktime = TIME_REGEX.search(cook_time)
        except AttributeError:  # when there is no span with class prep-time / cook-time
            return 0

        total_minutes = 0

        if matched_preptime is not None and matched_preptime.group('hours') is not None:
            total_minutes += 60 * int(matched_preptime.group('hours'))
        if matched_cooktime is not None and matched_cooktime.group('hours') is not None:
            total_minutes += 60 * int(matched_cooktime.group('hours'))
        if matched_preptime is not None and matched_preptime.group('minutes') is not None:
            total_minutes += int(matched_preptime.group('minutes'))
        if matched_cooktime is not None and matched_cooktime.group('minutes') is not None:
            total_minutes += int(matched_cooktime.group('minutes'))

        return total_minutes

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

    def social_rating(self):
        # if shared more than 1k 100 social rating, otherwise shares / 10 percentage rating
        shares_count = [
            shares.get_text() for shares in
            self.soup.findAll('span', {'class': 'share-button-counter'})
        ]

        if any(['k' in share_count for share_count in shares_count]):
            return 100

        shares_count = reduce(lambda x, y: int(x) + int(y), shares_count, 0)
        if shares_count / 10 > 100:
            return 100

        return int(shares_count / 10)
