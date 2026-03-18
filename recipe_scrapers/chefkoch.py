from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg


class Chefkoch(AbstractScraper):

    class _CustomSchemaOrg(SchemaOrg):
        def _extract_howto_instructions_text(self, schema_item):
            instructions_gist = []

            if isinstance(schema_item, list):
                for item in schema_item:
                    instructions_gist.extend(
                        self._extract_howto_instructions_text(item)
                    )

            elif isinstance(schema_item, dict):
                if schema_item.get("@type") == "HowToSection":
                    elements = schema_item.get("itemListElement")
                    if elements:
                        instructions_gist.extend(
                            self._extract_howto_instructions_text(elements)
                        )

                elif schema_item.get("@type") == "HowToStep":
                    name = schema_item.get("name")
                    text = schema_item.get("text")

                    if (
                        isinstance(name, str)
                        and text
                        and not text.startswith(name.rstrip("."))
                    ):
                        instructions_gist.append(name)

                    elements = schema_item.get("itemListElement")
                    if elements:
                        instructions_gist.extend(
                            self._extract_howto_instructions_text(elements)
                        )

                    if text:
                        instructions_gist.append(text)

            return instructions_gist

    _schema_cls = _CustomSchemaOrg

    @classmethod
    def host(cls):
        return "chefkoch.de"
