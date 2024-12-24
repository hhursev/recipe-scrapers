import functools
import logging

from recipe_scrapers.settings import settings

from ._interface import PluginInterface

logging.basicConfig()
logger = logging.getLogger(__name__)


class ExceptionHandlingPlugin(PluginInterface):
    """
    Plugin that is used only if settings.SUPPRESS_EXCEPTIONS is set to True.

    The outer-most plugin and decorator.

    If ANY of the methods listed raises ANY kind of exception, silence it
    and return the respective value from settings.ON_EXCEPTION_RETURN_VALUES

    If settings.SUPPRESS_EXCEPTIONS is set to False this plugin is ignored and
    does nothing. (In other words exceptions won't be handled and will bubble up
    to program's explosion. Left to the end-user to handle them on his own).
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
            if settings.SUPPRESS_EXCEPTIONS:
                logger.setLevel(settings.LOG_LEVEL)
                class_name = self.__class__.__name__
                method_name = decorated.__name__
                logger.debug(
                    f"Decorating: {class_name}.{method_name}() with ExceptionHandlingPlugin"
                )

                try:
                    return decorated(self, *args, **kwargs)
                except Exception as e:
                    logger.info(
                        f"ExceptionHandlingPlugin silenced exception: {str(e)} in {class_name}.{method_name}()"
                    )

                    return settings.ON_EXCEPTION_RETURN_VALUES.get(
                        decorated.__name__, None
                    )
            return decorated(self, *args, **kwargs)

        return decorated_method_wrapper
