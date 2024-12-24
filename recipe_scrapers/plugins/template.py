import functools
import logging

from recipe_scrapers.plugins._interface import PluginInterface
from recipe_scrapers.settings import settings

logging.basicConfig()
logger = logging.getLogger(__name__)


class TemplatePlugin(PluginInterface):
    """
    Sample starting point to write your custom plugin.

    Check the available plugins implementations for more details.
    """

    run_on_hosts = ("*",)
    run_on_methods = (
        "title",
        # ... others
    )

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            # in here you'll have self.soup, self.schema and the other
            # instance attributes/methods you can work with.
            # check other plugins for examples
            logger.setLevel(settings.LOG_LEVEL)
            class_name = self.__class__.__name__
            method_name = decorated.__name__
            logger.debug(
                f"Decorating: {class_name}.{method_name}() with TemplatePlugin"
            )
            return decorated(self, *args, **kwargs)

        return decorated_method_wrapper
