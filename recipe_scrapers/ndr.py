from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Ndr(AbstractScraper):
    @classmethod
    def host(cls):
        return "ndr.de"

    def author(self):
        return "NDR"

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            "h2",
            ".ingredient",
        )

        for group in groups:
            if group.purpose and group.purpose.strip().lower() == "zutaten:":
                group.purpose = None

        return groups

    def instructions(self):
        instructions = []

        for element in self.soup.find_all(["p", "h2"]):
            if element.name == "h2" and "Nährwerte pro Portion" in element.get_text(
                strip=True
            ):
                break
            if element.name == "p":
                text = element.get_text(separator="\n", strip=True)
                instructions.append(text)

        return "\n".join(instructions)
