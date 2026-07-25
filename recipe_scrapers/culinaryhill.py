from ._abstract import AbstractScraper
from ._wprm import WPRMMixin


class CulinaryHill(WPRMMixin, AbstractScraper):
    @classmethod
    def host(cls):
        return "culinaryhill.com"

    def ingredients(self):
        return [
            li.get_text(" ", strip=True).replace("▢", "").strip()
            for li in self.soup.select(
                "ul.wprm-recipe-ingredients > li.wprm-recipe-ingredient"
            )
        ]
