from ._abstract import AbstractScraper


class CuisineAZ(AbstractScraper):
    @classmethod
    def host(cls):
        return "cuisineaz.com"

    def ingredients(self):
        ingredients_list = self.schema.ingredients()

        # Check if the first line is blank and skip it
        if ingredients_list and not ingredients_list[0].strip():
            return ingredients_list[1:]

        return ingredients_list
