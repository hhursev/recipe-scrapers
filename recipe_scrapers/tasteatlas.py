from ._abstract import AbstractScraper
from ._utils import normalize_string


class TasteAtlas(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteatlas.com"

    def description(self):
        clean_text = normalize_string(self.schema.description())
        return clean_text

    def site_name(self):
        return "Taste Atlas"
