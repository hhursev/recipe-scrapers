from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
import re


class TwentyFourKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "24kitchen.nl"

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            ".ingredient-list-title",
            ".recipe-ingredient",
        )
        if (
            len(groups) == 1
            and groups[0].purpose
            and groups[0].purpose.strip() == self.schema.title()
        ):
            groups[0].purpose = None
        return groups

    def instructions(self):
        instructions = []

        # Instructions format #1
        preparation_steps = self.soup.select(
            ".preparation-step .field--name-field-text"
        )
        for step in preparation_steps:
            text = step.get_text(strip=True)
            if not text.lower().startswith("stap:"):
                instructions.append(text)

        # Instructions format #2
        paragraph_steps = self.soup.select(".preparation-text p")
        for step in paragraph_steps:
            text = step.get_text(strip=True)
            cleaned_instructions_text = re.sub(r"^Stap\s*\d+:?", "", text).strip()
            if cleaned_instructions_text:
                instructions.append(cleaned_instructions_text)

        return "\n".join(instructions)
