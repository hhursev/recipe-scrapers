from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class ChooseHomemade(AbstractScraper):
    @classmethod
    def host(cls):
        return "choosehomemade.org"

    def _get_summary_value(self, label):
        for item in self.soup.select(".recipe-layout__summary-item"):
            title = item.select_one(".recipe-layout__summary-item-title")
            if title and label.lower() in title.get_text(strip=True).lower():
                value = item.select_one(".recipe-layout__summary-item-value")
                if value:
                    return value.get_text(strip=True)
        return None

    def title(self):
        return self.soup.select_one("h1.recipe-layout__content-title").get_text(
            strip=True
        )

    def total_time(self):
        time = self._get_summary_value("Time")
        return get_minutes(time)

    def yields(self):
        yields = self._get_summary_value("Servings")
        return get_yields(yields)

    def category(self):
        return self._get_summary_value("Meal")

    def cooking_method(self):
        return self._get_summary_value("Method")

    def keywords(self):
        badges = self.soup.select(
            ".recipe-layout__badges img.recipe-layout__badge[alt]"
        )
        return [badge.get("alt").strip() for badge in badges]

    def author(self):
        return "Choose Homemade"

    def ingredients(self):
        ingredients = []
        for el in self.soup.select(
            "ul.recipe-ingredients__inner-list li .recipe-ingredient__label"
        ):
            text = el.get_text()
            first_non_space = next(
                (i for i, c in enumerate(text) if not c.isspace()), len(text)
            )
            cleaned_text = text[first_non_space:]
            if cleaned_text:
                ingredients.append(cleaned_text)
        return ingredients

    def instructions(self):
        return "\n".join(
            el.get_text(strip=True)
            for el in self.soup.select("ol.recipe-steps__inner li .recipe-step__inner")
        )
