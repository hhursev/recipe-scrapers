import re
from ._abstract import AbstractScraper
from ._utils import normalize_string


class PaulaDeen(AbstractScraper):
    @classmethod
    def host(cls):
        return "pauladeen.com"

    def __init__(self, html, url, best_image=None):
        # Fix invalid JSON-LD by removing the trailing semicolon before the closing script tag
        html = re.sub(r"};\s*</script>", "}</script>", html)
        super().__init__(html, url, best_image)

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        # The JSON-LD description is often empty, so we use
        # the HTML content found in the 'full-description' div.
        if element := self.soup.find("div", {"class": "full-description"}):
            return normalize_string(element.get_text())

        return self.schema.description()
