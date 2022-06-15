import re

from ._abstract import AbstractScraper


class FredriksFikaAllas(AbstractScraper):
    @classmethod
    def host(cls):
        return "fredriksfika.allas.se"

    def author(self):
        author = self.soup.find("div", {"class": "c-post_author__name"}).get_text()
        return author.replace("Av:", "").strip()

    def title(self):
        return self.soup.find("div", {"class": "c-post_title"}).get_text()

    def category(self):
        return (
            self.soup.find("div", {"class": "c-post_author__category"})
            .get_text()
            .replace("i ", "")
            .strip()
        )

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = []
        content = self.soup.find("strong", text=re.compile("Ingredienser"))

        contentRows = content.parent.text.split("\n")

        for i in contentRows:
            if "Ingredienser" not in i:
                ingredients.append(i.replace("\r", "").replace("Gör så här:", ""))
            if "Gör så här" in i:
                break

        return ingredients

    def instructions(self):
        instructions = []
        content = self.soup.find("strong", text=re.compile("Gör så här"))

        contentRows = content.parent.text.split("\n")

        fillData = False
        for i in contentRows:
            if fillData:
                instructions.append(i.replace("\r", ""))
            if "Gör så här" in i:
                fillData = True

        return "\n".join(instructions)
