import functools
import logging

from recipe_scrapers.settings import settings

from .._utils import normalize_string
from ._interface import PluginInterface

logging.basicConfig()
logger = logging.getLogger(__name__)


class NormalizeStringPlugin(PluginInterface):
    """
    Explicitly run the output from the methods listed through normalize_string
    """

    decorate_hosts = ("*",)
    run_on_methods = ("title",)

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            # TODO: write logging. Configure logging.
            logger.setLevel(settings.LOG_LEVEL)
            class_name = self.__class__.__name__
            method_name = decorated.__name__
            logger.debug(
                f"Decorating: {class_name}.{method_name}() with NormalizeStringPlugin"
            )

            return normalize_string(decorated(self, *args, **kwargs))

        return decorated_method_wrapper
