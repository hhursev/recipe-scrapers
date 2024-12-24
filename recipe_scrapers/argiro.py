from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg
from ._utils import get_equipment, normalize_string


class Argiro(AbstractScraper):

    class _CustomSchemaOrg(SchemaOrg):
        """Overrides the default schema.org metadata parser"""

        @staticmethod
        def _contains_schematype(item, schematype):
            if not isinstance(item, (dict, list, str)):
                return False
            return SchemaOrg._contains_schematype(item, schematype)

        def _extract_howto_instructions_text(self, schema_item):
            if schema_item.get("@type") != "HowToStep":
                return
            return schema_item.get("text").split("\n")

    _schema_cls = _CustomSchemaOrg

    @classmethod
    def host(cls):
        return "argiro.gr"

    def equipment(self):
        equipment_items = [
            normalize_string(e.get_text())
            for e in self.soup.find_all("div", class_="equipment-title")
        ]
        return get_equipment(equipment_items)
