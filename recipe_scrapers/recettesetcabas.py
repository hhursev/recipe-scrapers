import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string

STEP_NUMBER = re.compile(r"^\d+\s*[.)]\s*")


def _split_instruction_paragraph(paragraph):
    fragments = [
        fragment
        for raw_fragment in paragraph.get_text("\n").splitlines()
        if (fragment := normalize_string(raw_fragment))
    ]
    steps = []
    for fragment in fragments:
        if STEP_NUMBER.match(fragment) or not steps:
            steps.append(fragment)
        else:
            steps[-1] = normalize_string(f"{steps[-1]} {fragment}")

    return steps


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
        # Recipes can leave the schema instructions empty or collapse multiple visible
        # steps into one item. Some pages give every instruction paragraph the same
        # styling, including unnumbered preparation notes. Others only distinguish
        # their steps from the introduction by numbering them. The sections after the
        # first one hold the Thermomix version and the site's own commentary.
        steps = self.schema.instructions().split("\n")
        recipe_section = self.soup.select_one(".bloc-recette > section:first-of-type")
        paragraphs = (
            recipe_section.find_all("p", recursive=False) if recipe_section else []
        )
        numbered_paragraphs = [
            paragraph
            for paragraph in paragraphs
            if any(
                STEP_NUMBER.match(step)
                for step in _split_instruction_paragraph(paragraph)
            )
        ]
        numbered_step_count = sum(
            bool(STEP_NUMBER.match(step))
            for paragraph in numbered_paragraphs
            for step in _split_instruction_paragraph(paragraph)
        )

        if not any(steps) or (len(steps) == 1 and numbered_step_count > 1):
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
                    for step in _split_instruction_paragraph(paragraph)
                ]
            else:
                steps = [
                    step
                    for paragraph in numbered_paragraphs
                    for step in _split_instruction_paragraph(paragraph)
                ]

        steps = [STEP_NUMBER.sub("", step) for step in steps if step]
        if not steps:
            raise ElementNotFoundInHtml("Could not find the recipe instructions.")

        return "\n".join(steps)
