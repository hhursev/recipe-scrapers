import functools
import logging

from ._interface import PluginInterface


class SchemaOrgFill(PluginInterface):
    """
    TODO: write docstring

    If data not found in html, auto-try with Schema.org if data available
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
            try:
                return decorated(self, *args, **kwargs)
            except NotImplementedError as e:
                function = getattr(self.schema, decorated.__name__)
                if self.schema.data and function:
                    # TODO: write logging. Configure logging.
                    logging.debug("TODO: write", exc_info=True)
                    return function(*args, **kwargs)
                else:
                    raise e

        return decorated_method_wrapper
