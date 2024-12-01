import functools
import logging

from recipe_scrapers._exceptions import FillPluginException, RecipeSchemaNotFound
from recipe_scrapers.settings import settings

from ._interface import PluginInterface

logging.basicConfig()
logger = logging.getLogger(__name__)


class SchemaOrgFillPlugin(PluginInterface):
    """
    If any of the methods listed is invoked on a scraper class
    that happens not to be implement and Schema.org is available
    attempt to return the results from the schema available.
    """

    run_on_hosts = ("*",)
    run_on_methods = (
        "author",
        "site_name",
        "title",
        "category",
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
        "cooking_method",
        "cuisine",
        "description",
        "cook_time",
        "prep_time",
        "keywords",
        "ratings_count",
        "dietary_restrictions",
    )

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            logger.setLevel(settings.LOG_LEVEL)
            class_name = self.__class__.__name__
            method_name = decorated.__name__
            logger.debug(
                f"Decorating: {class_name}.{method_name}() with SchemaOrgFillPlugin"
            )
            try:
                return decorated(self, *args, **kwargs)
            except (FillPluginException, NotImplementedError) as e:
                function = getattr(self.schema, decorated.__name__)
                if not self.schema.data:
                    raise RecipeSchemaNotFound(url=self.url)
                if function:
                    logger.info(
                        f"{class_name}.{method_name}() seems to not be implemented but .schema is available! Attempting to return result from SchemaOrg."
                    )
                    return function(*args, **kwargs)
                else:
                    raise e

        return decorated_method_wrapper
