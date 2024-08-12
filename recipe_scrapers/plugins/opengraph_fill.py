import functools
import logging

from recipe_scrapers._exceptions import FillPluginException
from recipe_scrapers.settings import settings

from ._interface import PluginInterface

logging.basicConfig()
logger = logging.getLogger(__name__)


class OpenGraphFillPlugin(PluginInterface):
    """
    If any of the methods listed is invoked on a scraper class
    that happens not to be implemented, attempt to return results
    by checking for OpenGraph metadata.
    """

    run_on_hosts = ("*",)
    run_on_methods = (
        "site_name",
        "image",
    )

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            logger.setLevel(settings.LOG_LEVEL)
            class_name = self.__class__.__name__
            method_name = decorated.__name__
            logger.debug(
                f"Decorating: {class_name}.{method_name}() with OpenGraphFillPlugin"
            )

            try:
                return decorated(self, *args, **kwargs)
            except (FillPluginException, NotImplementedError) as e:
                function = getattr(self.opengraph, decorated.__name__)
                if self.opengraph.soup and function:
                    logger.info(
                        f"{class_name}.{method_name}() seems not to be implemented but OpenGraph metadata may be available. Attempting to return result from OpenGraph."
                    )
                    return function(*args, **kwargs)
                else:
                    raise e

        return decorated_method_wrapper
