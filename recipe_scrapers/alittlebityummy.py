from ._abstract import AbstractScraper
from ._utils import normalize_string


class ALittleBitYummy(AbstractScraper):
    @classmethod
    def host(cls):
        return "alittlebityummy.com"

    def author(self):
        author_tag = self.soup.find(
            "h4", string=lambda text: text and "Author:" in text
        )
        if author_tag:
            return author_tag.text.replace("Author:", "").strip()

    def ingredients(self):
        ingredient_blocks = self.soup.select(".ingredients-tab-content div")
        seen = set()
        ingredients = []
        for block in ingredient_blocks:
            unit_display = block.find("b", class_="ingredient-unit-display")
            primary = (
                unit_display.get("data-primary-amount", "").strip(),
                unit_display.get("data-primary-unit", "").strip(),
            )
            secondary = (
                unit_display.get("data-secondary-amount", "").strip(),
                unit_display.get("data-secondary-unit", "").strip(),
            )

            amount_text = f"{primary[0]} {primary[1]}"
            if secondary[0]:
                amount_text += f" ({secondary[0]} {secondary[1]})"

            name = block.find("span", class_="ingredient-name-display").text.strip()
            full_ingredient = f"{amount_text} {name}"
            if full_ingredient not in seen:
                seen.add(full_ingredient)
                ingredients.append(full_ingredient)
        return ingredients

    def instructions(self):
        instruction_steps = self.soup.select("#method ol li")
        return "\n".join(
            normalize_string(step.get_text())
            for step in instruction_steps
            if step.get_text()
        )
