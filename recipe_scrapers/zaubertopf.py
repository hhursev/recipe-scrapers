# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class ZauberTopf(AbstractScraper):
    @classmethod
    def host(cls):
        return "zaubertopf.de"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        for h2_element in self.soup.find_all("h2"):
            if "Die Zutaten" in h2_element.text:
                ul_element = h2_element.find_next("ul")
                if ul_element:
                    return [
                        normalize_string(li.text)
                        for li in ul_element.find_all("li")
                        if li.text
                    ]

    def instructions(self):
        for h2_element in self.soup.find_all("h2"):
            if "Die Zubereitung" in h2_element.text:
                ol_element = h2_element.find_next("ol")
                if ol_element:
                    return "\n".join(
                        [li.get_text() for li in ol_element.find_all("li") if li.text]
                    )

    def description(self):
        return self.schema.description()
