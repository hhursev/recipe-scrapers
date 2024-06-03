# mypy: allow-untyped-defs

import warnings

from ._abstract import AbstractScraper
from ._utils import normalize_string

MARK_SEPARATOR = " "
INGREDIENT_SEPARATOR = "• "

BUG_REPORT_LINK = "https://github.com/hhursev/recipe-scrapers/issues"


def _field_not_provided_by_website_warning(host, field):
    class FieldNotProvidedByWebsiteWarning(Warning):
        pass

    message = (
        "{} doesn't seem to support the {} field. "
        "If you know this to be untrue for some recipe, please submit a bug report at {}"
    )

    warnings.warn(
        message.format(host, field, BUG_REPORT_LINK),
        category=FieldNotProvidedByWebsiteWarning,
    )


class FelixKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "felix.kitchen"

    def author(self):
        result = self.soup.select("span.author > a")
        if not result:
            return None
        return result[0].text

    def title(self):
        found = self.soup.find("meta", {"property": "og:title"})
        return normalize_string(found.get("content"))

    def total_time(self):
        _field_not_provided_by_website_warning(self.host(), "total_time")
        return None

    def yields(self):
        heading_p = self.soup.find("p", {"class": "ti"})
        container_p = heading_p.find_next_sibling("p")
        yields_strong = container_p.find("strong")
        return yields_strong.text

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = []

        step_divs = self._get_step_divs()
        for step_div in step_divs:
            ingredients_div = step_div.find("div")
            ingredients_em_list = ingredients_div.find_all("em")
            for ingredients_em in ingredients_em_list:
                ingredients_text = normalize_string(ingredients_em.text).lstrip(
                    INGREDIENT_SEPARATOR
                )
                ingredients.extend(ingredients_text.split(INGREDIENT_SEPARATOR))

        return ingredients

    def instructions(self):
        instruction_lines = []

        step_divs = self._get_step_divs()
        for step_div in step_divs:
            instructions_div = step_div.find_all("div")[1]
            instructions_p_list = instructions_div.find_all("p")
            for instruction_p in instructions_p_list:
                mark = instruction_p.find("mark", recursive=False)
                if mark:
                    mark.string += MARK_SEPARATOR

                for br in instruction_p.find_all("br"):
                    br.replace_with("\n")

                lines = instruction_p.text.split("\n")
                for line in lines:
                    instruction_lines.append(normalize_string(line))

        return "\n".join(instruction_lines)

    def description(self):
        content_div = self.soup.find("div", {"class": "entry-content"})
        lines = []
        for child in content_div.findChildren(recursive=False):
            if child.name != "p":
                break

            lines.append(child.text)
        return "\n".join(lines)

    def _get_step_divs(self):
        return self.soup.select('div[class*="wp-block-columns is-layout-flex"]')
