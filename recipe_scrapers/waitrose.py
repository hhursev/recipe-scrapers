from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import normalize_string


class Waitrose(AbstractScraper):
    @classmethod
    def host(cls):
        return "waitrose.com"

    def author(self):
        raise StaticValueException(return_value="Waitrose")

    def site_name(self):
        logo = next(iter(self.soup.select("div.logo")), None)
        if not logo:
            raise StaticValueException(return_value="Waitrose")
        if home_link := logo.find("a", {"href": "/"}):
            return home_link.text

    def ingredients(self):
        ingredient_items = self.soup.select("[data-testid='ingredients'] li")
        if ingredient_items:
            ingredient_text = [
                normalize_string(item.get_text())
                for item in ingredient_items
                if item.get_text()
            ]
            return ingredient_text

    def instructions(self):
        instruction_items = self.soup.select("[data-test='method'] li")

        if instruction_items:
            instruction_text = []
            for item in instruction_items:
                line = item.get_text()
                lower = line.lower().strip()
                if not lower or (lower.startswith("step ") and lower[5:].isdigit()):
                    continue
                instruction_text.append(normalize_string(line))
            return "\n".join(instruction_text)
