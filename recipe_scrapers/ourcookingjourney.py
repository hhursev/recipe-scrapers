import re

from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException, StaticValueException
from ._grouping_utils import IngredientGroup
from ._utils import get_yields, normalize_string


class OurCookingJourney(AbstractScraper):
    @classmethod
    def host(cls):
        return "ourcookingjourney.com"

    def author(self):
        raise StaticValueException(return_value="Francesco Mattana")

    def title(self):
        return self.soup.select_one(".blog-title").get_text()

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def yields(self):
        servings = self.soup.select_one(".blog-content").find(
            string=re.compile(r"(Serves|Makes)\s+\d", re.IGNORECASE)
        )
        return get_yields(servings)

    def ingredients(self):
        return [
            normalize_string(ingredient.get_text())
            for ingredient_list in self._get_lists("ingredients")
            for ingredient in ingredient_list.select("li")
        ]

    def ingredient_groups(self):
        groups = []
        for ingredient_list in self._get_lists("ingredients"):
            heading = ""
            for sibling in ingredient_list.previous_siblings:
                if sibling.name in ("ul", "ol"):
                    break
                heading = normalize_string(sibling.get_text()).rstrip(":").strip()
                if heading:
                    break
            groups.append(
                IngredientGroup(
                    ingredients=[
                        normalize_string(ingredient.get_text())
                        for ingredient in ingredient_list.select("li")
                    ],
                    purpose=(
                        heading if heading.lower() not in ("", "ingredients") else None
                    ),
                )
            )
        if not any(group.purpose for group in groups):
            return super().ingredient_groups()
        return groups

    def instructions(self):
        return "\n".join(
            normalize_string(instruction.get_text())
            for instruction_list in self._get_lists("method")
            for instruction in instruction_list.select("li")
        )

    def _get_lists(self, section):
        current_section = None
        for element in self.soup.select(
            ".blog-content strong, .blog-content ul, .blog-content ol"
        ):
            if element.name == "strong":
                heading = normalize_string(element.get_text()).rstrip(":").lower()
                if heading in ("ingredients", "method"):
                    current_section = heading
            elif current_section == section:
                yield element

    def description(self):
        return normalize_string(
            self.soup.select_one(".blog-content .paragraph").get_text()
        )

    def notes(self):
        notes = []
        for paragraph in self.soup.select(".blog-content .paragraph"):
            for heading in paragraph.find_all(
                string=re.compile(r"^\s*\*?\s*top\s+tip\s*:?\s*$", re.IGNORECASE)
            ):
                while heading.parent != paragraph:
                    heading = heading.parent
                parts = []
                line_break = False
                for sibling in heading.next_siblings:
                    if sibling.name == "br":
                        if line_break:
                            break
                        line_break = True
                    else:
                        parts.append(sibling.get_text())
                        if normalize_string(sibling.get_text()):
                            line_break = False
                note = normalize_string("".join(parts)).lstrip("-–—: ")
                if note:
                    notes.append(note)
        return notes
