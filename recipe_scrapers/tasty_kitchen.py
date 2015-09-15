from ._abstract import AbstractScraper

from .consts import TIME_REGEX, HTML_SYMBOLS


class TastyKitchen(AbstractScraper):

    @classmethod
    def host(self):
        return 'tastykitchen.com/'

    def publisher_site(self):
        return 'http://tastykitchen.com/'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def total_time(self):
        prep_time = self.soup.find('time', {'itemprop': 'prepTime'}).get_text()
        cook_time = self.soup.find('time', {'itemprop': 'cookTime'}).get_text()

        prep_matched = TIME_REGEX.search(prep_time)
        cook_matched = TIME_REGEX.search(cook_time)
        total_minutes = 0

        if prep_matched is not None and prep_matched.group('hours') is not None:
            total_minutes += 60 * int(prep_matched.group('hours'))

        if cook_matched is not None and cook_matched.group('hours') is not None:
            total_minutes += 60 * int(cook_matched.group('hours'))

        if prep_matched is not None and prep_matched.group('minutes') is not None:
            total_minutes += int(prep_matched.group('minutes'))

        if cook_matched is not None and cook_matched.group('minutes') is not None:
            total_minutes += int(cook_matched.group('minutes'))

        return total_minutes

    def ingredients(self):
        ingredients_html = self.soup.find('ul', {'class': "ingredients"}).findAll('li')
        return [
            ingredient.get_text(strip=True).replace(HTML_SYMBOLS, ' ')
            for ingredient in ingredients_html
        ]

    def instructions(self):
        directions_html = self.soup.find('span', {'itemprop': 'instructions'})
        return directions_html.get_text()
