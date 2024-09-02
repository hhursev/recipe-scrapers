from html import unescape

from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg


class KitchenStories(AbstractScraper):
    @classmethod
    def host(cls):
        return "kitchenstories.com"
