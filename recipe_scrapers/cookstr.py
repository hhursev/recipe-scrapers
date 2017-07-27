from ._abstract import AbstractScraper
from ._utils import get_minutes, get_servings, normalize_string
from datetime import datetime
import re


class Cookstr(AbstractScraper):

    @classmethod
    def host(self):
        return 'cookstr.com'

    def title(self):
        return normalize_string(self.soup.find('h1', {'class': 'articleHeadline'}).get_text())

    def _short_property(self, text):
        html= self.soup.find('span', {'class': 'attrLabel'}, string=text)
        if not html:
            return None
        html = html.parent
        text = html.find(text=True, recursive=False)
        if text is None:
            text = html.findAll('span')[1].get_text()
        if text is not None:
            text = str(text).strip()
        return text

    def date_modified(self):
        text = normalize_string(self.soup.find('div', {'class': 'dateModified'}).get_text())
        dt = datetime.strptime(text, "Updated %B %d, %Y")
        return dt.date()

    def total_time(self):
        return self._short_property("Total Time")

    def serves(self):
        text = self._short_property("Serves")
        if not text:
            text = self._short_property("Makes")
        if text:
            return get_servings(text) or text # cookstr is unusually random, just put the text

    def _parse_boolean(self, text):
        if text == "Yes":
            return True
        if text == "No":
            return False
        return text

    def make_ahead_recipe(self):
        text = self._short_property("Make Ahead Recipe")
        if text:
            return self._parse_boolean(text)

    def kid_friendly(self):
        text = self._short_property("Kid Friendly")
        if text:
            return self._parse_boolean(text)

    def cooking_method(self):
        html = self.soup.find('span', {'itemprop': 'cookingMethod'})
        if html:
            return normalize_string(html.get_text())

    def cost(self):
        return self._short_property("Cost")

    def difficulty(self):
        cost_html = self.soup.find('span', {'class': 'attrLabel'}, string="Cost").parent.parent
        html = cost_html.find_next_sibling("div").find('img')
        if html:
            return html["alt"]

    def chef(self):
        html = self.soup.find('h4', string="Chef")
        if not html:
            return None
        html = html.find_next_sibling("h5")
        return normalize_string(html.get_text())

    def contributors(self):
        html = self.soup.find('h4', string="Contributors")
        if not html:
            return None
        html = html.find_next_sibling("ul").find_all("li")
        return [
            normalize_string(user.get_text())
            for user in html 
        ]
    
    def cookbook(self):
        html = self.soup.find('h4', string='Cookbook')
        if html:
            html = html.find_next_sibling("h5").find("a")
        if html:
            return normalize_string(html.get_text())

    def cookbook_publisher(self):
        html = self.soup.find('h4', string='Cookbook')
        if html:
            html = html.find_next_sibling("p", {'class': 'publisher'})
        if not html:
            return None
        text = normalize_string(html.get_text())
        if text.startswith("Published by"):
            text = text[len("Published by"):]
        return text.strip()

    def copyright(self):
        html = self.soup.find("p", {"class": "copyrightLink"})
        if html:
            return normalize_string(html.get_text())

    def image_url(self):
        html = self.soup.find('div', {'class': "mainImg"}).find("img")
        if not html:
            return None
        src = html["src"]
        if src.startswith("//"): # Get rid of schemeless uri for export
          src = "https:" + src 
        return src

    def image_credit_name(self):
        html = self.soup.find('div', {'class': "articleImgCredit"})
        if html:
            html = html.find("a")
        if html:
            return normalize_string(html.get_text())

    def image_credit_site(self):
        html = self.soup.find('div', {'class': "articleImgCredit"})
        if html:
            html = html.find("a")
        if html:
            return html["href"]

    def description(self):
        #html = self.soup.find('div', {'class':'articleDiv'}).find(
        html = self.soup.find('div', {'class': 'mainImg'}).find_next_sibling(lambda x: (x.name == 'p') or (x.name == 'div' and "articleAttrSection" in x.get("class", '')))
        return normalize_string(html.get_text())

    def comment_count(self):
        html = self.soup.find('h4', {'id': 'commentCount'})
        text = html.get_text()
        m = re.match("(?P<comments>\d+) Comments", text)
        if m:
            return int(m.groupdict().get("comments"))

    def rating_value(self):
        html = self.soup.find('meta', {'itemprop': 'ratingValue'})
        if html:
            return float(html["content"])
        else:
            return None

    def rating_count(self):
        html = self.soup.find('meta', {'itemprop': 'ratingCount'})
        if html:
            return int(html["content"])
        else:
            return 0

    def occasion(self):
        return self._short_property("Occasion")

    def recipe_course(self):
        return self._short_property("Recipe Course")

    def dietary_considerations(self):
        return self._short_property("Dietary Consideration")

    def meal(self):
        return self._short_property("Meal")

    def taste_and_texture(self):
        return self._short_property("Taste and Texture")

    def type_of_dish(self):
        return self._short_property("Type of Dish")

    def ingredients(self):
        ingredients = self.soup.findAll('span', {'itemprop': "ingredients"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def ingredients_detailed(self):
        ingredients = self.soup.findAll('span', {'itemprop': "ingredients"})

        return [
            {
                "line": normalize_string(ingredient.get_text()),
                "ingredients": [normalize_string(e.get_text()) for e in ingredient.findAll('span', 
                  {'class': 'ingredient'})],
            }
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions_html = self.soup.find('div', {'class': 'stepByStepInstructionsDiv'})

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions_html.findAll('p')
        ])
