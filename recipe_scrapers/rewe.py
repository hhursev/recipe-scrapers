import ast
import re

from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_minutes, normalize_string


class Rewe(AbstractScraper):
    @classmethod
    def host(cls):
        return "rewe.de"

    def language(self):
        return self.soup.find("html")["lang"]

    def author(self):
        return self.schema.author()

    def title(self):
        return self.soup.find("h1", {"class": "ld-rds"}).get_text()

    def category(self):
        category = self.soup.find(
            "a", {"id": "nutrition-information-mobile"}
        ).get_text()
        return normalize_string(category)

    def total_time(self):
        x_data = self.soup.select_one(
            "#recipe-basics>.ld-rds:first-child:first-child div:last-child span:first-child"
        ).get("x-data")

        # Transform the `x-data` string into a dictionary
        data_dict = ast.literal_eval(
            re.sub(r"(\w+):", r"'\1':", x_data.replace("`", "'"))
        )

        # Return the "displayText" field
        return get_minutes(data_dict["displayText"])

    def yields(self):
        return self.soup.find("span", {"x-text": "currentServings"}).get_text().strip()

    def ingredients(self):
        ingredient_list = self.soup.find("ul", {"id": "ingredient_list"})
        list_items = ingredient_list.find_all("li", {"class": "ingredient_list_item"})
        ingredients = []

        for item in list_items:
            amount = normalize_string(
                item.find("div", class_="formattedAmountDiv").get_text()
            )
            ingredient = item.find(
                "span", {"class": "ld-rds break-words leading-6"}
            ).get_text(" ", strip=True)
            ingredients.append(
                normalize_string(f"{amount + ' ' if amount != '0' else ''}{ingredient}")
            )

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

    def description(self):
        return self.soup.find("meta", {"property": "og:description"})["content"]

    def canonical_url(self):
        return self.soup.find("meta", {"property": "og:url"})["content"]

    def site_name(self):
        raise StaticValueException(return_value="REWE")
