import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class SunBasket(AbstractScraper):
    @classmethod
    def host(self, domain="com"):
        return f"sunbasket.{domain}"

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        minutes_tag = self.soup.find("span", text=re.compile(r"Minutes"))
        return get_minutes(minutes_tag.parent.get_text())

    def yields(self):
        yields_tag = self.soup.find("span", text=re.compile(r"Servings,"))
        return get_yields(yields_tag.parent.get_text())

    def ingredients(self):
        ingredients_container = self.soup.find(class_="ingredients-list")
        ingredients = ingredients_container.findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def _instructions_list(self):
        instructions_container = self.soup.find(
            "div", {"class": "instructions-container"}
        )
        instructions = instructions_container.findAll("div", {"class": "step"})
        instruction_list = []
        for instruction in instructions:
            step_number_tag = instruction.find(class_="step-number")
            if step_number_tag is not None:
                step_number = normalize_string(
                    instruction.find(class_="step-number").get_text()
                )
                step_name = normalize_string(
                    instruction.find(class_="step-header").get_text()
                )
                step_instructions = normalize_string(
                    instruction.find(class_="instruction-description").get_text()
                )
                instruction_list.append(
                    f"{step_number}: {step_name} - {step_instructions}"
                )
        return instruction_list

    def instructions(self):
        data = self._instructions_list()
        return "\n".join(data) if data else None

    def image(self):
        container = self.soup.find("div", {"class": "recipe-image-container"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None
