# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class Ricetta(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricetta.it"

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def instructions(self):
        instructions_list = []

        # ricetta uses an inline, square-bracketed numbering system;
        #   "crumble the biscuits [1].  bake [2] in the oven."
        current_instruction = ""
        for sentence in self.schema.instructions().split("."):
            current_instruction += sentence + "." if sentence.strip() else ""
            if "[" in sentence and "]" in sentence:
                instructions_list.append(current_instruction.lstrip(" "))
                current_instruction = ""

        if current_instruction:
            instructions_list.append(current_instruction.lstrip(" "))

        return "\n".join(instructions_list)

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
