from ._abstract import AbstractScraper
from ._utils import normalize_string


class TasteOfHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteofhome.com"

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
        instructions = self.soup.findAll("li", {"class": "recipe-directions__item"})
        if instructions:
            return "\n".join(
                [
                    normalize_string(instruction.get_text())
                    for instruction in instructions
                ]
            )
        else:
            # In case our HTML parsing doesn't find any instructions, fall back to what the schema provides.
            return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
