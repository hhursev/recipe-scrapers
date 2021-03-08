from bs4 import BeautifulSoup

from ._abstract import AbstractScraper


class BBCGoodFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "bbcgoodfood.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        inst = str(self.schema.instructions())
        instSoup = BeautifulSoup(inst, features="html.parser")
        return instSoup.text
