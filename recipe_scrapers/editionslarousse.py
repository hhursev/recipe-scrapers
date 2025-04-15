from ._abstract import AbstractScraper
from ._utils import normalize_string, get_equipment
from ._grouping_utils import group_ingredients


class EditionsLarousse(AbstractScraper):
    @classmethod
    def host(cls):
        return "editions-larousse.fr"

    def author(self):
        return "Larousse"

    def ingredients(self):
        elements = self.soup.select(
            "div.Ingredients ul li, div.Ingredients div.Contents p"
        )
        return [
            normalize_string(element.get_text())
            for element in elements
            if normalize_string(element.get_text())
        ]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".Ingredients h2",
            ".Ingredients li, .Ingredients p",
        )

    def equipment(self):
        elements = self.soup.select("div.Equipment div.Contents p")
        equipment = [
            normalize_string(element.get_text())
            for element in elements
            if normalize_string(element.get_text())
        ]
        return get_equipment(equipment)

    def instructions(self):
        steps = []
        containers = self.soup.select("div.Step div.Contents")

        for container in containers:
            paragraphs = container.select("p") or [container]
            for paragraph in paragraphs:
                text = normalize_string(paragraph.get_text())
                if text.startswith("* "):
                    text = text[2:].strip()
                if text:
                    steps.append(text)

        return "\n".join(steps)
