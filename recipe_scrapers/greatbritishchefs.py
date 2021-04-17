# GreatBritishChefs.com scraper
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 6 February, 2020
# =======================================================


from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class GreatBritishChefs(AbstractScraper):
    @classmethod
    def host(cls):
        return "greatbritishchefs.com"

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    def total_time(self):
        total_time = 0
        tt1 = self.soup.find("span", {"class": "RecipeAttributes__Time"})
        if tt1:
            tt = tt1.find("span", {"class": "header-attribute-text"}).get_text()
            tt3 = normalize_string(tt)
            tt2 = get_minutes(tt3)
            if tt3 and (tt2 == 0):
                total_time = tt3
            else:
                total_time = tt2
        return total_time

    def yields(self):
        recipe_yield = self.soup.find("span", {"class": "RecipeAttributes__Serves"})
        if recipe_yield:
            recipe_yield = normalize_string(
                recipe_yield.find("span", {"class": "header-attribute-text"}).get_text()
            )
        return recipe_yield

    def image(self):
        image = self.soup.find("img", {"id": "head-media"}, "src")
        if image:
            src = image.get("src", None)
            if "http:" in src:
                return src
            else:
                src = "http:" + src
        return src if image else None

    def ingredients(self):
        ingredientsOuter = self.soup.find(
            "ul", {"class": "IngredientsList__ListContainer"}
        )
        ingGroup = []
        ingredparts = ingredientsOuter.findAll("li")
        for i in ingredparts:
            x = normalize_string(i.get_text())
            ingGroup.append(x)
        return ingGroup

    def instructions(self):
        instructions = self.soup.find("div", {"class": "Method__List MethodList"})

        ins = instructions.findAll("div", {"class": "MethodList__StepText"})

        return "\n".join([normalize_string(inst.text) for inst in ins])

    def ratings(self):
        # This site does not support ratings at this time
        return None

    def description(self):
        d = normalize_string(
            self.soup.find("div", {"class": "RecipeAbstract__Abstract"}).text
        )
        return d if d else None
