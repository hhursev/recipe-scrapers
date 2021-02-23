# BettyCrocker.com scraper
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 18 January, 2020
# =======================================================

from typing import List, Optional

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class BettyCrocker(AbstractScraper):
    @classmethod
    def host(cls):
        return "bettycrocker.com"

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        total_time = 0
        tt = self.soup.find("li", {"id": "gmi_rp_primaryAttributes_total"})
        if tt:
            tt1 = normalize_string(tt.get_text())
            tt2 = get_minutes(tt1)
        total_time = tt2
        return total_time

    def yields(self) -> Optional[str]:
        recipe_yield = self.soup.find("li", {"id": "gmi_rp_primaryAttributes_servings"})
        if recipe_yield:
            y = recipe_yield.find(attrs={"class": "attributeValue"})
            valu = y.text + " serving(s)"
            return valu
        else:
            return get_yields(
                self.soup.find(
                    "div", {"class": "recipe-adjust-servings__original-serving"}
                ).get_text()
            )

    def image(self) -> Optional[str]:
        image = self.soup.find("div", {"class": "recipeImage"})
        if image:
            tag = image.find("meta")
            src = tag.get("content", None)

        return src if image else None

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.findAll("div", {"class": "recipePartIngredient"})

        if not ingredients:
            ingredients = self.soup.findAll("span", {"class": "ingredients-item-name"})

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if ingredient.get_text(strip=True)
            not in ("Add all ingredients to list", "", "ADVERTISEMENT")
        ]

    def instructions(self) -> Optional[str]:
        instructions = self.soup.findAll("li", {"class": "recipePartStep"})
        retstr = ""
        for instruction in instructions:
            instemp = instruction.find("div", {"class": "recipePartStepDescription"})
            s = normalize_string(instemp.get_text())

            retstr = retstr + s.strip() + " "
        instructions = retstr.strip()
        return instructions

    def ratings(self) -> Optional[float]:
        r = self.soup.find("span", {"class": "ratingCount"}).get_text()
        if "\xa0Ratings" in r:
            r = r.replace("\xa0Ratings", "")
        return int(r)
