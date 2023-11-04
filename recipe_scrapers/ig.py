# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class IG(AbstractScraper):
    @classmethod
    def host(cls):
        return "receitas.ig.com.br"

    def title(self):
        return self.schema.title()

    def author(self):
        nav = self.soup.find("nav", {"class": "nav-mais-receitas"})
        if nav:
            first = nav.find("li", {"class": "first"})
            if first:
                return first.find("a").get_text()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        container = self.soup.find("div", {"class": "box-info-rendimento"})
        if not container:
            return None
        else:
            return get_yields(container.find("span", {"class": "valor"}).get_text())

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        instructions = self.soup.find("div", {"class": "box-preparo"})
        return normalize_string(instructions.get_text())
