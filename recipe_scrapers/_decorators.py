import functools
from language_tags import tags

from ._schemaorg import SchemaOrgException
from ._utils import normalize_string


class Decorators:
    @staticmethod
    def schema_org_priority(decorated):
        """
        Use SchemaOrg parser with priority (if there's data in it)
        On exception raised - continue by default.
        If there's no data (no schema implemented on the site) - continue by default
        """

        @functools.wraps(decorated)
        def schema_org_priority_wrapper(self, *args, **kwargs):
            function = getattr(self.schema, decorated.__name__)
            if not function:
                raise SchemaOrgException(
                    "Function '{}' not found in schema".format(decorated.__name)
                )

            if not self.schema.data:
                return decorated(self, *args, **kwargs)

            try:
                value = function(*args, **kwargs)
            except SchemaOrgException:
                return decorated(self, *args, **kwargs)
            return value or decorated(self, *args, **kwargs)

        return schema_org_priority_wrapper

    @staticmethod
    def og_image_get(decorated):
        @functools.wraps(decorated)
        def og_image_get_wrapper(self, *args, **kwargs):
            try:
                image = self.soup.find(
                    "meta", {"property": "og:image", "content": True}
                )
                return image.get("content")
            except AttributeError:
                return decorated(self, *args, **kwargs)

        return og_image_get_wrapper

    @staticmethod
    def bcp47_validate(decorated):
        @functools.wraps(decorated)
        def bcp47_validate_wrapper(self, *args, **kwargs):
            tag = tags.tag(decorated(self, *args, **kwargs))
            return str(tag) if tag.valid else None

        return bcp47_validate_wrapper

    @staticmethod
    def normalize_string_output(decorated):
        @functools.wraps(decorated)
        def normalize_string_output_wrapper(self, *args, **kwargs):
            return normalize_string(decorated(self, *args, **kwargs))

        return normalize_string_output_wrapper
