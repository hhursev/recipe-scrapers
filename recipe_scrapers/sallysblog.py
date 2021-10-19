from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class SallysBlog(AbstractScraper):
    @classmethod
    def host(cls):
        return "sallys-blog.de"

    def title(self):
        return normalize_string(
            self.soup.find("h1", {"class": "blog--detail-headline"}).get_text()
        )

    def total_time(self):
        return get_minutes(self.soup.find("span", {"id": "zubereitungszeit"}))

    def yields(self):
        amount = self.soup.find("input", {"class": "float-left"}).get("value")
        unit = self.soup.find("span", {"id": "is_singular"}).get_text()

        return f"{amount} {unit}"

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "quantity"})

        return [normalize_string(i.get_text()) for i in ingredients]

    def instructions(self):
        instructionBlock = self.soup.find(
            "div", {"class": "blog--detail-description block"}
        )
        instructions = instructionBlock.findAll(
            "div", {"class": ["content_type_2", "content_type_3", "content_type_4"]}
        )

        return "\n".join(
            [
                normalize_string(instruction.find("p").get_text())
                for instruction in instructions
            ]
        )
