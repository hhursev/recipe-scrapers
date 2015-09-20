from ._abstract import AbstractScraper

from ._consts import TIME_REGEX


class SteamyKitchen(AbstractScraper):

    @classmethod
    def host(self):
        return 'steamykitchen.com'

    def publisher_site(self):
        return 'http://steamykitchen.com/'

    def title(self):
        return self.soup.find('span', {'itemprop': 'name'}).get_text()

    def prep_time(self):
        try:
            time = self.soup.find('meta', {'itemprop': 'prepTime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span with class prep-time / cook-time
            return 0

    def cook_time(self):
        try:
            time = self.soup.find('meta', {'itemprop': 'cookTime'}).get_text()
            matched = TIME_REGEX.search(time)
            total_minutes = int(matched.groupdict().get('minutes') or 0)
            total_minutes += 60 * int(matched.groupdict().get('hours') or 0)
            return total_minutes
        except AttributeError:  # when there is no span with class prep-time / cook-time
            return 0

    def total_time(self):
        return self.prep_time() + self.cook_time()

    def ingredients(self):
        ingredients_html = self.soup.findAll('span', {'itemprop': "ingredients"})
        return [
            ingredient.get_text(strip=True)
            for ingredient in ingredients_html
            if len(ingredient.get_text(strip=True)) > 0
        ]

    def instructions(self):
        instructions_html = self.soup.findAll('span', {'itemprop': 'recipeInstructions'})
        return '\n'.join(
            [
                instruction.get_text(strip=True)
                for instruction in instructions_html
            ])
