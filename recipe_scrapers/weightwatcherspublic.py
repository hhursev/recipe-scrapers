from ._exceptions import StaticValueException
from ._utils import normalize_string
from .weightwatchers import WeightWatchers


# collect the differences between public and non-public weightwatcher recipes in this class
class WeightWatchersPublic(WeightWatchers):
    @classmethod
    def host(cls):
        return "weightwatchers.com"

    def site_name(self):
        title = self.soup.find("title")
        if not title:
            raise StaticValueException(return_value="WeightWatchers")
        _recipe, _delimiter, site_name = title.text.rpartition("|")
        return site_name.lstrip()

    def _find_data_container(self):
        return self.soup.find("div", {"class": "HorizontalList_list__GESs0"})

    def _extract_item_field(self, item):
        return item.find("div", {"data-e2e-name": "attribute_item_value"})

    def image(self):
        return self.soup.find("img", {"class": "FoodMasthead_heroImage__BjVdZ"})["src"]

    def language(self):
        return self.soup.find("html").get("xml:lang")

    def nutrients(self):
        return {
            "points": self.soup.find("div", {"class": "Coin_text__3UOb0"})["aria-label"]
        }

    def description(self):
        return normalize_string(
            self.soup.find("div", {"data-e2e-name": "food_masthead_detail_description"})
            .find("div", {"class": "ReadMoreLess_collapsed__IAzxP"})
            .get_text()
        )

    def instructions(self):
        return self._get_instructions(
            "h2", "class", "InstructionsFood_headline__vw7cn", "span"
        )

    def _find_ingredient_tags(self):
        return (
            self.soup.find("div", {"class": "IngredientsCard_card__VSY4x"})
            .find("div", {"data-e2e-name": "vertical_list_items"})
            .find_all("div", recursive=False)
        )

    @staticmethod
    def _extract_ingredient_name(ingredient):
        return normalize_string(
            ingredient.find("p", {"data-e2e-name": "ingredient_name"}).get_text()
        )

    @staticmethod
    def _extract_portion_parts(ingredient):
        tags = ingredient.find(
            "p", {"data-e2e-name": "ingredient_description"}
        ).find_all("span")

        if len(tags) > 2:
            comment = normalize_string(tags[2].get_text().replace(", ", "", 1))
            unit = normalize_string(tags[1].get_text())
        else:
            description_parts = normalize_string(tags[1].get_text()).split(", ", 1)
            unit = description_parts[0]
            comment = description_parts[1] if len(description_parts) > 1 else None

        return normalize_string(tags[0].get_text()), unit, comment
