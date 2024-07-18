from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class QuiToque(AbstractScraper):
    @classmethod
    def host(cls):
        return "quitoque.fr"

    @staticmethod
    def _get_text(element):
        if element:
            return normalize_string(element.get_text())
        else:
            return None

    def _get_time(self, time_name):
        times = self.soup.select("div,.recipe-infos-short .item-info")
        total_time = None
        for time in times:
            if time_name in time.get_text():
                total_time = self._get_text(time).replace(time_name, "")
        return get_minutes(total_time)

    def _get_nutrients(self, nutrient_name):
        nutrient_element = self._nutrient_list.find("p", string=nutrient_name).parent
        return self._get_text(nutrient_element.find("p", class_="regular"))

    def canonical_url(self):
        return self.soup.find("meta", {"property": "og:url"}).get("content")

    def author(self):
        return "QuiToque"

    def title(self):
        return self._get_text(self.soup.find("h1", class_="title-2"))

    def keywords(self):
        product_tags = self.soup.find(id="product-tags").find_all(class_="badge")
        keywords = {self._get_text(tag) for tag in product_tags}
        return list(sorted(keywords))

    def category(self):
        category = self.soup.find(class_="primary-ghost")
        return self._get_text(category)

    def total_time(self):
        return self._get_time("Total")

    def prep_time(self):
        return self._get_time("En cuisine")

    def yields(self):
        serving = self.soup.find(id="ingredients").find("p", class_="body-2")
        return get_yields(serving)

    def image(self):
        img_element = self.soup.find(class_="image").find("img")
        return img_element["src"]

    def ingredients(self):
        ingredients_list = self.soup.select("#ingredients .ingredient-list li")
        ingredients_list.extend(self.soup.select(".kitchen-list li"))
        return [self._get_text(tag) for tag in ingredients_list]

    def equipment(self):
        equipment_list = self.soup.select("#equipment .ingredient-list li")
        return [self._get_text(tag) for tag in equipment_list]

    def instructions(self):
        instructions_list = self.soup.select("#preparation-steps li")
        return "\n".join(
            [self._get_text(instruction) for instruction in instructions_list]
        )

    def description(self):
        description = self.soup.find("div", class_="container body-2 regular mt-2 mb-4")
        return self._get_text(description)

    def nutrients(self):
        self._nutrient_list = self.soup.find(id="portion")
        nutrients = {
            "calories": self._get_nutrients("Énergie (kCal)"),
            "fatContent": self._get_nutrients("Matières grasses"),
            "saturatedFatContent": self._get_nutrients("dont acides gras saturés"),
            "carbohydrateContent": self._get_nutrients("Glucides"),
            "sugarContent": self._get_nutrients("dont sucre"),
            "fiberContent": self._get_nutrients("Fibres"),
            "proteinContent": self._get_nutrients("Protéines"),
            "sodiumContent": self._get_nutrients("Sel"),
        }
        return nutrients
