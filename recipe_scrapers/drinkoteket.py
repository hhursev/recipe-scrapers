# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Drinkoteket(AbstractScraper):
    @classmethod
    def host(cls):
        return "drinkoteket.se"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return 1

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients_element = self.soup.find("ul", {"class": "ingredients"})

        ingredients_separator = ingredients_element.find("li", {"class": "separator"})

        if ingredients_separator is not None:
            separator_index = ingredients_element.index(ingredients_separator)
            raw_list = ingredients_element.findAll("span")[0::2][:separator_index]
        else:
            raw_list = ingredients_element.findAll("span")[0::2]

        ingredients = [i.getText().strip() for i in raw_list]
        return ingredients

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
