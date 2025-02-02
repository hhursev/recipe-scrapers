from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_minutes, normalize_string
from ._grouping_utils import group_ingredients


class USDAMyPlate(AbstractScraper):
    @classmethod
    def host(cls):
        return "myplate.gov"

    def site_name(self):
        raise StaticValueException(return_value="MyPlate")

    def cook_time(self):
        cook_time_span = self.soup.find(
            "div", {"class": "mp-recipe-full__detail--cook-time"}
        ).find("span", {"class": "mp-recipe-full__detail--data"})

        if cook_time_span:
            return get_minutes(cook_time_span)

        return 0

    def prep_time(self):
        prep_time_span = self.soup.find(
            "div", {"class": "mp-recipe-full__detail--prep-time"}
        ).find("span", {"class": "mp-recipe-full__detail--data"})

        if prep_time_span:
            return get_minutes(prep_time_span)

        return 0

    def total_time(self):
        cook_time = self.cook_time()
        prep_time = self.prep_time()

        total_minutes = cook_time + prep_time
        return total_minutes

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"class": "field--name-field-ingredients"}
        ).findAll("li")

        return [normalize_string(paragraph.get_text()) for paragraph in ingredients]

    def ingredient_groups(self):
        ingredients_section = self.soup.find(
            "div", {"class": "field--name-field-ingredients"}
        )
        return group_ingredients(
            self.ingredients(),
            ingredients_section,
            "b",
            "li.field__item",
        )

    def instructions(self):
        div = self.soup.find(
            "div",
            {
                "class": "clearfix text-formatted field field--name-field-instructions field--type-text-long field--label-above"
            },
        )
        instructions = div.find("div", {"class", "field__item"})

        return "\n".join(instructions.stripped_strings)

    def nutrients(self):
        nutrition = {}

        table = self.soup.find(
            "form", {"class": "mp-recipe-full__nutrition-form"}
        ).find("table")
        rows = table.find_all("tr")

        elements = []
        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            elements.append([ele for ele in cols if ele])

        for el in elements:
            if len(el) > 1:
                nutrition[el[0]] = el[1]

        return nutrition
