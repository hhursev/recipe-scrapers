from ._abstract import AbstractScraper

from ._utils import normalize_string, get_yields


class Smaker(AbstractScraper):
    @classmethod
    def host(cls):
        return "smaker.pl"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.schema.yields())

    def image(self):
        image = self.soup.find("div", {"class": "image_wrap"}).find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        container = self.soup.find("ol", {"class": "preparation"})
        if not container:
            return None

        instructions = []

        items = self.soup.findAll("li", {"itemprop": "itemListElement"})
        for item in items:
            instruction = item.find("p", {"itemprop": "itemListElement"})
            if not instruction:
                continue
            instructions.append(normalize_string(instruction.get_text()))

        return "\n".join(instructions)

    def description(self):
        d = normalize_string(self.soup.find("div", {"class": "userDescriptionHint"}).get_text())
        return d if d else None
