from ._abstract import AbstractScraper


class Chefkoch(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefkoch.de"

    def instructions(self):
        # The first element is always "Zubereitung", which is not actually a step
        raw_instructions = self.schema.instructions().split("\n")
        return "\n".join(raw_instructions[1:])
