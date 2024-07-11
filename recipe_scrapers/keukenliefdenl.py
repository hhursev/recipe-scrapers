from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._utils import get_minutes, get_yields, normalize_string


class KeukenLiefdeNL(AbstractScraper):
    @classmethod
    def host(cls):
        return "keukenliefde.nl"

    def author(self):
        return self.soup.find("meta", {"name": "author"}).get("content")

    def title(self):
        return self.soup.find("meta", {"property": "og:title"}).get("content")

    def category(self):
        return self.soup.find(
            "div", {"class": "article-meta-item sp gerecht"}
        ).getText()

    def total_time(self):
        time = self.soup.find("div", {"class": "article-meta-item sp tijd"})
        if time:
            return get_minutes(time.get_text())

        return None

    def yields(self):
        yields = self.soup.find("div", {"class": "article-meta-item sp aantal"})
        if yields:
            return get_yields(yields.get_text())

        return None

    def ingredients(self):
        ingredents_container = self.soup.find("div", {"id": "clipboard-ingredients"})
        if ingredents_container:
            return self.process_ingredients(ingredents_container)

        ingredient_header = self.soup.find("strong", string="Ingrediënten")
        if ingredient_header:
            return self.process_ingredients(
                ingredient_header.parent.find_next_sibling("ul")
            )

        # Nothing found, we give up.
        raise ElementNotFoundInHtml("Could not find ingredients.")

    def process_ingredients(self, container):
        ingredients = container.findChildren("li")

        return [normalize_string(i.get_text()) for i in ingredients]

    def instructions(self):
        # Old recipes are written in paragraphs, new ones are a list.
        preparation = self.soup.find("div", {"class": "preparation"})
        if preparation:
            return self.normalize_instructions(
                preparation.find_all("p") + preparation.find_all("li")
            )

        # There are some really old recipes that do not have the nice classes
        instructions_heading = self.soup.find("strong", string="Bereiding")
        if instructions_heading:
            # We are doing some assumptions here
            return self.normalize_instructions(
                [instructions_heading.parent]
                + instructions_heading.parent.find_next_siblings("p")
            )

        raise ElementNotFoundInHtml("Could not find instructions.")

    def normalize_instructions(self, instructions):
        instructions = [
            normalize_string(item.get_text())
            for item in instructions
            if normalize_string(item.get_text())
        ]

        return "\n".join(instructions)

    def description(self):
        return self.soup.find("meta", {"name": "description"}).get("content")
