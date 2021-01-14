from ._abstract import AbstractScraper

from ._utils import normalize_string, get_yields


class DomoweWypieki(AbstractScraper):
    @classmethod
    def host(cls):
        return "domowe-wypieki.pl"

    def author(self):
        return None

    def title(self):
        header = self.soup.find("div", {"class": "page-header"})
        if not header:
            return None

        return normalize_string(header.get_text())

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.schema.yields())

    def image(self):
        image = self.soup.find("img", {"id": "article-img-1", "data-src": True})
        return image["data-src"] if image else None

    def ingredients(self):
        containers = self.soup.find("div", {"id": "recipe-ingredients"})
        ingredients = []

        if not containers:
            return ingredients

        for container in containers:
            if container.name == "p":
                ingredients.append(container.get_text())
            elif container.name == 'ul':
                ingredients_part = container.findAll("li")
                ingredients = ingredients + [ingredient.get_text() for ingredient in ingredients_part]
            else:
                continue

        return [normalize_string(ingredient) for ingredient in ingredients]

    def instructions(self):
        container = self.soup.find("div", {"id": "recipe-instructions"})
        if not container:
            return None

        instructions = []
        parts = container.findAll("ol")
        for part in parts:
            instructions = instructions + [normalize_string(item.get_text()) for item in part.findAll("li")]

        return "\n".join(instructions)

    def description(self):
        container = self.soup.find("div", {"id": "recipe-description"})
        if not container:
            return None

        parts = [normalize_string(part.get_text()) for part in container.findAll("p")]
        return "\n".join(parts)
