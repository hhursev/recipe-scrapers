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

    def instructions(self):
        p_list = self.soup.find("div", {"class": "procedure-list"}).findChildren("p")

        instructions = []
        for p in p_list:
            p_text = p.get_text().strip()
            if p_text:
                instructions.append(p_text)

        return "\n".join(instructions)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".title-red-small",
            ".wrap",
        )
