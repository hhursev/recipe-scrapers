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

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
