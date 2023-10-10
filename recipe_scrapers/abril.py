# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class Abril(AbstractScraper):
    @classmethod
    def host(cls):
        return "claudia.abril.com.br"

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
        modo_de_preparo = self.soup.find("div", class_="modo-de-preparo")
        instructions = modo_de_preparo.find_all("p")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
