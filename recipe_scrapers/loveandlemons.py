from ._abstract import AbstractScraper


class LoveAndLemons(AbstractScraper):
    @classmethod
    def host(cls):
        return "loveandlemons.com"

    def ingredients(self):
        ingredients_elements = self.soup.select(".wprm-recipe-ingredient")
        return [element.get_text() for element in ingredients_elements]
