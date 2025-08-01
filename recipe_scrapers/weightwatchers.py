from ._abstract import AbstractScraper
from ._utils import normalize_string


class WeightWatchers(AbstractScraper):
    @classmethod
    def host(cls):
        return "weightwatchers.com"

    def author(self):
        return "WeightWatchers"

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
