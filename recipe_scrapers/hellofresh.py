# mypy: disallow_untyped_defs=False
import re

from ._abstract import AbstractScraper
from ._utils import get_minutes


class HelloFresh(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"hellofresh.{domain}"

    def title(self):
        return self.schema.title()

    def total_time(self):
        script_tag = self.soup.find("script", {"id": "__NEXT_DATA__"})

        if script_tag:
            script_content = script_tag.string
            total_time_match = re.search(r'"totalTime":"(PT\d+M)"', script_content)
            prep_time_match = re.search(r'"prepTime":"(PT\d+M)"', script_content)

            if total_time_match and prep_time_match:
                total_time_str = total_time_match.group(1)
                prep_time_str = prep_time_match.group(1)

                total_time_minutes = get_minutes(total_time_str)
                prep_time_minutes = get_minutes(prep_time_str)

                return total_time_minutes + prep_time_minutes

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def image(self):
        return self.schema.image()

    def nutrients(self):
        return self.schema.nutrients()

    def cuisine(self):
        return self.schema.cuisine()

    def category(self):
        return self.schema.category()
