from ._abstract import AbstractScraper
from ._utils import normalize_string


class LekkerEnSimpel(AbstractScraper):
    @classmethod
    def host(cls):
        return "lekkerensimpel.com"

    def author(self):
        return self.schema.author()

    def title(self):
        title = self.soup.find("h1", {"class": "hero__title"}).text
        return normalize_string(title)

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        image = self.soup.find("meta", {"property", "og:image"})
        return image["content"] if image else None

    def ingredients(self):
        ingredients = self.soup.find("div", {"class": "recipe__necessities"}).find_all(
            "li"
        )
        return [normalize_string(i.get_text()) for i in ingredients]

    def instructions(self):
        instructions = self.soup.find("div", {"class": "entry__content"}).find_all("p")
        return "\n".join(
            [normalize_string(i.get_text()) for i in instructions]
            if instructions
            else None
        )

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        description = self.soup.find("div", {"class": "entry__content"}).find("p").text
        return normalize_string(description) if description else None

    def language(self):
        return "nl-NL"
