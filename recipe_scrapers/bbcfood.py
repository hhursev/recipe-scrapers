from ._abstract import AbstractScraper
from ._utils import get_minutes, get_servings, normalize_string

class BBCFood(AbstractScraper):

    @classmethod
    def host(self):
        return 'bbc.co.uk'

    def title(self):
        return self.soup.find('h1', {'class': 'content-title__text'}).get_text()

    def total_time(self):
        return self.preparation_time() + self.cooking_time()

    def preparation_time(self):
        return get_minutes(self.soup.find('p', {'itemprop': 'prepTime'}))

    def cooking_time(self):
        return get_minutes(self.soup.find('p', {'itemprop': 'cookTime'}))

    def serves(self):
        return get_servings(self.soup.find('p', {'itemprop': 'recipeYield'}))

    def description(self):
        html = self.soup.find('p', {'itemprop': 'description'})
        if html:
            return normalize_string(html.get_text())
        else:
            return ""

    def chef(self):
        return normalize_string(self.soup.find('div', {'class': 'chef__name'}).find("a").get_text())
    def chef_id(self):
        return self.soup.find('div', {'class': 'chef__name'}).find("a")["href"].split("/")[-1]

    def program(self):
        programme_html = self.soup.find('div', {'class': 'chef__programme-name'})
        if programme_html:
            return normalize_string(programme_html.find("a").get_text())
    def program_id(self):
        programme_html = self.soup.find('div', {'class': 'chef__programme-name'})
        if programme_html:
            return programme_html.find("a")["href"].split("/")[-1]

    def photo_url(self):
        html = self.soup.find('img', {'class': 'recipe-media__image'})
        if html:
            return html["src"]

    def ingredients(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients_html
        ]

    def ingredients_detailed(self):
        ingredients_html = self.soup.findAll('li', {'itemprop': "ingredients"})

        detailed = []
        for ingredient in ingredients_html:
            simple_ingredient = ingredient.find("a", {"class": "recipe-ingredients__link"})
            if simple_ingredient:
                simple_ingredient = normalize_string(simple_ingredient.get_text())
            detailed.append({
                "line": normalize_string(ingredient.get_text()),
                "ingredient": simple_ingredient,
            })
        return detailed

    def instructions(self):
        instructions_html = self.soup.findAll('li', {'itemprop': 'recipeInstructions'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html
        ])
