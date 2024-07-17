from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class SaboresAjinomoto(AbstractScraper):
    @classmethod
    def host(cls):
        return "saboresajinomoto.com.br"

    def site_name(self):
        raise StaticValueException(return_value="Sabores Ajinomoto")

    def title(self):
        return self.schema.title().capitalize()

    def category(self):
        breadcrumb = self.soup.find("ul", {"class": "bread_crumb"})

        if breadcrumb:
            breadcrumb_items = breadcrumb.find_all("li")
            if len(breadcrumb_items) >= 2:
                return breadcrumb_items[1].text

    def ingredients(self):
        ingredients_list = []
        ingredients_section = self.soup.find("div", {"class": "ingredients"})

        if ingredients_section:
            li_items = ingredients_section.find_all("li")
            for item in li_items:
                ingredient_text = normalize_string(item.text)
                ingredients_list.append(ingredient_text)

        return ingredients_list

    def instructions(self):
        instructions_list = []
        instructions_section = self.soup.find("div", {"class": "steps"})

        if instructions_section:
            ol_items = instructions_section.find_all("li")
            for item in ol_items:
                instructions_list.append(normalize_string(item.text))

        return "\n".join(instructions_list)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredients p",
            ".ingredients li",
        )
