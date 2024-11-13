from ._abstract import AbstractScraper


class AlbertHeijn(AbstractScraper):
    @classmethod
    def host(cls):
        return "ah.nl"

    def instructions(self):
        instructions = self.schema.instructions()

        filtered_instructions = [
            line
            for line in instructions.split("\n")
            if not line.lower().startswith("stap")
        ]

        return "\n".join(filtered_instructions)
