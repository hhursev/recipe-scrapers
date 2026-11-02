from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg


class EinfachKochen(AbstractScraper):
    class _CustomSchemaOrg(SchemaOrg):
        def _extract_howto_instructions_text(self, schema_item):
            if (
                isinstance(schema_item, dict)
                and schema_item.get("@type") == "HowToStep"
            ):
                text = schema_item.get("text")
                if isinstance(text, list):
                    text = ", ".join(t.strip() for t in text if t.strip())
                    schema_item = {**schema_item, "text": text}
            return super()._extract_howto_instructions_text(schema_item)

    _schema_cls = _CustomSchemaOrg

    @classmethod
    def host(cls):
        return "einfachkochen.de"
