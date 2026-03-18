from ._abstract import AbstractScraper
from ._wprm import WPRMMixin
from ._schemaorg import SchemaOrg


class LeckerSchmecker(WPRMMixin, AbstractScraper):

    class _CustomSchemaOrg(WPRMMixin, SchemaOrg):
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
