from ._abstract import AbstractScraper
from ._utils import normalize_string


class Abril(AbstractScraper):
    @classmethod
    def host(cls):
        return "claudia.abril.com.br"

    def instructions(self):
        modo_de_preparo = self.soup.find("div", class_="modo-de-preparo")
        instructions = modo_de_preparo.find_all("p")

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
