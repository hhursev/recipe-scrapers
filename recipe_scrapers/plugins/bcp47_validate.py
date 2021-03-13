import functools
import logging

from language_tags import tags


class Bcp47ValidatePlugin:
    """
    TODO: write docstring
    """

    run_on_methods = ("language",)

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            logging.debug("TODO: write", exc_info=True)
            tag = tags.tag(decorated(self, *args, **kwargs))
            return str(tag) if tag.valid else None

        return decorated_method_wrapper
