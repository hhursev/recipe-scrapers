from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class TineNo(AbstractScraper):
    @classmethod
    def host(cls):
        return "tine.no"

    def title(self):
        return self.soup.find("h1").get_text()

    def total_time(self):
        total_time = 0
        tt1 = self.soup.find("li", {"class": "m-recipe-overview__total-time"})
        if tt1:
            tt = tt1.find("span", {"class": "t-info"})
            tt1 = normalize_string(tt.get_text())
            tt2 = get_minutes(tt1)
            if tt1 and (tt2 == 0):
                total_time = tt1
            else:
                total_time = tt2
        return total_time

    def yields(self):
        recipe_yield = self.soup.find("input", {"id": "portions"})
        if recipe_yield:
            return recipe_yield["value"]
        else:
            return get_yields(
                self.soup.find(
                    "div", {"class": "recipe-adjust-servings__original-serving"}
                ).get_text()
            )

    def image(self):
        image = self.soup.find("img", {"id": "HeaderMediaContent"})
        if image:
            # tag = image.find('src')
            src = image.get("src", None)

        return src if image else None

    def ingredients(self):
        # site uses <section><section>...</section></section>
        ingredientsOuter = self.soup.findAll(
            "div", {"id": "ingredient-groups-container"}
        )
        ingGroup = []
        ingredients1 = ingredientsOuter[0].findAll("section")
        for ings in ingredients1:
            ingredients = ings.findAll("section")
            for ingredient in ingredients:
                if len(ingredient) > 1:
                    try:
                        header = ingredient.find(
                            "h3",
                            {
                                "class": "t-tertiary-heading o-recipe-ingredients__sub-title"
                            },
                        ).get_text()
                    except Exception:
                        header = ""
                    tablelines = ingredient.findAll("td")
                    lst = []
                    cntr = 0
                    tmplst = []
                    for item in tablelines:
                        tmplst.append(normalize_string(item.get_text(strip=True)))
                        cntr += 1
                        if cntr % 2 == 0:
                            lst.append(" ".join(tmplst))
                            tmplst = []
                    if header != "":
                        ingGroup.append(header)
                    ingGroup += lst
        return ingGroup

    def instructions(self):
        instructions = self.soup.find("ol", {"class": "o-recipe-steps__step-groups"})

        ins = instructions.findAll("li", {"class": "o-recipe-steps__step-group"})

        return "\n".join([normalize_string(inst.text) for inst in ins])

    def description(self):
        d = normalize_string(
            self.soup.find(
                "div",
                {
                    "class": "t-ingress m-page-ingress m-page-ingress--recipe l-recipe__ingress"
                },
            ).text
        )

        return d if d else None
