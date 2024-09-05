from ._abstract import AbstractScraper
from ._utils import get_max_res_src, get_minutes, normalize_string


class Instrupix(AbstractScraper):
    @classmethod
    def host(cls):
        return "instrupix.com"

    def site_name(self):
        return "Instrupix"

    def author(self):
        return "Instrupix"

    def title(self):
        return self.soup.find("h1", {"class": "entry-title"}).get_text()

    def category(self):
        return self.soup.find("span", {"class": "wprm-recipe-course"}).get_text()

    def total_time(self):
        return (self.cook_time() | 0) + (self.prep_time() | 0)

    def yields(self):
        return self.soup.find("span", {"class": "wprm-recipe-servings"}).get_text()

    def image(self):
        container = self.soup.find("div", {"class": "acme_featured_image"})
        if not container:
            return None
        image = container.find("img", {"src": True})
        return get_max_res_src(image) if image else None

    def ingredients(self):
        ingredient_tags = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})
        return [
            normalize_string(ingredient_tag.get_text())
            for ingredient_tag in ingredient_tags
        ]

    def instructions(self):
        return "\n".join(self.instructions_list())

    def instructions_list(self):
        instruction_tags = self.soup.findAll("li", {"class": "wprm-recipe-instruction"})
        return [
            normalize_string(instruction_tag.get_text())
            for instruction_tag in instruction_tags
        ]

    def ratings(self):
        return None

    def cuisine(self):
        keywords_tag = self.soup.find("span", {"class": "wprm-recipe-cuisine"})
        return keywords_tag.get_text() if keywords_tag else None

    def description(self):
        return self.soup.find("meta", {"name": "description"})["content"]

    def cook_time(self):
        cook_time_tag = self.soup.find(
            "div", {"class": "wprm-recipe-cook-time-container"}
        )

        return get_minutes(cook_time_tag) if cook_time_tag else None

    def prep_time(self):
        prep_time = self.soup.find("div", {"class": "wprm-recipe-prep-time-container"})
        return get_minutes(prep_time) if prep_time else None

    def equipment(self):
        equipment_tags = self.soup.findAll(
            "li", {"class": "wprm-recipe-equipment-item"}
        )
        return [
            normalize_string(equipment_tag.get_text())
            for equipment_tag in equipment_tags
        ]

    def keywords(self):
        keywords_tag = self.soup.find("span", {"class": "wprm-recipe-keyword"})
        return keywords_tag.get_text().split(", ") if keywords_tag else None
