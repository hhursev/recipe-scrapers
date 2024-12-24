import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml


class Valdemarsro(AbstractScraper):
    @classmethod
    def host(cls):
        return "valdemarsro.dk"

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

    def instructions(self):
        instruction_elements = self.soup.find(
            "div", {"itemprop": "recipeInstructions"}
        ).find_all("p")

        instructions_list = [tag.get_text() for tag in instruction_elements]

        return "\n".join(instructions_list)

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
