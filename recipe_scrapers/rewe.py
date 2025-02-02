from ._abstract import AbstractScraper
from ._utils import normalize_string


class Rewe(AbstractScraper):
    @classmethod
    def host(cls):
        return "rewe.de"

    def ingredients(self):
        ingredient_list = self.soup.find("ul", {"id": "ingredient_list"})
        list_items = ingredient_list.find_all("li", {"class": "ingredient_list_item"})
        ingredients = []

        for item in list_items:
            amount_div = item.find("div", {"class": "formattedAmountDiv"})
            amount = (
                normalize_string(amount_div.get_text(strip=True)) if amount_div else ""
            )

            name_span = item.find("span", {"class": "break-words"})
            name = normalize_string(name_span.get_text(strip=True)) if name_span else ""

            if amount == "0":
                ingredients.append(name)
            else:
                ingredient_text = f"{amount} {name}".strip()
                ingredients.append(ingredient_text)

        return ingredients

    def instructions(self):
        step_divs = self.soup.find_all("div", {"class": "step-ingredients"})
        steps = []

        for step in step_divs:
            instruction = step.find(
                "div",
                {
                    "class": "ld-rds mt-4 self-stretch text-sm leading-5 text-gray-1000 md:text-base lg:mt-6 lg:leading-6 [&_a:hover]:text-brand-800 [&_a]:underline [&_a]:underline-offset-3"
                },
            )

            steps.append(instruction.get_text().strip())

        return "\n".join(steps)
