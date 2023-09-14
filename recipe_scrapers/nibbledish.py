# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class NibbleDish(AbstractScraper):
    @classmethod
    def host(cls):
        return "nibbledish.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        schema_instructions = self.schema.ingredients()

        # Good case: multiple instructions were found
        if len(schema_instructions) > 1:
            return schema_instructions

        # Fallback case: to handle situations where all instruction text has been merged
        # into a single recipeInstruction metadata item.
        container = self.soup.find("div", {"class": "recipe-instructions"})
        instructions = container.find_all("li")

        return (
            "\n".join(
                [
                    normalize_string(instruction.get_text())
                    for instruction in instructions
                ]
            )
            or None
        )

    def ratings(self):
        return self.schema.ratings()
