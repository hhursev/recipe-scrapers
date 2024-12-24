from ._abstract import AbstractScraper
from ._utils import normalize_string


class SunBasket(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"sunbasket.{domain}"

    def site_name(self):
        return self.author()

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
