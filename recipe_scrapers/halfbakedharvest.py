import re

from ._abstract import AbstractScraper


class HalfBakedHarvest(AbstractScraper):
    # Splits between inline numbered steps after sentence punctuation, e.g. "400°F.2. Mix" -> "400°F." / "2. Mix"
    _INLINE_STEP_PATTERN = re.compile(r"(?<=[.!?])\s*(?=\d+\.\s)")

    @classmethod
    def host(cls):
        return "halfbakedharvest.com"

    def instructions(self):
        recipe_instructions = self.schema.data.get("recipeInstructions")

        if (isinstance(recipe_instructions, list)
            and len(recipe_instructions) == 1
            and isinstance(recipe_instructions[0], dict)
            and recipe_instructions[0].get("@type") == "HowToStep"):
            raw_text = recipe_instructions[0].get("text")
            if isinstance(raw_text, str):
                steps = []
                for step in self._INLINE_STEP_PATTERN.split(raw_text.strip()):
                    if step.strip():
                        steps.append(step)
                if len(steps) > 1:
                    return "\n".join(steps)

        return self.schema.instructions()
