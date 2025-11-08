from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._exceptions import StaticValueException


class Yamasa(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipe.yamasa.com"

    def author(self):
        author_tag = self.soup.find("th", string="Author")
        if author_tag:
            td = author_tag.find_next_sibling("td")
            if td:
                return td.get_text(strip=True)
        return self.schema.author()

    def ingredients(self):
        return [
            " ".join(i.stripped_strings)
            for i in self.soup.select(".ingredients .ingredient")
        ]

    def instructions(self):
        instructions = self.schema.instructions()

        filtered_instructions = [
            line
            for line in instructions.split("\n")
            if line.strip().lower() != "preparation"
        ]

        return "\n".join(filtered_instructions)

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".group-head",
            ".ingredient",
        )

    def cuisine(self):
        raise StaticValueException(return_value="Japanese")
