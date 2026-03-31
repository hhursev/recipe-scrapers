from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_minutes, get_yields


class DonalSkehan(AbstractScraper):
    @classmethod
    def host(cls):
        return "donalskehan.com"

    def author(self):
        image_element = self.soup.find("img", class_="img-fluid")
        return image_element.get("alt")

    def site_name(self):
        raise StaticValueException(return_value="Donal Skehan")

    def title(self):
        return self.soup.find("title").get_text()

    def category(self):
        return self.soup.find("h6", class_="catColour dk-label").get_text()

    def total_time(self):
        recipe_data = self.soup.find_all("li", class_="list-inline-item mb-2")
        for element in recipe_data:
            if element.find("img", alt="time"):
                return get_minutes(element.get_text())

    def yields(self):
        recipe_data = self.soup.find_all("li", class_="list-inline-item mb-2")
        for element in recipe_data:
            if "serves" in element.text.lower():
                return get_yields(element.text)

    def image(self):
        image_element = self.soup.find("img", class_="img-fluid shadow")
        return image_element["src"]

    def ingredients(self):
        ingredients_section = self.soup.find(
            "div", class_="tab-pane fade show active", id="metric"
        )
        return [
            ingredient.get_text().strip()
            for ingredient in ingredients_section.find_all("p")
        ]

    def instructions(self):
        instructions_section = self.soup.find(
            "div", class_="recipe steps container-fluid"
        )
        return "\n".join(
            step.get_text().strip()
            for step in instructions_section.find_all("li", class_="list-group-item")
        )

    def keywords(self):
        keywords_section = self.soup.find("ul", id="tag")
        return [
            keyword.get_text().strip()
            for keyword in keywords_section.find_all(
                "li", class_="list-inline-item mb-2"
            )
        ]

    def equipment(self):
        equipment_section = self.soup.find("div", class_="need")
        return [
            item.get_text().strip()
            for item in equipment_section.find_all("p")
            if item.get_text().strip()
        ]

    def description(self):
        description_element = self.soup.find("meta", attrs={"name": "description"})
        return description_element["content"]
