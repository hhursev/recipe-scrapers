from bs4 import Tag
import re

from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException, StaticValueException
from ._utils import normalize_string, get_minutes
from ._grouping_utils import IngredientGroup

# fiter to find non-empty tags
nonempty = re.compile(r".+")


def has_css_class(tag, cssclass):
    classes = tag.get("class")
    if not classes:
        return False
    if isinstance(classes, list):
        return cssclass in classes
    return classes == cssclass


class Rezeptwelt(AbstractScraper):
    @classmethod
    def host(cls):
        return "rezeptwelt.de"

    def site_name(self):
        return "Thermomix Rezeptwelt"

    def author(self):
        tag = self.soup.find("div", itemprop="author")
        if tag:
            return normalize_string(tag.get_text())
        tag = self.soup.find("span", {"id": "viewRecipeAuthor"})
        return normalize_string(tag.get_text())

    def ingredients(self) -> list[str]:
        results = []
        for ingredient_group in self.ingredient_groups():
            results.extend(ingredient_group.ingredients)
        return results

    def ingredient_groups(self) -> list[IngredientGroup]:
        ingredient_groups = []
        group = None
        ingredients = None
        section = self.soup.find(id="ingredient-section")
        # iterate over all tags in the ingredient section
        # for each <p class="h5"> start a new group
        # for each <tag itemprop="recipeIngredient"> add a new ingredient
        for child in section.descendants:
            if isinstance(child, Tag):
                if child.name == "p" and has_css_class(child, "h5"):
                    if ingredients:
                        # save previous group
                        ingredient_groups.append(IngredientGroup(purpose=group, ingredients=ingredients))
                    # group might be an empty string, but that is ok
                    group = child.text.strip()
                    ingredients = []
                elif child.get("itemprop", "") == "recipeIngredient":
                    ingredients.append(child.text)
        if ingredients:
            # group can be None if there is only one main group for all ingredients
            ingredient_groups.append(IngredientGroup(purpose=group, ingredients=ingredients))
        return ingredient_groups

    def instructions(self):
        container = self.soup.find("div", id="preparationSteps").find(
            "span", itemprop="text"
        )
        instructions = []
        for p in container.find_all("p"):
            text = p.get_text().strip()
            if text:
                instructions.append(text)
        if not instructions:
            # instructions are divided by "<br>"
            for text in str(container).replace("<br/>", "\n").replace("\r", "").splitlines():
                text = normalize_string(text.strip())
                if text:
                    instructions.append(text)
        # add optional tips to instructions
        container = self.soup.find("div", attrs={"class": "tips"})
        for p in container.find_all("p"):
            if p and p.string:
                for text in str(p).replace("<br/>", "\n").replace("\r", "").splitlines():
                    text = normalize_string(text.strip())
                    if text:
                        instructions.append(text)
        return "\n".join(instructions)

    def cuisine(self):
        try:
            return self.schema.cuisine()
        except SchemaOrgException:
            return None

    def description(self):
        return self.schema.description().replace(
            " Mehr Thermomix ® Rezepte auf www.rezeptwelt.de", ""
        )

    def language(self):
        return self.soup.find("meta", {"property": "og:locale"})["content"]

    def prep_time(self):
        tag = self.soup.find(itemprop="performTime", content=nonempty)
        return get_minutes(tag['content']) if tag else None

    def equipment(self):
        return [tag['content'] for tag in self.soup.find_all("meta", itemprop="tool", content=nonempty)]

    def reviews(self):
        return None
