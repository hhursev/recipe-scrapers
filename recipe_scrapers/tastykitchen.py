from ._abstract import AbstractScraper

from ._consts import TIME_REGEX, HTML_SYMBOLS


class TastyKitchen(AbstractScraper):

    @classmethod
    def host(self):
        return 'tastykitchen.com/'

    def publisher_site(self):
        return 'http://tastykitchen.com/'

    def title(self):
        return self.soup.find('h1', {'itemprop': 'name'}).get_text()

    def prep_time(self):
        try:
            time = self.soup.find('time', {'itemprop': 'prepTime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span or no time regex match
            return 0

    def cook_time(self):
        try:
            time = self.soup.find('time', {'itemprop': 'cookTime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span or no time regex match
            return 0

    def total_time(self):
        return self.prep_time() + self.cook_time()

    def ingredients(self):
        ingredients_html = self.soup.find('ul', {'class': "ingredients"}).findAll('li')
        return [
            ingredient.get_text(strip=True).replace(HTML_SYMBOLS, ' ')
            for ingredient in ingredients_html
        ]

    def instructions(self):
        directions_html = self.soup.find('span', {'itemprop': 'instructions'})
        return directions_html.get_text()
