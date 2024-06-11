# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class DonnaHay(AbstractScraper):
    @classmethod
    def host(cls):
        return "donnahay.com.au"

    def author(self):
        return self.schema.author()

    def title(self):
        return (
            self.soup.find("h1", class_="text-center recipe-title__mobile")
            .getText()
            .upper()
        )

    def yields(self):
        div = self.soup.find("div", class_="col-sm-6 method")
        return div.find("b").getText()

    def image(self):
        div = self.soup.find("div", class_="image-frame recipes")
        if not div:
            return
        image = div.find("img")
        return image["src"]

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        div = self.soup.find("div", class_="col-sm-6 method")
        if not div:
            return
        instructions = div.find_all("li")
        for instruction in instructions:
            text = instruction.get_text(separator=" ", strip=True)
            if "Serves" in text:
                text = text.split("Serves", 1)[
                    0
                ].strip()  # Remove the sentence starting with Serves
            instruction.string = text
        return instructions

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def keywords(self):
        div = self.soup.find("div", class_="section text-left")
        tags = div.find_all("a")
        keywords = []
        for tag in tags:
            keywords.append(tag.getText())
        return keywords
