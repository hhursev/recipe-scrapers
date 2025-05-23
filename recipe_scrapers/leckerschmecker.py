from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg
from ._utils import get_equipment


class LeckerSchmecker(AbstractScraper):

    class _CustomSchemaOrg(SchemaOrg):
        def _find_entity(self, item, schematype):
            if self._contains_schematype(item, schematype):
                return item
            graph = item.get("@graph", [])
            if isinstance(graph, dict):
                graph = list(graph.values())
            elif not isinstance(graph, list):
                graph = [graph]
            for node in graph:
                if isinstance(node, dict) and self._contains_schematype(
                    node, schematype
                ):
                    return node

    _schema_cls = _CustomSchemaOrg

    @classmethod
    def host(cls):
        return "leckerschmecker.me"

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
