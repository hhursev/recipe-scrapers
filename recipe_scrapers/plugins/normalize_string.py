import functools
import logging

from .._utils import normalize_string


class NormalizeStringPlugin:
    """
    TODO: write docstring
    """

    run_on_methods = ("title",)

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            # TODO: write logging. Configure logging.
            logging.debug("TODO: write", exc_info=True)
            return normalize_string(decorated(self, *args, **kwargs))

        return decorated_method_wrapper
