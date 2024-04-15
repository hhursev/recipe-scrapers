# mypy: allow-untyped-defs

import functools
import json
import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class AmericasTestKitchen(AbstractScraper):

    @classmethod
    def host(cls, domain="americastestkitchen.com"):
        return domain

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def description(self):
        return self.schema.description()

    def total_time(self):
        return get_minutes(self._get_additional_details.get("recipeTimeNote", None))

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):  # add headnote
        if headnote := self._get_additional_details.get("headnote", None):
            # Ideally this would use HTMLTagStripperPlugin, but I'm not sure how to invoke it here
            headnote = f"Note: {normalize_string(re.sub(r'<.*?>', '', headnote))}\n"
        else:
            headnote = ""
        return headnote + self.schema.instructions()

    def yields(self):
        return self.schema.yields()

    def nutrients(self):
        return self.schema.nutrients()

    def category(self):
        return self.schema.category()

    def ratings(self):
        return self.schema.ratings()

    @functools.cached_property
    def _get_additional_details(self):
        j = json.loads(self.soup.find(type="application/json").string)
        name = list(j["props"]["initialState"]["content"]["documents"])[0]
        return j["props"]["initialState"]["content"]["documents"][name]
