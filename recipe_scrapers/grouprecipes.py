from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_minutes, get_yields, normalize_string


class GroupRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "grouprecipes.com"

    def site_name(self):
        raise StaticValueException(return_value="Group Recipes")

    def title(self):
        return normalize_string(self.soup.find("title").text)

    def author(self):
        container = self.soup.find("div", {"class": "thecook"})
        return normalize_string(container.find("a", {"class": "usr"}).text)

    def image(self):
        container = self.soup.find("div", {"class": "photos"})
        return container.find("img", {"class": "photo"})["src"]

    def total_time(self):
        container = self.soup.find("strong", {"class": "cooktime"})
        return get_minutes(container.find("span", {"class": "value-title"})["title"])

    def yields(self):
        container = self.soup.find("div", {"class": "details"})
        return get_yields(container.find("li", {"class": "servings"}))

    def description(self):
        container = self.soup.find("div", {"class": "details"})
        return normalize_string(next(container.find("p").stripped_strings))

    def category(self):
        container = self.soup.find("ul", {"class": "tags_text"})
        return ", ".join([tag.text for tag in container.find_all("li")])

    def ingredients(self):
        container = self.soup.find("div", {"class": "ingredients"}).find("ul")
        ingredients = [ingredient for ingredient in container.find_all("li")]
        return [
            " ".join(ingredient.find("a", {"class": "to_list"})["rel"])
            for ingredient in ingredients
        ]

    def instructions(self):
        container = self.soup.find("ul", {"class": "instructions"})
        instructions = [instruction.text for instruction in container.find_all("li")]
        return "\n".join(instructions)
