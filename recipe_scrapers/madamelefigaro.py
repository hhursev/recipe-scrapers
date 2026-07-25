from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg


class MadameLeFigaro(AbstractScraper):

    class _CustomSchemaOrg(SchemaOrg):
        def _extract_howto_instructions_text(self, schema_item):
            if (
                isinstance(schema_item, dict)
                and schema_item.get("@type") == "HowToStep"
            ):
                name = schema_item.get("name")
                text = schema_item.get("text")
                if (
                    isinstance(name, str)
                    and isinstance(text, str)
                    and name.strip()
                    and text.strip()
                    and not text.startswith(name.rstrip("."))
                ):
                    return [f"{name.strip()}: {text.strip()}"]
            return super()._extract_howto_instructions_text(schema_item)

    _schema_cls = _CustomSchemaOrg

    @classmethod
    def host(cls):
        return "madame.lefigaro.fr"
