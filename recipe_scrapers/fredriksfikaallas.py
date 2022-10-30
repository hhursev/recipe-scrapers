# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper


class FredriksFikaAllas(AbstractScraper):
    @classmethod
    def host(cls):
        return "fredriksfika.allas.se"

    def title(self):
        return self.soup.find("h1").get_text()

    def category(self):
        return self.soup.find("div", {"class": "post_category"}).get_text()

    def image(self):
        return self.soup.find("meta", {"property": "og:image", "content": True}).get(
            "content"
        )

    def ingredients(self):
        ingredients = []
        content = self.soup.find("strong", string=re.compile("Ingredienser"))
        contentRows = str(content.parent).split("<br/>")

        for i in contentRows:
            if "Ingredienser" not in i:
                ingredients.append(i.replace("\r", "").replace("Gör så här:", ""))
            if "Gör så här" in i:
                break

        return ingredients

    def instructions(self):
        instructions = []
        content = self.soup.find("strong", string=re.compile("Gör så här"))

        contentRows = str(content.parent).split("<br/>")

        fillData = False
        for i in contentRows:
            if fillData:
                instructions.append(i.replace("\r", ""))
            if "Gör så här" in i:
                fillData = True

        return "\n".join(instructions)
