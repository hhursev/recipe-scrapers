import functools
import logging

from .._utils import normalize_string
from ._interface import PluginInterface


class NormalizeStringPlugin(PluginInterface):
    """
    TODO: write docstring
    """

    decorate_hosts = ("*",)
    run_on_methods = ("title",)

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            # TODO: write logging. Configure logging.
            logging.debug("TODO: write", exc_info=True)
            return normalize_string(decorated(self, *args, **kwargs))

        return decorated_method_wrapper
