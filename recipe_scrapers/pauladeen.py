import re
from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._schemaorg import SchemaOrg


class PaulaDeen(AbstractScraper):
    class _CustomSchemaOrg(SchemaOrg):
        def __init__(self, page_data):
            # Fix invalid JSON-LD by removing the trailing semicolon before the closing script tag
            page_data = re.sub(r"};\s*</script>", "}</script>", page_data)
            super().__init__(page_data)

    _schema_cls = _CustomSchemaOrg

    @classmethod
    def host(cls):
        return "pauladeen.com"

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
        paragraphs = self.soup.select("section.directions .directions__content p")
        steps = [
            normalize_string(p.get_text()) for p in paragraphs if p.get_text(strip=True)
        ]
        return "\n".join(steps)

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
