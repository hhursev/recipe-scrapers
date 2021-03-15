import functools
import logging

from ._interface import PluginInterface


class ExceptionHandlingPlugin(PluginInterface):
    """
    TODO: write docstring
    """

    run_on_hosts = ("*",)
    run_on_methods = (
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
            from recipe_scrapers.settings import settings

            if self.exception_handling or settings.EXCEPTION_HANDLING:
                try:
                    return decorated(self, *args, **kwargs)
                except Exception as e:
                    # TODO: write logging. Configure logging.
                    logging.debug(f"TODO: write {str(e)}", exc_info=True)
                    return settings.ON_EXCEPTION_RETURN_VALUES.get(
                        decorated.__name__, None
                    )
            return decorated(self, *args, **kwargs)

        return decorated_method_wrapper
