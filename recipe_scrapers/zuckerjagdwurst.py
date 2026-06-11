import re

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class ZuckerJagdwurst(AbstractScraper):
    @classmethod
    def host(cls):
        return "zuckerjagdwurst.com"

    def site_name(self):
        return "Zucker & Jagdwurst"

    def author(self):
        author = self.schema.author()
        match = re.search(r"\b(?:von|by)\s+(.+)$", author, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return author

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self._parse_time(r"(?:Back|Koch)zeit|baking")

    def prep_time(self):
        return self._parse_time(r"Vorbereitung|Zubereitung|prep")

    def _parse_time(self, keyword):
        for div in self.soup.find_all("div"):
            text = div.get_text(strip=True)
            if re.search(keyword, text, re.IGNORECASE) and re.search(
                r"[Mm]inuten|minutes", text
            ):
                mins_word = r"(?:Minuten?|minutes?)"
                hours_word = r"(?:Stunden?|hours?)"
                kw = r"(?:" + keyword + r")"
                m = re.search(
                    r"(\d+)\s+" + hours_word + r"\s+(\d+)\s+" + mins_word + r"\s+" + kw,
                    text,
                    re.IGNORECASE,
                )
                if m:
                    return int(m.group(1)) * 60 + int(m.group(2))
                m = re.search(
                    r"(\d+)\s+" + hours_word + r"\s+" + kw, text, re.IGNORECASE
                )
                if m:
                    return int(m.group(1)) * 60
                m = re.search(
                    r"(\d+)\s+" + mins_word + r"\s+" + kw, text, re.IGNORECASE
                )
                if m:
                    return int(m.group(1))
        return None

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        tag = self.soup.find("meta", attrs={"name": "description"})
        if tag and tag.get("content"):
            return normalize_string(tag["content"])
        return self.schema.description()

    def ingredient_groups(self):
        first_li = self.soup.find("li", attrs={"itemprop": "recipeIngredient"})
        if not first_li:
            return [IngredientGroup(ingredients=self.ingredients(), purpose=None)]

        container = first_li.parent.parent
        groups = []
        current_purpose = None
        current_ingredients = []

        for child in container.children:
            if not hasattr(child, "name") or child.name is None:
                continue
            if child.name == "h4":
                if current_ingredients:
                    groups.append(
                        IngredientGroup(
                            ingredients=current_ingredients, purpose=current_purpose
                        )
                    )
                    current_ingredients = []
                purpose = normalize_string(child.get_text()).rstrip(":")
                current_purpose = purpose
            elif child.name == "ul":
                for li in child.find_all("li", attrs={"itemprop": "recipeIngredient"}):
                    current_ingredients.append(normalize_string(li.get_text()))

        if current_ingredients:
            groups.append(
                IngredientGroup(
                    ingredients=current_ingredients, purpose=current_purpose
                )
            )

        return (
            groups
            if groups
            else [IngredientGroup(ingredients=self.ingredients(), purpose=None)]
        )
