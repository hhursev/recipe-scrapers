from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class Cucchiaio(AbstractScraper):
    @classmethod
    def host(cls):
        return "cucchiaio.it"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        time = self.soup.find("div", {"class": "sintesi sx"})
        if time:
            time = get_minutes(time.get_text())
        return time

    def yields(self):
        header = self.soup.find("td", text="PORZIONI")
        if header:
            value = header.find_next("td")
            return get_yields(value)
        return None

    def image(self):
        data = self.soup.find("div", {"class": "auto"}).find("img", {"class": "image"})
        if data:
            data = data.get("src")
        return data

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return None
