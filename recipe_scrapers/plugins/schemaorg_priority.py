import functools

from recipe_scrapers.settings import settings

from .._exceptions import SchemaOrgException
from ._interface import PluginInterface


class SchemaOrgPriorityPlugin(PluginInterface):
    """
    Plugin that if put into use will check if there's Schema.org
    available on the page being scraped.

    If Schema.org is available, it will ignore the methods in the
    site-specific scraper and use the SchemaOrg instead.

    If SchemaOrg raises SchemaOrgException for some reason, the plugin
    will fallback to the method used in the site-specific scraper.

    In the ideal future every site implements Schema.org, but we are no there yet.
    """

    run_on_hosts = ("*",)
    run_on_methods = (
        "author",
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
            function = getattr(self.schema, decorated.__name__)
            if self.schema.data and function:
                # TODO: write logging. Configure logging.
                settings.logger.debug("TODO: write", exc_info=True)
                try:
                    return function(*args, **kwargs)
                except SchemaOrgException:
                    return decorated(self, *args, **kwargs)
            else:
                return decorated(self, *args, **kwargs)

        return decorated_method_wrapper
