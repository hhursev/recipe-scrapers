from ._abstract import AbstractScraper
from ._utils import normalize_string
import re


class WDR(AbstractScraper):
    @classmethod
    def host(cls):
        return "www1.wdr.de"

    def site_name(self):
        return "WDR"

    def title(self):
        return self.soup.find("meta", property="og:title")["content"]

    def ingredients(self):
        header = self.soup.find("h2", string=re.compile(r"^Zutaten.*"))

        # find <li> siblings until the next <h2> tag:
        ingredients = []
        for sibling in header.find_next_siblings(name=True):
            if sibling.name == "h2":
                break
            items = sibling.find_all("li")
            if len(items) > 0:
                ingredients.extend([normalize_string(li.get_text()) for li in items])
        return ingredients

    def image(self):
        return f'https://{self.host()}{self.soup.find("picture").find_next(name="source")["srcset"]}'

    def instructions(self) -> str:
        header = self.soup.find("h2", string="Zubereitung")
        # Some recipes have the instructions in <li> tags, others in <p> tags
        return "\n".join(
            [
                normalize_string(li.get_text())
                for li in header.find_next_sibling(name=True).find_all("li")
            ]
            + [
                normalize_string(p.get_text())
                for p in header.find_next_siblings(name="p")
            ]
        )

    def description(self):
        return self.soup.find("meta", {"name": "Description"})["content"]
