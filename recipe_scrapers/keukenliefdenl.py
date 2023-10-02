# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
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
        return get_minutes(
            self.soup.find("div", {"class": "article-meta-item sp tijd"}).get_text()
        )

    def yields(self):
        yields = self.soup.find("div", {"class": "article-meta-item sp aantal"})
        if yields:
            return get_yields(yields.get_text())

        return None

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"id": "clipboard-ingredients"}
        ).findChildren("li")

        return [normalize_string(i.get_text()) for i in ingredients]

    def instructions(self):
        # Old recipes are written in paragraphs, new ones are a list.
        paragraphs = self.soup.find("div", {"class": "preparation"}).find_all("p")
        listitems = self.soup.find("div", {"class": "preparation"}).find_all("li")

        instructions = [
            normalize_string(item.get_text())
            for item in paragraphs + listitems
            if item.get_text()
        ]

        return "\n".join(instructions)

    def description(self):
        return self.soup.find("meta", {"name": "description"}).get("content")
