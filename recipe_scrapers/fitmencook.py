from ._abstract import AbstractScraper
from ._utils import get_equipment, get_minutes, get_yields, normalize_string


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
        parent = self.soup.find("div", {"class": "fmc_ingredients"})
        if parent:
            return [
                normalize_string(li.get_text())
                for li in parent.find_all("li")
                if not li.find("strong") and normalize_string(li.get_text())
            ]

        ingredients = []
        seen = set()
        for ul in self.soup.find_all("ul", class_="fmc_instacart_list"):
            for li in ul.find_all("li", recursive=False):
                for junk in li.select("button, .fmc_btn_container, .product_price"):
                    junk.decompose()
                text = normalize_string(li.get_text())
                if text and len(text) > 2 and text not in seen:
                    ingredients.append(text)
                    seen.add(text)
        if ingredients:
            return ingredients

        return []

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
        return ", ".join(get_equipment(categories))

    def instructions(self):
        steps = []

        rc_steps = self.soup.find("div", class_="rc_steps")
        if rc_steps:
            for li in rc_steps.find_all("li", class_="rc_step"):
                text = li.get_text(separator=" ", strip=True)
                if text:
                    steps.append(" ".join(text.split()))

        if not steps:
            container = self.soup.find("div", class_="fmc_recipe_the_content")
            if container:
                for step_div in container.find_all("div", class_="fmc_step_wrap"):
                    content_div = step_div.find("div", class_="fmc_step_content")
                    if content_div:
                        text = content_div.get_text(separator=" ", strip=True)
                        if text:
                            steps.append(" ".join(text.split()))

        return "\n".join(steps)
