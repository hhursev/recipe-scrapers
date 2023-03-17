from urllib.parse import unquote

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class SallysBlog(AbstractScraper):
    @classmethod
    def host(cls):
        return "sallys-blog.de"

    def title(self):
        return normalize_string(self.soup.head.find("title").get_text())

    def image(self):
        image_element = self.soup.find("div", {"class": "images-wrap"}).findAll(
            "img", {"sizes": "100vw"}
        )[0]
        image_src = image_element["src"]
        image_url = unquote(image_src).split("url=")[1].split("&")[0]
        return image_url

    def total_time(self):
        heading = self.soup.find("p", string="Zubereitungszeit")
        timing = heading.find_next_sibling("h6")
        return get_minutes(timing.text)

    def _servings_heading(self):
        return self.soup.find("h4", string="Zutaten für:")

    def yields(self):
        servings_heading = self._servings_heading()
        servings = servings_heading.find_next_sibling("div").find("input")
        return servings["value"]

    def _groupings(self):
        servings_heading = self._servings_heading()
        ingredients_area = servings_heading.next_sibling.next_sibling
        return ingredients_area.find_all("div", recursive=False)

    def ingredients(self):
        descriptions = []
        for grouping in self._groupings():
            ingredients = grouping.find_all("div", recursive=False)
            for ingredient in ingredients:
                descriptions.append(ingredient.text)

        return [normalize_string(description) for description in descriptions]

    def instructions(self):
        grouping_titles = {grouping.find("h5").text for grouping in self._groupings()}
        uppercase_titles = self.soup.find_all("h2", {"class": "uppercase"})

        descriptions = []
        for title in uppercase_titles:
            if title.text in grouping_titles or title.text.endswith("fertigstellen"):
                instructions = title.find_next_sibling("div").find_all("p")
                for instruction in instructions:
                    descriptions.append(instruction.text)

        return "\n".join(
            [normalize_string(description) for description in descriptions]
        )
