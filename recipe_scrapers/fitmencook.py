# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class FitMenCook(AbstractScraper):
    @classmethod
    def host(cls):
        return "fitmencook.com"

    def title(self):
        title = self.soup.find("h1", {"class": "fmc_title_1"}).get_text()
        return title

    def total_time(self):
        total_time_element = self.soup.find("div", {"class": "fmc_total"})
        if total_time_element:
            time_text = total_time_element.find("span", {"class": "fmc_amount"})
            if time_text:
                return get_minutes(time_text.text.strip())

    def yields(self):
        yields = None
        for h4 in self.soup.findAll("h4"):
            raw_yield = h4.text
            for word in raw_yield.split():
                if word.isdigit():
                    yields = word

        if yields:
            return get_yields("{} servings".format(yields))

    def ingredients(self):
        ingredients_parent = self.soup.find("div", {"class": "fmc_ingredients"})
        ingredients = ingredients_parent.findAll("li")
        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if ingredient.find("strong") is None
        ]

    def instructions(self):
        instructions_div = self.soup.find("div", {"class": "fmc_steps"})
        if instructions_div:
            step_elements = instructions_div.findAll("div", {"class": "fmc_sr_step"})

            instructions_list = []
            for step_element in step_elements:
                step_content = step_element.find("div", {"class": "fmc_step_content"})
                if step_content:
                    instruction_text = normalize_string(
                        step_content.find("p").get_text()
                    )
                    instructions_list.append(instruction_text)

            if instructions_list:
                return "\n".join(instructions_list)
