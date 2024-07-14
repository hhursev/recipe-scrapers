from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import normalize_string


class Costco(AbstractScraper):
    @classmethod
    def host(cls):
        return "costco.com"

    def author(self):
        return "Costco Connection"

    def site_name(self):
        raise StaticValueException(return_value="Costco")

    def title(self):
        return self.soup.find("h1", style="font-size: 2.5em;").get_text()

    def ingredients(self):
        parent_div = self.soup.find("div", {"class": "col-xs-12 col-md-5"})
        if parent_div:
            parent_ul = parent_div.find("ul")
            if parent_ul:
                ingredients_list_items = parent_ul.find_all("li")
                ingredients_list = [
                    normalize_string(li.get_text()) for li in ingredients_list_items
                ]
                return ingredients_list

    def instructions(self):
        parent_div = self.soup.find("div", {"class": "col-xs-12 col-md-5"})
        if parent_div:
            instructions_paragraphs = parent_div.find_all("p")
            instructions = [
                normalize_string(p.get_text())
                for p in instructions_paragraphs
                if p.get_text()
            ]
            return "\n".join(instructions)

    def image(self):
        parent_div = self.soup.find("div", {"class": "col-xs-12 col-md-6"})
        if parent_div:
            image_tag = parent_div.find("img")
            if image_tag and "src" in image_tag.attrs:
                return image_tag["src"]
