from collections import defaultdict

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


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

        if not categoryheader:
            return ""

        return categoryheader.find_next("p").get_text()

    def total_time(self):
        timeheader = self.soup.find(string=lambda text: text and text.lower() == "time")

        if not timeheader:
            return ""

        return int(timeheader.find_next("p").get_text().split(" ")[0])

    def yields(self):
        servingheader = self.soup.find(
            string=lambda text: text and text.lower() == "servings"
        )

        if not servingheader:
            return ""

        servingsize = servingheader.find_next("p").get_text().split(" ")[0]
        return (
            f"{servingsize} serving"
            if int(servingsize) == 1
            else f"{servingsize} servings"
        )

    def image(self):
        return self.soup.find("img", {"alt": "recipe"}).get("src")

    def ingredients(self):
        possibleingredients = (
            self.soup.find("section", {"id": "recipe-ingredients"})
            .findChildren(
                "div",
                {
                    "class": "flex flex-col gap-y-4 font-medium md:basis-1/2 xl:basis-2/5"
                },
            )[0]
            .find_all("p")
        )
        ingredientslist = []

        if possibleingredients:
            for ingredient in possibleingredients:
                if not ingredient.find("strong") and normalize_string(
                    ingredient.get_text()
                ):
                    ingredientslist.append(normalize_string(ingredient.get_text()))
        else:
            possibleingredients = (
                self.soup.find("section", {"id": "recipe-ingredients"})
                .findChildren(
                    "div",
                    {
                        "class": "flex flex-col gap-y-4 font-medium md:basis-1/2 xl:basis-2/5"
                    },
                )[0]
                .find_all("li")
            )
            ingredientslist = [
                normalize_string(ingredient.get_text())
                for ingredient in possibleingredients
            ]

        return ingredientslist

    def ingredient_groups(self):
        possibleingredients = (
            self.soup.find("section", {"id": "recipe-ingredients"})
            .findChildren(
                "div",
                {
                    "class": "flex flex-col gap-y-4 font-medium md:basis-1/2 xl:basis-2/5"
                },
            )[0]
            .find_all("p")
        )
        groupings = defaultdict(list)
        current_heading = None

        if possibleingredients:
            for ingredient in possibleingredients:
                normalizedingredient = normalize_string(ingredient.get_text())
                if normalizedingredient:
                    if ingredient.find("strong"):
                        current_heading = normalizedingredient
                    else:
                        groupings[current_heading].append(normalizedingredient)
        else:
            possibleingredients = (
                self.soup.find("section", {"id": "recipe-ingredients"})
                .findChildren(
                    "div",
                    {
                        "class": "flex flex-col gap-y-4 font-medium md:basis-1/2 xl:basis-2/5"
                    },
                )[0]
                .find_all()
            )
            for ingredient in possibleingredients:
                normalizedingredient = normalize_string(ingredient.get_text())
                if normalizedingredient:
                    if (
                        ingredient.name == "h3"
                        and normalizedingredient.lower() != "ingredients"
                    ):
                        current_heading = normalizedingredient
                    elif ingredient.name == "li":
                        groupings[current_heading].append(normalizedingredient)

        return [
            IngredientGroup(purpose=heading, ingredients=items)
            for heading, items in groupings.items()
        ]

    def instructions(self):
        instructions = (
            self.soup.find("section", {"id": "recipe-ingredients"})
            .findChildren(
                "div",
                {
                    "class": "flex flex-col gap-y-4 font-medium md:basis-1/2 xl:basis-2/5"
                },
            )[1]
            .find_all("p")
        )
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
