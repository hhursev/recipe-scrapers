from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class FitMenCook(AbstractScraper):
    @classmethod
    def host(cls):
        return "fitmencook.com"

    def total_time(self):
        total_time_element = self.soup.find("div", {"class": "fmc_total"})
        if total_time_element:
            time_text = total_time_element.find("span", {"class": "fmc_amount"})
            if time_text:
                return get_minutes(time_text.text.strip())

    def yields(self):
        if div := self.soup.find("div", class_="fmc_nos"):
            if span := div.find("span"):
                return get_yields(f"{span.get_text(strip=True)} servings")

        for h4 in self.soup.find_all("h4"):
            raw_yield = h4.get_text(strip=True)
            for word in raw_yield.split():
                if word.isdigit():
                    return get_yields(f"{word} servings")

    def ingredients(self):
        ingredients_parent = self.soup.find("div", {"class": "fmc_ingredients"})
        ingredients = ingredients_parent.find_all("li")
        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
            if ingredient.find("strong") is None
        ]

    def nutrients(self):
        data = {}
        div = self.soup.find("div", class_="fmc_macros")
        if not div:
            return {}

        mapping = {
            "Calories": "calories",
            "Cal": "calories",
            "Protein": "proteinContent",
            "Fats": "fatContent",
            "Fat": "fatContent",
            "Carbs": "carbohydrateContent",
            "Carbohydrates": "carbohydrateContent",
            "Fiber": "fiberContent",
            "Sodium": "sodiumContent",
            "Sugar": "sugarContent",
        }

        for item in div.find_all("div", class_="fmc_macro"):
            span = item.find("span")
            if not span:
                continue

            raw_val = span.get_text(strip=True)
            raw_val = raw_val.strip()
            num_value = ""
            unit = ""
            i = 0
            while i < len(raw_val) and (raw_val[i].isdigit() or raw_val[i] == "."):
                num_value += raw_val[i]
                i += 1
            if i < len(raw_val):
                unit = raw_val[i:].strip()
            if not num_value:
                num_value, unit = raw_val, ""

            label = item.get_text(strip=True).replace(raw_val, "").strip()

            for key, field in mapping.items():
                if key in label:
                    if field == "calories":
                        data[field] = num_value
                    else:
                        val = f"{num_value} {unit}".strip()
                        data[field] = val if val != num_value else num_value
                    break
        return data

    def category(self):
        div = self.soup.find("div", class_="fmc_grid_cat")
        if not div:
            return ""
        categories = [
            a.get_text(strip=True) for a in div.find_all("a") if a.get_text(strip=True)
        ]
        return ", ".join(set(categories))
