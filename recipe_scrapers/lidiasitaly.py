from ._abstract import AbstractScraper
from ._utils import get_yields


class LidiasItaly(AbstractScraper):
    @classmethod
    def host(cls):
        return "lidiasitaly.com"

    def author(self):
        return "LIDIA'S RESTAURANT"

    def title(self):
        return self.soup.select_one(".print[data-name]")["data-name"].strip()

    def image(self):
        el = self.soup.select_one(".recipe-image")
        if el and el.has_attr("style"):
            return el["style"].split("url(")[-1].split(")")[0].strip(" '\"")

    def ingredients(self):
        return [
            li.get_text(strip=True)
            for li in self.soup.select(".box-ingredients ul li")
            if "category" not in li.get("class", [])
        ]

    def instructions(self):
        ps = self.soup.select(".box-directions .recipe-text p")
        return "\n".join(p.get_text(strip=True) for p in ps)

    def yields(self):
        servings_text = self.soup.select_one("h3.servings")
        if servings_text:
            return get_yields(servings_text.get_text(strip=True))
