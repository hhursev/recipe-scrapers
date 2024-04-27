# mypy: allow-untyped-defs

import re
from typing import List

from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup
from ._utils import normalize_string


class Ploetzblog(AbstractScraper):
    @classmethod
    def host(cls):
        return "ploetzblog.de"

    def author(self):
        return self._get_script_string_field("authorName")

    def title(self):
        return self.soup.find("h1").text

    def category(self):
        return self.schema.category()

    def total_time(self):
        # Could also be scraped manually from the page text
        # Issue is that the time units are in German, which get_minutes does not work for
        return self._get_script_number_field("preparationTime")

    def yields(self):
        count_input = self.soup.find("input", {"id": "recipePieceCount"})
        count = count_input.get("value")

        unit_td = count_input.parent.find_next_sibling("td")
        unit = normalize_string(unit_td.text)

        return f"{count} {unit}"

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients_div = self.soup.find(
            "div", {"class": "we2p-pb-recipe__ingredients"}
        )
        ingredients_table = ingredients_div.find_all("table")[1]
        return self._get_ingredients_from_table(ingredients_table)

    def ingredient_groups(self) -> List[IngredientGroup]:
        ingredient_groups = []

        group_divs = self.soup.find_all(
            "div", {"class": "module-mb-4 vg-wort-text module-break-inside-avoid"}
        )
        for group_div in group_divs:
            h4 = group_div.find("h4")
            purpose = normalize_string(h4.text)

            ingredients_table = group_div.find("table")
            ingredients = self._get_ingredients_from_table(ingredients_table)

            ingredient_groups.append(IngredientGroup(ingredients, purpose=purpose))

        return ingredient_groups

    def instructions(self):
        instruction_ps = self.soup.find_all(
            "p", {"class": "module-float-left module-my-auto we2p-autolinker"}
        )
        instructions = [
            normalize_string(instruction.text) for instruction in instruction_ps
        ]
        return "\n".join(instructions[:2])

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        description_div = self.soup.find(
            "div", {"class": "we2p-pb-recipe__description"}
        )

        lines = []
        for p in description_div.find_all("p"):
            lines.append(normalize_string(p.text))

        return "\n".join(lines)

    def site_name(self):
        return "Plötzblog"

    def _get_ingredients_from_table(self, ingredients_table):
        ingredients = []

        tr_list = ingredients_table.find_all("tr")
        for tr in tr_list:
            line = []
            td_list = tr.find_all("td", limit=2)
            for td in td_list:
                span_list = td.find_all("span")
                for span in span_list:
                    text = normalize_string(span.text)
                    if text:
                        line.append(text)
            ingredients.append(" ".join(line))

        return ingredients

    def _get_script(self):
        main = self.soup.find("main", {"id": "main-content"})
        script = main.find(
            "script", string=re.compile(r'"types":\["ForumPost","Recipe"\]')
        )
        return script

    def _get_field_name_pattern(self, field_name):
        return f'\\"{field_name}\\"\\s*:\\s*'

    def _get_script_string_field(self, field_name):
        script = self._get_script()

        result = re.search(
            self._get_field_name_pattern(field_name) + '\\"([^"]+)', script.string
        )
        if not result:
            return None

        return result.group(1)

    def _get_script_number_field(self, field_name):
        script = self._get_script()

        result = re.search(
            self._get_field_name_pattern(field_name) + "([^,]+)", script.string
        )
        if not result:
            return None

        return int(result.group(1))
