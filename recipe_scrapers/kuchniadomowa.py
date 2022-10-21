# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback


class KuchniaDomowa(AbstractScraper):
    @classmethod
    def host(cls):
        return "kuchnia-domowa.pl"

    def title(self):
        return self.soup.find("h2").get_text().strip()

    @schemaorg_fallback
    def total_time(self):
        pass

    @schemaorg_fallback
    def yields(self):
        pass

    @opengraph_fallback
    def image(self):
        urls = self.soup.findAll("img", {"class": "article-img", "id": "article-img-1"})
        return f"https:{urls[1]['src']}"

    @schemaorg_fallback
    def ingredients(self):
        pass

    def instructions(self):
        instructions = self.soup.find("div", {"id": "recipe-instructions"}).findAll(
            "li"
        )
        instructions = [x.text for x in instructions]
        return "\n".join(instructions)
