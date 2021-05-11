# gonnawantseconds.py
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 9 February, 2020
# =======================================================


from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class GonnaWantSeconds(AbstractScraper):
    @classmethod
    def host(cls):
        return "gonnawantseconds.com"

    def title(self):
        return normalize_string(self.soup.find("h1").get_text())

    def total_time(self):
        total_time = 0
        try:
            tt1 = self.soup.find(
                "span",
                {
                    "class": "wprm-recipe-details wprm-recipe-details-hours wprm-recipe-total_time wprm-recipe-total_time-hours"
                },
            ).get_text()
        except Exception:
            tt1 = 0
        tt2 = self.soup.find(
            "span",
            {
                "class": "wprm-recipe-details wprm-recipe-details-minutes wprm-recipe-total_time wprm-recipe-total_time-minutes"
            },
        ).get_text()
        if tt1:
            tt3 = (int(tt1) * 60) + int(tt2)
            tt2 = get_minutes(tt3)
            if tt3 and (tt2 == 0):
                total_time = tt3
            else:
                total_time = tt2
        elif tt2:
            total_time = tt2
        return total_time

    def yields(self):
        recipe_yield = self.soup.find(
            "div",
            {
                "class": "wprm-recipe-servings-container wprm-recipe-block-container wprm-recipe-block-container-inline wprm-block-text-normal"
            },
        ).get_text()
        if "Servings:" in recipe_yield:
            ry = normalize_string(recipe_yield[9:])
        return ry

    def image(self):
        image = self.soup.find(
            "div", {"class": "wprm-recipe-image wprm-block-image-normal"}
        )  # , 'src': True})
        img = image.find(
            "img", {"class": "attachment-200x200 size-200x200", "src": True}
        )
        issrc = img["src"]
        return issrc if image else None

    def ingredients(self):
        ingredientsOuter = self.soup.findAll(
            "div", {"class": "wprm-recipe-ingredient-group"}
        )

        ingGroup = []
        for ig in ingredientsOuter:
            try:
                header = ig.find(
                    "h4",
                    {
                        "class": "wprm-recipe-group-name wprm-recipe-ingredient-group-name wprm-block-text-bold"
                    },
                ).text
            except Exception:
                header = None
            if header is not None:
                ingGroup.append(header)
            ingredparts = ig.findAll("li")
            for i in ingredparts:
                x = normalize_string(i.get_text())
                ingGroup.append(x)
        return ingGroup

    def _instructions_list(self):
        instructions = self.soup.findAll(
            "div", {"class": "wprm-recipe-instruction-group"}
        )
        data = []
        if len(instructions):
            for instruct in instructions:
                try:
                    header = instruct.find(
                        "h4",
                        {
                            "class": "wprm-recipe-group-name wprm-recipe-instruction-group-name wprm-block-text-bold"
                        },
                    ).text
                except Exception:
                    header = None
                if header is not None:
                    data.append(header)
                ins = instruct.findAll("div", {"class": "wprm-recipe-instruction-text"})

                data.append("\n".join([normalize_string(inst.text) for inst in ins]))
            return data
        return None

    def instructions(self):
        data = self._instructions_list()
        return "\n".join(data) if data else None

    def ratings(self):
        try:
            found = self.soup.find("div", {"class": "wprm-recipe-rating"})
            stars = found.findAll(
                "span",
                attrs={
                    "class": lambda e: e.endswith("wprm-rating-star-full")
                    if e
                    else False
                },
            )
        except Exception:
            stars = []
        return round(float(len(stars)), 2) if stars else None

    def description(self):
        d = normalize_string(self.soup.find("span", {"style": "display: block;"}).text)
        return d if d else None
