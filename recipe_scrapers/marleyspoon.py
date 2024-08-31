import re

from ._abstract import AbstractScraper
from ._exceptions import RecipeScrapersExceptions
from ._utils import get_minutes, normalize_string


class UnsupportedLocale(RecipeScrapersExceptions):
    """No support for selected locale of this website"""

    def __init__(self, lang):
        self.lang = lang
        message = f'Selected locale "{self.lang}" is not supported.'
        super().__init__(message)


class MarleySpoon(AbstractScraper):
    @classmethod
    def host(cls, domain="de"):
        return f"marleyspoon.{domain}"

    def canonical_url(self):
        return self.soup.find("meta", {"property": "og:url"})["content"]

    def author(self):
        return normalize_string(self.soup.find(class_="author-info").a.get_text())

    def title(self):
        return normalize_string(
            self.soup.find("h3", {"class": "recipe-title"}).get_text()
        )

    def _specs(self):
        vocab = {
            "de": {
                "time": "Dauer",
                "category": "Schwierigkeitsgrad",
                "nutrients": "Nährwertangaben",
            },
            "nl": {
                "time": "Bereidingstijd",
                "category": "Niveau",
                "nutrients": "Voedingswaarde",
            },
            "en": {
                "time": "Serving Time",
                "category": "Level",
                "nutrients": "Nutrition",
            },
        }

        self.locale = self.language()[:2]
        if self.locale not in vocab.keys():
            raise UnsupportedLocale(self.locale)

        recipe_specs = self.soup.find("ul", {"class": "recipe-specs"})

        time_label = recipe_specs.find("label", string=vocab[self.locale]["time"])
        category_label = recipe_specs.find(
            "label", string=vocab[self.locale]["category"]
        )
        nutrients_pattern = "^{}.*$".format(vocab[self.locale]["nutrients"])
        nutrients_label = recipe_specs.find(
            "label", string=re.compile(nutrients_pattern)
        )

        time_info = time_label.find_next_sibling("p").get_text()
        category_info = category_label.find_next_sibling("p").get_text()
        nutrients_info = nutrients_label.find_next_sibling("p").get_text()

        return time_info, category_info, nutrients_info

    def total_time(self):
        return get_minutes(self._specs()[0])

    def category(self):
        return normalize_string(self._specs()[1])

    def nutrients(self):
        nutrients = {}

        vocab = {
            "calories": {
                "de": "Kalorien",
                "nl": "Calorieën",
                "en": "Calories",
                "unit": "calories",
            },
            "fatContent": {"de": "Fett", "nl": "Vet", "en": "Fat", "unit": "grams fat"},
            "proteinContent": {
                "de": "Eiweiß",
                "nl": "Eiwit",
                "en": "Proteins",
                "unit": "grams protein",
            },
            "carbohydrateContent": {
                "de": "Kohlenhydrate",
                "nl": "Koolhydraten",
                "en": "Carbs",
                "unit": "grams carbohydrates",
            },
        }

        nutrients_info = self._specs()[2].split(",")
        for nutrient in nutrients_info:
            for key, value in vocab.items():
                if self.locale not in value.keys():
                    raise UnsupportedLocale(self.locale)
                if value[self.locale] in nutrient:
                    nutrients[key] = (
                        re.search(r"[\d.]+", nutrient).group() + " " + value["unit"]
                    )
        return nutrients

    def image(self):
        return self.soup.find("meta", property="og:image")["content"]

    def ingredients(self):
        send = self.soup.find("div", {"class": "dish-detail__we-send"}).find_all("div")
        additional = self.soup.find(
            "div", {"class": "dish-detail__sidebar-section"}
        ).div.find_all("li")
        return [normalize_string(i.get_text()) for i in send + additional]

    def instructions(self):
        steps = self.soup.find("div", {"class": "dish-steps__container"}).find_all(
            "p", {"class": "dish-step__body-text"}
        )
        steps = [normalize_string(step.get_text()) for step in steps]
        return "\n".join(steps)

    def equipment(self):
        equipment = self.soup.find_all(
            "div", {"class": "dish-detail__sidebar-section"}
        )[1].find_all("li")
        return [normalize_string(e.get_text()) for e in equipment]

    def keywords(self):
        keywords = self.soup.find(class_="recipe-labels").find_all(
            class_="recipe-attributes__label"
        )
        return [normalize_string(keyword.get_text()) for keyword in keywords]

    def description(self):
        description = self.soup.find("div", {"class": "whats-cooking"}).p.get_text()
        return normalize_string(description)
