# mypy: allow-untyped-defs

import re

from ._abstract import AbstractScraper


class TasteAtlas(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteatlas.com"

    def description(self):
        clean_text = re.sub("<[^>]*>", "", self.schema.description())
        return clean_text

    def site_name(self):
        return "Taste Atlas"
