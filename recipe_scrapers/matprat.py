from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class Matprat(AbstractScraper):
    @classmethod
    def host(cls):
        return "matprat.no"

    def title(self):
        return self.soup.find("h1").get_text().strip()

    def total_time(self):
        total_time = 0
        tt = self.soup.find("span", {"data-epi-property-name": "RecipeTime"})
        if tt:
            tt1 = normalize_string(tt.get_text())
            tt2 = get_minutes(tt1)
            if tt1 and (tt2 == 0):
                total_time = tt1
            else:
                total_time = tt2
        return total_time

    def yields(self):
        recipe_yield = self.soup.find("input", {"id": "portionsInput"})
        if recipe_yield:
            return str(recipe_yield["value"]) + " serving(s)"
        else:
            return get_yields(
                self.soup.find(
                    "div", {"class": "recipe-adjust-servings__original-serving"}
                ).get_text()
            )

    def image(self):
        image = self.soup.find("div", {"class": "responsive-image"})
        if image:
            tag = image.find("img")
            src = tag.get("src", None)
        return src if image else None

    def ingredients(self):
        details = self.soup.find("div", {"class": "ingredients-list"})
        sections = details.findAll("h3", {"class": "ingredient-section-title"})
        ingredients = details.findAll("ul", {"class": "ingredientsList"})

        cntr = 0
        ilist = []
        for ingpart in ingredients:
            ingreditem = ingpart.findAll("li")
            for i in ingreditem:
                ilist.append(normalize_string(i.get_text()))
            if cntr <= (len(sections) - 1):
                if len(sections[cntr].text) > 0:
                    # txt = f'--- {sections[cntr].text} ---'
                    txt = "--- {0} ---".format(sections[cntr].text)
                    ilist.append(txt)
            cntr += 1
        return ilist

    def instructions(self):
        instructions = self.soup.find("div", {"class": "rich-text"})
        ins = instructions.findAll("li")

        return "\n".join([normalize_string(inst.text) for inst in ins])

    def ratings(self):
        r = self.soup.find("span", {"data-bind": "text: numberOfVotes"})
        return int(normalize_string(r.get_text()))

    def description(self):
        return normalize_string(self.soup.find("div", {"class": "article-intro"}).text)
