from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class IG(AbstractScraper):
    @classmethod
    def host(cls):
        return "receitas.ig.com.br"

    def title(self) -> Optional[str]:
        return self.soup.find("h2", {"itemprop": "name"}).get_text()

    def total_time(self) -> Optional[int]:
        container = self.soup.find("div", {"class": "box-info-preparacao"})
        if not container:
            return None
        else:
            return int(container.find("span", {"class": "valor"}).get_text())

    def yields(self) -> Optional[str]:
        container = self.soup.find("div", {"class": "box-info-rendimento"})
        if not container:
            return None
        else:
            return get_yields(container.find("span", {"class": "valor"}).get_text())

    def image(self) -> Optional[str]:
        container = self.soup.find("div", {"class": "box-img-receita"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find("ul", {"class", "lista-ingredientes"}).findAll(
            "li"
        )

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("div", {"class": "box-preparo"})
        return normalize_string(instructions.get_text())
