import re

from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException


class ProjectGezond(AbstractScraper):
    @classmethod
    def host(cls):
        return "projectgezond.nl"

    def author(self):
        return "Project Gezond"

    def ratings(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def cuisine(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def category(self):
        category_script = self.soup.find(
            "script", string=re.compile("var dataLayer_content =")
        )
        if not category_script:
            return None

        category_text = category_script.string
        start = category_text.find('"pageCategory":[')
        if start != -1:
            start += len('"pageCategory":[')
            end = category_text.find("]", start)
            if end != -1:
                categories = category_text[start:end].strip('"').split('","')
                return categories if categories else None

    def nutrients(self):
        nutrient_info = {}
        nutrient_elements = self.soup.select("details.nutritions div.nutrition")
        for element in nutrient_elements:
            key = element.get("itemprop")
            value = element.find("dt").get_text(strip=True)
            nutrient_info[key] = value
        return nutrient_info
