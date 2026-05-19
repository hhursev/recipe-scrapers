from ._abstract import AbstractScraper
from ._utils import normalize_string


class EDEKA(AbstractScraper):
    @classmethod
    def host(cls):
        return "edeka.de"

    def ingredients(self):
        prefix = "o-recipes-m314-ingredients-and-serves__ingredients-"

        return [
            normalize_string(
                f'{i.find("span", {"data-element": prefix + "count"}).text} {i.find("span", {"data-element": prefix + "unit"}).text} {i.find("span", {"data-element": prefix + "label"}).text}'
            )
            for i in self.soup.find_all(
                "li",
                {"class": "o-recipes-m314-ingredients-and-serves__ingredients-item"},
            )
        ]

    def instructions(self):
        return "\n".join(
            [
                normalize_string(i.text)
                for i in self.soup.find_all(
                    "div", {"class": "o-recipes-m315-method__item-content"}
                )
            ]
        )
