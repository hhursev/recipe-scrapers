from ._abstract import AbstractScraper
from ._exceptions import StaticValueException


class Kochbucher(AbstractScraper):
    @classmethod
    def host(cls):
        return "kochbucher.com"

    def site_name(self):
        raise StaticValueException(return_value="Kochbucher")

    def title(self):
        return self.soup.find("h1", {"class": "post-title entry-title left"}).get_text()

    def category(self):
        category_element = self.soup.find("span", {"class": "post-head-cat"})
        if category_element is not None:
            return category_element.get_text()

    def author(self):
        author_element = self.soup.find(
            "span", {"class": "author-name vcard fn author"}
        )
        if author_element is not None:
            return author_element.get_text()

    def ingredients(self):
        zutaten_heading = self.soup.find("p", string="Zutaten")
        if zutaten_heading is not None:
            next_p_element = zutaten_heading.find_next("p")
            if next_p_element is not None:
                ingredients_list = next_p_element.get_text().split("\n")
                ingredients_list = [
                    ingredient.strip()
                    for ingredient in ingredients_list
                    if ingredient.strip()
                ]
                return ingredients_list

    def instructions(self):
        zubereitung_heading = self.soup.find("p", string="Zubereitung")
        if zubereitung_heading is not None:
            next_p_element = zubereitung_heading.find_next("p")
            if next_p_element is not None:
                raw_instructions = next_p_element.get_text().replace("– ", "")
                if isinstance(raw_instructions, str):
                    instructions_list = raw_instructions.split("\n")
                    return "\n".join(filter(None, instructions_list))
