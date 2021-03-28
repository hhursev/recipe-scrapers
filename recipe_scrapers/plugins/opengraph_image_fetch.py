import functools
import logging

from recipe_scrapers.settings import settings

from ._interface import PluginInterface

logging.basicConfig()
logger = logging.getLogger(__name__)


class OpenGraphImageFetchPlugin(PluginInterface):
    """
    If .image() method on whatever scraper return exception for some reason,
    do try to fetch the recipe image from the og:image on the page.

    Apply to .image() method on all scrapers if plugin is active.
    """

    run_on_hosts = ("*",)
    run_on_methods = ("image",)

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            logger.setLevel(settings.LOG_LEVEL)
            class_name = self.__class__.__name__
            method_name = decorated.__name__
            logger.debug(
                f"Decorating: {class_name}.{method_name}() with OpenGraphImageFetchPlugin"
            )

            image = None
            try:
                image = decorated(self, *args, **kwargs)
            except Exception:
                pass

            if image:
                return image
            else:
                logger.info(
                    f"{class_name}.{method_name}() did not manage to find recipe image. OpenGraphImageFetchPlugin will attempt to do its magic."
                )
                image = self.soup.find(
                    "meta", {"property": "og:image", "content": True}
                )
                return image.get("content")

        return decorated_method_wrapper
