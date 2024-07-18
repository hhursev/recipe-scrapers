from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException
from ._grouping_utils import group_ingredients


class DobruChutAktualitySK(AbstractScraper):
    @classmethod
    def host(cls):
        return "dobruchut.aktuality.sk"

    def keywords(self):
        # site has no support for recipe keywords
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        p_list = self.soup.find("div", {"class": "procedure-list"}).findChildren("p")

        instructions = []
        for p in p_list:
            p_text = p.get_text().strip()
            if p_text:
                instructions.append(p_text)

        return "\n".join(instructions)

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".title-red-small",
            ".wrap",
        )
