from ._abstract import AbstractScraper
import re


class RussianFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "russianfood.com"

    def title(self):
        return self.soup.find("h1").get_text().strip()

    def ingredients(self):
        ingr_table = self.soup.find("table", {"class": "ingr"})
        if not ingr_table:
            return []
        rows = ingr_table.find_all("tr", {"class": re.compile(r"ingr_tr_\d+")})
        result = []
        for row in rows:
            text = row.get_text(" ", strip=True)
            if text and text != "*":
                result.append(text)
        return result

    def instructions(self):
        steps = self.soup.find_all("div", {"class": "step_n"})
        result = []
        for step in steps:
            p = step.find("p")
            if p:
                text = p.get_text(strip=True)
                if text:
                    result.append(text)
        return "\n".join(result)

    def image(self):
        og_image = self.soup.find("meta", {"property": "og:image"})
        if og_image:
            return og_image.get("content")
        return None