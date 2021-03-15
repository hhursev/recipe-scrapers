import functools
import logging

from .._schemaorg import SchemaOrgException
from ._interface import PluginInterface


class SchemaOrgPrioriotyPlugin(PluginInterface):
    """
    TODO: write docstring
    """

    run_on_hosts = ("*",)
    run_on_methods = (
        "author",
        "title",
        "total_time",
        "yields",
        "image",
        "ingredients",
        "instructions",
        "ratings",
        "reviews",
        "links",
        "language",
        "nutrients",
    )

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            function = getattr(self.schema, decorated.__name__)
            if self.schema.data and function:
                # TODO: write logging. Configure logging.
                logging.debug("TODO: write", exc_info=True)
                try:
                    return function(*args, **kwargs)
                except SchemaOrgException:
                    return decorated(self, *args, **kwargs)
            else:
                return decorated(self, *args, **kwargs)

        return decorated_method_wrapper
