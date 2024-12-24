from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class Ricetta(AbstractScraper):
    @classmethod
    def host(cls):
        return "ricetta.it"

    def site_name(self):
        raise StaticValueException(return_value="Ricetta.it")

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
