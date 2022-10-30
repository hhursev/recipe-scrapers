# mypy: allow-untyped-defs

from ._utils import normalize_string
from .weightwatchers import WeightWatchers


# collect the differences between public and non-public weightwatcher recipes in this class
class WeightWatchersPublic(WeightWatchers):
    @classmethod
    def host(cls):
        return "www.weightwatchers.com"

    def _findDataContainer(self):
        return self.soup.find("div", {"class": "HorizontalList_list__GESs0"})

    def _extractItemField(self, item):
        return item.find("div", {"data-e2e-name": "attribute_item_value"})

    def image(self):
        return self.soup.find("img", {"class": "FoodMasthead_heroImage__BjVdZ"})["src"]

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
        return self._getInstructions(
            "h2", "class", "InstructionsFood_headline__vw7cn", "span"
        )

    def _findIngridientTags(self):
        return (
            self.soup.find("div", {"class": "IngredientsCard_card__VSY4x"})
            .find("div", {"data-e2e-name": "vertical_list_items"})
            .find_all("div", recursive=False)
        )

    def _extractIngridientName(self, ingridient):
        return normalize_string(
            ingridient.find("p", {"data-e2e-name": "ingredient_name"}).get_text()
        )

    def _extractPortionParts(self, ingridient):
        tags = ingridient.find(
            "p", {"data-e2e-name": "ingredient_description"}
        ).find_all("span")

        comment = None
        unit = None
        if len(tags) > 2:
            comment = normalize_string(tags[2].get_text().replace(", ", "", 1))
            unit = normalize_string(tags[1].get_text())
        else:
            descriptionParts = normalize_string(tags[1].get_text()).split(", ", 1)
            unit = descriptionParts[0]
            comment = descriptionParts[1] if len(descriptionParts) > 1 else None

        return (normalize_string(tags[0].get_text()), unit, comment)
