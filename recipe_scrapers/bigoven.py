from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class BigOven(AbstractScraper):
    @classmethod
    def host(cls):
        return "bigoven.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "yield"}).text)

    def image(self):
        return self.schema.image()

    def ingredients(self):
        rows = self.soup.find("ul", {"class": "ingredients-list"}).findAll("li")
        return [
            normalize_string(row.span.text)
            for row in rows
            if "ingHeading" not in row.span["class"]
        ]

    def instructions(self):
        ps = self.soup.find("div", {"class": "instructions"}).findAll("p")
        return "\n".join([normalize_string(p.text) for p in ps])

    def ratings(self):
        try:
            cnt = (
                self.soup.find("div", {"class": "recipe-rating"})
                .find("span", {"class": "count"})
                .text
            )
            rating = (
                self.soup.find("div", {"class": "recipe-rating"})
                .find("span", {"class": "rating"})
                .text
            )
            return {"count": int(cnt), "rating": round(float(rating), 2)}
        except Exception:
            return None
