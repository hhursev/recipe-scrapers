from ._abstract import AbstractScraper
from ._utils import normalize_string


class TasteOfHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteofhome.com"

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
