import functools
import warnings

from recipe_scrapers._exceptions import (
    FieldNotProvidedByWebsiteException,
    StaticValueException,
)
from recipe_scrapers._warnings import (
    FieldNotProvidedByWebsiteWarning,
    StaticValueWarning,
)
from recipe_scrapers.plugins._interface import PluginInterface


class StaticValueExceptionHandlingPlugin(PluginInterface):
    """
    Handles cases where a scraper indicates that it returns a static value --
    perhaps because the website never provides info for that method at all
    (communicated by FieldNotProvidedByWebsiteException), or because for some
    reason it is easier or more convenient to define statically (communicated
    by StaticValueException).

    Objects of StaticValueException and subclasses include a return value, so
    we return that to the caller instead after emitting a suitable warning for
    use by developers/users.
    """

    BUG_REPORT_LINK = "https://github.com/hhursev/recipe-scrapers/issues"

    run_on_hosts = ("*",)
    run_on_methods = (
        "author",
        "site_name",
        "language",
        "cuisine",
        "cooking_method",
        "total_time",
        "yields",
    )

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            try:
                return decorated(self, *args, **kwargs)
            except FieldNotProvidedByWebsiteException as e:
                message = (
                    f"{self.host()} doesn't seem to support the {decorated.__name__} field. "
                    "If you know this to be untrue for some recipe, please submit a bug report at "
                    f"{StaticValueExceptionHandlingPlugin.BUG_REPORT_LINK}"
                )
                warnings.warn(
                    message=message, category=FieldNotProvidedByWebsiteWarning
                )
                return e.return_value
            except StaticValueException as e:
                message = (
                    f"{self.host()} returns a constant value from the {decorated.__name__} field. "
                    "If you believe we can and should determine that dynamically, please submit a "
                    f"bug report at {StaticValueExceptionHandlingPlugin.BUG_REPORT_LINK}"
                )
                warnings.warn(message=message, category=StaticValueWarning)
                return e.return_value

        return decorated_method_wrapper
