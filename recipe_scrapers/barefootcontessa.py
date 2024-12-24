from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class BareFootContessa(AbstractScraper):
    @classmethod
    def host(cls):
        return "barefootcontessa.com"

    def author(self):
        return "Ina Garten"

    def ingredients(self):
        ingredient_list = []
        ingredient_divs = self.soup.find_all("div", {"class": "mb-10"})

        for div in ingredient_divs:
            ul = div.find("ul", {"class": "h29"})
            if ul:
                ingredients = ul.find_all("li")
                ingredient_list.extend([item.text for item in ingredients])

        return ingredient_list

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".mb-10 p",
            ".mb-10 li",
        )

    def instructions(self):
        instructions = []
        instruction_divs = self.soup.find_all(
            "div", {"class": "bd4 mb-10 EntryPost__text a-bc-blue"}
        )

        for div in instruction_divs:
            instruction_paragraphs = div.find_all("p")
            for paragraph in instruction_paragraphs:
                if paragraph is not None:
                    paragraph_text = normalize_string(paragraph.text)
                    instructions.append(paragraph_text)

        return "\n".join(instructions)
