import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._utils import normalize_string


class Valdemarsro(AbstractScraper):
    @classmethod
    def host(cls):
        return "valdemarsro.dk"

    def title(self):
        return self.soup.h1.get_text().strip()

    def category(self):
        category_group_element = self.soup.find("div", {"class": "recipe-bar"})

        categories = [
            a.get_text()
            for a in category_group_element.find_all(
                lambda a: "/tag/" not in a.attrs["href"]
            )
        ]
        return ",".join(categories)

    def get_time(self, label):
        metadata_group_element = self.soup.findAll(
            "span", {"class": "recipe-stat-label"}
        )
        time_label_element = next(
            filter(lambda x: label in x.getText(), metadata_group_element), None
        )
        time_text_element = time_label_element.parent.find("strong")
        time_text = time_text_element.getText()

        matched = re.search(
            r"((?P<hours>\d+) timer?\s*)?((?P<minutes>\d+)\s*min.)?", time_text
        )

        minutes = int(matched.groupdict().get("minutes") or 0)
        minutes += 60 * int(matched.groupdict().get("hours") or 0)

        if minutes > 0:
            return minutes
        else:
            raise ElementNotFoundInHtml(label)

    def total_time(self):
        return self.get_time("Tid i alt")

    def cook_time(self):
        return self.get_time("Arbejdstid")

    def yields(self):
        yields_element = self.soup.find("i", {"class": "fa-sort"}).parent
        yields_text = yields_element.getText().strip()
        return yields_text

    def image(self):
        parent_element = self.soup.find("div", {"class": "recipe-image"})
        image_element = parent_element.find(lambda x: not x.has_attr("class"))
        image_url = image_element["src"]
        return image_url

    def ingredients(self):
        ingredient_elements = self.soup.find_all("li", {"itemprop": "recipeIngredient"})

        return [
            normalize_string(paragraph.get_text().strip())
            for paragraph in ingredient_elements
        ]

    def instructions(self):
        instruction_elements = self.soup.find(
            "div", {"itemprop": "recipeInstructions"}
        ).find_all("p")

        instructions_list = [tag.get_text() for tag in instruction_elements]

        return "\n".join(instructions_list)

    def author(self):
        return "Ann-Christine Hellerup Brandt"

    def description(self):
        description_element = self.soup.find("div", {"itemprop": "description"})

        description_paragraph_elements = description_element.find_all(
            lambda tag: tag.name == "p" and " også:" not in tag.get_text(),
            recursive=False,
        )

        description_paragraphs = [
            p.get_text().strip() for p in description_paragraph_elements
        ]

        description = "\n".join(description_paragraphs)

        return description
