import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class WeightWatchers(AbstractScraper):
    @classmethod
    def host(cls):
        return "weightwatchers.com"

    def author(self):
        return "WeightWatchers"

    def title(self):
        return self.soup.find("h1").get_text().strip()

    # cooking times, yield, difficulty are in a common div in public and non-public recipes
    # but class of that block and sub elements are different
    # so finding the block and extracting a value will be overridden in class for public recipes,
    # but picking the data item based on order is don in this base class (total_time(), cook_time() and so on)
    def _find_data_container(self):
        return self.soup.find("div", {"class": "styles_container__3N3E8"})

    def _extract_item_field(self, item):
        return item.contents[1]

    def total_time(self):
        return get_minutes(
            self._extract_item_field(self._find_data_container().contents[0])
        )

    def prep_time(self):
        return get_minutes(
            self._extract_item_field(self._find_data_container().contents[1])
        )

    def cook_time(self):
        return get_minutes(
            self._extract_item_field(self._find_data_container().contents[2])
        )

    def yields(self):
        return get_yields(
            self._extract_item_field(self._find_data_container().contents[3])
        )

    def difficulty(self):
        return self._extract_item_field(
            self._find_data_container().contents[4]
        ).get_text()

    #   Alternative way to extract data based on description instead of position
    #    def total_time(self):
    #        return get_minutes(
    #            self.__find_data_container()
    #            .find("div", string=re.compile(r"minutes Total Time"))
    #            .previous_sibling
    #        )

    def image(self):
        background_image_style = self.soup.find(
            "div", {"class": "styles_image__2dnNm"}
        )["style"]

        if background_image_style:
            return (
                re.search(r'url\("(?P<imgurl>\S*)"\);', background_image_style)
                .groupdict()
                .get("imgurl")
            )

        return None

    def _find_ingredient_tags(self):
        return self.soup.find(
            "h3", {"id": "food-detail-recipe-ingredients-header"}
        ).parent.find_all("div", {"class": "styles_name__1OYVU"})

    @staticmethod
    def _extract_ingredient_name(ingredient):
        return normalize_string(
            ingredient.find("div", {"class": "styles_ingredientName__1Vffd"})
            .find("div")
            .get_text()
        )

    @staticmethod
    def _extract_portion_parts(ingredient):
        tags = ingredient.find("div", {"class": "styles_portion__2NQyq"}).find_all(
            "span"
        )
        try:
            return (
                normalize_string(tags[0].get_text()),
                normalize_string(tags[1].get_text()),
                (
                    normalize_string(tags[2].get_text().replace(", ", ""))
                    if tags[2]
                    else None
                ),
            )
        except IndexError:
            return (
                normalize_string(tags[0].get_text()),
                normalize_string(tags[1].get_text()),
                None,
            )

    def __parse_ingredient(self, ingredient):
        ingredient_name = self.__class__._extract_ingredient_name(ingredient)
        amount, unit, comment = self.__class__._extract_portion_parts(ingredient)

        if comment:
            return f"{amount} {unit} {ingredient_name}; {comment}"
        else:
            return f"{amount} {unit} {ingredient_name}"

    def ingredients(self):
        return [
            self.__parse_ingredient(ingredient)
            for ingredient in self._find_ingredient_tags()
        ]

    def _get_instructions(
        self, header_tag, header_attribute, header_value, instruction_tag
    ):
        instructions = self.soup.find(
            header_tag, {header_attribute: header_value}
        ).parent.find("ol")
        return "\n".join(
            [
                normalize_string(instruction.get_text())
                for instruction in instructions.find_all(instruction_tag)
            ]
        )

    def instructions(self):
        return self._get_instructions(
            "h3", "id", "food-detail-recipe-instruction-header", "div"
        )

    def description(self):
        return self.soup.find("div", {"class": "copy-1"}).get_text().strip()

    def nutrients(self):
        result = {}

        result["personal points"] = (
            self.soup.find("div", {"class": "styles_points__2gv9n"})
            .find("div", {"class": "styles_container__2p-YG"})
            .get_text()
        )

        veggiepoints = self.soup.find(
            "div", {"class": "styles_vegetableServings__2YSPy"}
        )
        if veggiepoints:
            result["positive points"] = normalize_string(
                veggiepoints.find(
                    "div", {"class": "styles_container__2p-YG"}
                ).next_sibling.get_text()
            )

        return result
