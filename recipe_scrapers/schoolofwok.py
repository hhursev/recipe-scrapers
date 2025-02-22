from collections import defaultdict

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import get_minutes, get_yields, normalize_string


class SchoolOfWok(AbstractScraper):
    @classmethod
    def host(cls):
        return "schoolofwok.co.uk"

    def author(self):
        return "School of Wok"

    def site_name(self):
        return "School of Wok"

    def title(self):
        return self.soup.find("h1").get_text()

    def cuisine(self):
        categoryheader = self.soup.find(
            string=lambda text: text and text.lower() == "cuisine"
        )

        return categoryheader.find_next(name="p").get_text() if categoryheader else None

    def total_time(self):
        timeheader = self.soup.find(string=lambda text: text and text.lower() == "time")

        return (
            get_minutes(timeheader.find_next(name="p").get_text())
            if timeheader
            else None
        )

    def yields(self):
        servingheader = self.soup.find(
            string=lambda text: text and text.lower() == "servings"
        )

        return (
            get_yields(servingheader.find_next(name="p").get_text())
            if servingheader
            else None
        )

    def image(self):
        return self.soup.find("img", {"alt": "recipe"}).get("src")

    def ingredients(self):
        section = self.soup.find("section", {"id": "recipe-ingredients"})
        div_class = "flex flex-col gap-y-4 font-medium md:basis-1/2 xl:basis-2/5"
        divs = section.findChildren("div", {"class": div_class})

        if not divs:
            return []

        paragraphs = divs[0].find_all("p")
        ingredients_list = []

        if paragraphs:
            for paragraph in paragraphs:
                text = normalize_string(paragraph.get_text())
                if text and not paragraph.find("strong"):
                    ingredients_list.append(text)
        else:
            list_items = divs[0].find_all("li")
            ingredients_list = [
                normalize_string(item.get_text()) for item in list_items
            ]

        return ingredients_list

    def ingredient_groups(self):
        section = self.soup.find("section", {"id": "recipe-ingredients"})
        div_class = "flex flex-col gap-y-4 font-medium md:basis-1/2 xl:basis-2/5"
        divs = section.findChildren("div", {"class": div_class})

        if not divs:
            return []

        paragraphs = divs[0].find_all("p")
        groupings = defaultdict(list)
        current_heading = None

        if paragraphs:
            for paragraph in paragraphs:
                normalized_ingredient = normalize_string(paragraph.get_text())
                if normalized_ingredient:
                    if paragraph.find("strong"):
                        current_heading = normalized_ingredient
                    else:
                        groupings[current_heading].append(normalized_ingredient)
        else:
            list_items = divs[0].find_all()
            for item in list_items:
                if (
                    item.name == "h3"
                    and normalize_string(item.get_text()).lower() != "ingredients"
                ):
                    current_heading = normalize_string(item.get_text())
                elif item.name == "li":
                    normalized_ingredient = normalize_string(item.get_text())
                    if normalized_ingredient:
                        groupings[current_heading].append(normalized_ingredient)

        return [
            IngredientGroup(purpose=heading, ingredients=items)
            for heading, items in groupings.items()
        ]

    def instructions(self):
        section = self.soup.find("section", {"id": "recipe-ingredients"})
        div_class = "flex flex-col gap-y-4 font-medium md:basis-1/2 xl:basis-2/5"
        divs = section.findChildren("div", {"class": div_class})

        if len(divs) < 2:
            return ""

        instructions = divs[1].find_all("p")
        instructionslist = []

        for instruction in instructions:
            normalizedinstruction = normalize_string(instruction.get_text())
            if normalizedinstruction:
                if normalizedinstruction[0].isdigit():
                    instructionslist.append(normalizedinstruction[3:])
                elif normalizedinstruction[0] == "•":
                    instructionslist.append(normalizedinstruction[2:])
                else:
                    instructionslist.append(normalizedinstruction)

        return "\n".join(instructionslist)

    def description(self):
        return self.soup.find(
            "p", {"class": "mb-2 pb-4 border-b border-b-white xl:text-lg"}
        ).get_text()
