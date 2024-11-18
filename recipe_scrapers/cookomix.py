from ._abstract import AbstractScraper


class Cookomix(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookomix.com"

    def instructions(self):
        instructions_data = self.schema.data.get("recipeInstructions", [])

        instructions = [step.get("text", "") for step in instructions_data]

        filtered_instructions = [
            line for line in instructions if not line.startswith("Ajout d")
        ]

        return "\n".join(filtered_instructions)
