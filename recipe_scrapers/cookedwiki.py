from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class CookedWiki(AbstractScraper):
    @classmethod
    def host(cls):
        return "cooked.wiki"

    def author(self):
        return "Cooked.wiki"

    def title(self):
        return self.soup.select_one(".header-title-content .title").get_text(strip=True)

    def image(self):
        img = self.soup.select_one(".header-image .item-img")
        return img.get("src") if img else None

    def _extract_ingredients(self, container):
        return [
            normalize_string(ingredient.find("p").get_text())
            for ingredient in container.select(
                ".ingredient[itemprop='recipeIngredient']"
            )
            if ingredient.find("p")
        ]

    def ingredients(self):
        return self._extract_ingredients(self.soup)

    def ingredient_groups(self):
        shopping_lists = self.soup.select(".shopping-list")
        groups = []

        for shopping_list in shopping_lists:
            note_elem = shopping_list.find("p", {"class": "note"})
            purpose = (
                normalize_string(note_elem.get_text(strip=True)) if note_elem else None
            )

            section_ingredients = self._extract_ingredients(shopping_list)

            if section_ingredients:
                groups.append(
                    IngredientGroup(ingredients=section_ingredients, purpose=purpose)
                )

        return groups if groups else None

    def instructions(self):
        steps = self.soup.select_one(".steps[itemprop='recipeInstructions']")
        if not steps:
            return ""
        return "\n".join(
            normalize_string(step.find("p").get_text())
            for step in steps.find_all("li")
            if step.find("p")
        )

    def yields(self):
        yields_elem = self.soup.find("div", {"itemprop": "recipeYield"})
        return f"{yields_elem.get_text(strip=True)} servings" if yields_elem else None

    def description(self):
        desc_input = self.soup.find("input", {"name": "description"})
        return (
            normalize_string(desc_input.get("value"))
            if desc_input and desc_input.get("value")
            else None
        )

    def keywords(self):
        keywords_input = self.soup.find("input", {"name": "keywords"})
        if keywords_input and keywords_input.get("value"):
            return [
                k.strip() for k in keywords_input.get("value").split(",") if k.strip()
            ]
        return None

    def canonical_url(self):
        recipe_link = self.soup.select_one(".header-title-content .recipe-link")
        if recipe_link and recipe_link.get("href"):
            return recipe_link.get("href")
        url_input = self.soup.find("input", {"name": "url"})
        return (
            url_input.get("value") if url_input and url_input.get("value") else self.url
        )
