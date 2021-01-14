from ._abstract import AbstractScraper

from ._utils import normalize_string, get_yields


class KwestiaSmaku(AbstractScraper):
    @classmethod
    def host(cls):
        return 'kwestiasmaku.com'

    def title(self):
        return self.schema.title()

    def yields(self):
        return get_yields(
            self.soup.find(
                "div", {"class": "field field-name-field-ilosc-porcji field-type-text field-label-hidden"}
            ).get_text()
        )

    def image(self):
        container = self.soup.find("div", {
            "class": "field field-name-zdjecie-z-linikem-do-bloga field-type-ds field-label-hidden"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self):
        containers = self.soup.find("div", {
            "class": "field field-name-field-skladniki field-type-text-long field-label-hidden"})

        ingredients = []

        if not containers:
            return ingredients

        for container in containers:
            if container.name == "div":
                ingredients.append(container.get_text())
            elif container.name == 'ul':
                ingredients_part = container.findAll("li")
                ingredients = ingredients + [ingredient.get_text() for ingredient in ingredients_part]
            else:
                continue

        return [normalize_string(ingredient) for ingredient in ingredients]

    def instructions(self):
        containers = self.soup.find("div", {
            "class": "field field-name-field-przygotowanie field-type-text-long field-label-above"})

        instructions = []

        if not containers:
            return None

        for container in containers:
            if container.name == "div":
                instructions.append(container.get_text())
            elif container.name == 'ul':
                instructions_part = container.findAll("li")
                instructions = instructions + [ingredient.get_text() for ingredient in instructions_part]
            else:
                continue

        return "\n".join([normalize_string(instruction) for instruction in instructions])

    def ratings(self):
        return self.schema.ratings()

    def description(self):
        d = normalize_string(
            self.soup.find("div", {
                "class": "field field-name-field-uwagi-wstepne field-type-text-long field-label-hidden"}).get_text()
        )
        return d if d else None
