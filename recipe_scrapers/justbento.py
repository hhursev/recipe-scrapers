from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class JustBento(AbstractScraper):
    @classmethod
    def host(cls):
        return "justbento.com"

    def title(self) -> Optional[str]:
        expected_prefix = "Recipe: "
        title = self.soup.find("meta", {"property": "og:title", "content": True})
        return title.get("content").replace(expected_prefix, "")

    def total_time(self) -> Optional[int]:
        time = self.soup.find(
            "div", {"class": "field-name-taxonomy-vocabulary-2"}
        ).find("a", {"typeof": "skos:Concept"})
        return get_minutes(time)

    def yields(self) -> Optional[str]:
        return "1"

    def ingredients(self) -> Optional[List[str]]:
        ingredients = (
            self.soup.find("div", {"class": "field-name-body"}).find("ul").findAll("li")
        )
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self) -> Optional[str]:
        elements_after_title = (
            self.soup.find("div", {"class": "field-name-body"})
            .find("h3")
            .find_next_sibling("ul")
            .find_next_siblings()
        )

        instructions: List[str] = []
        for element in elements_after_title:
            if instructions and element.name != "p":
                break
            if element.name == "p":
                instructions.append(element.get_text())
            instructions = [
                normalize_string(instruction) for instruction in instructions
            ]

        return "\n".join(instructions) if instructions else None

    def image(self) -> Optional[str]:
        image = self.soup.find("div", {"class": "field-name-body"}).find(
            "img", {"class": "centerimg", "src": True}
        )
        return image["src"] if image else None
