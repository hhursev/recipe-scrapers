from ._abstract import AbstractScraper

from .consts import TIME_REGEX, HTML_SYMBOLS


class AllRecipes(AbstractScraper):

    @classmethod
    def host(self):
        return 'allrecipes.com'

    def publisher_site(self):
        return 'http://allrecipes.com/'

    def title(self):
        return self.soup.find('h1').get_text()

    def total_time(self):
        try:
            time = self.soup.find('span', {'class': 'ready-in-time'}).get_text()
            matched = TIME_REGEX.search(time)
            if matched is None:
                raise AttributeError

            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)

            return total_minutes
        except AttributeError:  # when there is no span or no time regex match
            return 0

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'class': "checkList__line"})
        return [
            ingredient.get_text(strip=True)
            for ingredient in ingredients_html
            if ingredient.get_text(strip=True) not in ('Add all ingredients to list', '')
        ]

    def instructions(self):
        directions_html = self.soup.findAll('span', {'class': 'recipe-directions__list--item'})
        return '\n\n'.join(
            [
                direction.get_text(strip=True).replace(HTML_SYMBOLS, ' ')
                for direction in directions_html
            ]).strip()
