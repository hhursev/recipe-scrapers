import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string

STEP_NUMBER = re.compile(r"^\d+\s*[.)]\s*")


class RecettesEtCabas(AbstractScraper):
    @classmethod
    def host(cls):
        return "recettesetcabas.com"

    def ingredients(self):
        return [
            ingredient
            for group in self.ingredient_groups()
            for ingredient in group.ingredients
        ]

    def ingredient_groups(self):
        # The schema lists the recipe ingredients as semicolon separated text. The
        # page lists them too, but without their quantities and with a disclaimer
        # trailing the last item. The pantry staples are only listed in the page.
        groups = []

        ingredients = [
            normalize_string(ingredient)
            for entry in self.schema.ingredients()
            for ingredient in entry.split(";")
            if normalize_string(ingredient)
        ]
        if ingredients:
            groups.append(IngredientGroup(ingredients=ingredients))

        pantry = self.soup.select_one(".bloc-desc .col-header:has(.icon-cupboard)")
        if pantry:
            heading = pantry.find("h2")
            pantry_items = pantry.select("ul li")
            items = [
                normalize_string(ingredient)
                for item in pantry_items
                for ingredient in (
                    item.get_text().split(",")
                    if len(pantry_items) == 1
                    else [item.get_text()]
                )
                if normalize_string(ingredient)
            ]
            if items:
                groups.append(
                    IngredientGroup(
                        purpose=(
                            normalize_string(heading.get_text()).rstrip(" :")
                            if heading
                            else None
                        ),
                        ingredients=items,
                    )
                )

        return groups

    def instructions(self):
        # Recipes can leave the schema instructions empty. Some pages give every
        # instruction paragraph the same styling, including unnumbered preparation
        # notes. Others only distinguish their steps from the introduction by
        # numbering them. The sections after the first one hold the Thermomix version
        # of the recipe and the site's own commentary on it.
        steps = self.schema.instructions().split("\n")
        if not any(steps):
            recipe_section = self.soup.select_one(
                ".bloc-recette > section:first-of-type"
            )
            paragraphs = (
                recipe_section.find_all("p", recursive=False) if recipe_section else []
            )
            numbered_paragraphs = [
                paragraph
                for paragraph in paragraphs
                if STEP_NUMBER.match(normalize_string(paragraph.get_text()))
            ]
            instruction_classes = (
                numbered_paragraphs[0].get("class", []) if numbered_paragraphs else []
            )
            styled_paragraphs = (
                [
                    paragraph
                    for paragraph in paragraphs
                    if paragraph.get("class", []) == instruction_classes
                ]
                if instruction_classes
                else [
                    paragraph
                    for paragraph in paragraphs
                    if "para-style-body" in paragraph.get("class", [])
                ]
            )
            if styled_paragraphs:
                steps = [
                    step
                    for paragraph in styled_paragraphs
                    if (step := normalize_string(paragraph.get_text()))
                ]
            else:
                steps = [
                    normalize_string(paragraph.get_text())
                    for paragraph in numbered_paragraphs
                ]

        steps = [STEP_NUMBER.sub("", step) for step in steps if step]
        if not steps:
            raise ElementNotFoundInHtml("Could not find the recipe instructions.")

        return "\n".join(steps)
