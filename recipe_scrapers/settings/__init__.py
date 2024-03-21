import importlib
import os
from typing import Any


class RecipeScraperSettings:
    """
    Allowing users to configure package settings when using recipe-scraper
    without the need of touching the core package.

    Similar to django's settings module but simpler.

    Users can write settings in simple python format and using python expressions.
    User defined settings can be saved in whatever python settings module / .py file
    and then used by changing the env variable
    "RECIPE_SCRAPERS_SETTINGS" to point to them:
    os.environ["RECIPE_SCRAPERS_SETTINGS"] = "path.to.my.custom.settings.file" [py]

    This will make the package start using the user-defined settings instantly.

    Access package's settings with

    from recipe_scrapers.settings import settings
    # settings.LOG_LEVEL
    # settings.PLUGINS etc. (check recipe_scrapers/settings/default.py for more info)

    Users can easily add Plugins of their own and add/test extra scraper functionality
    as they find fit.
    """

    def __init__(self, *args: Any, **kwargs: Any):
        self._configured = False
        self._user_settings = False
        super().__init__(*args, **kwargs)

    def __getattribute__(self, item: Any) -> Any:
        if item.startswith("_"):
            return super().__getattribute__(item)

        # if settings haven't yet been configured or RECIPE_SCRAPERS_SETTINGS
        # environment has been changed, reconfigure settings before returning
        user_defined_settings = os.environ.get("RECIPE_SCRAPERS_SETTINGS", False)
        if not self._configured or user_defined_settings != getattr(
            self, "_user_settings"
        ):
            self._configure()
            return super().__getattribute__(item)

        return super().__getattribute__(item)

    def _configure(self) -> None:
        # configure the default settings by default
        if not getattr(self, "_configured"):
            default_settings = importlib.import_module(
                "recipe_scrapers.settings.default"
            )
            for item in dir(default_settings):
                if item.isupper():
                    setattr(self, item, getattr(default_settings, item))
            self._configured = True

        # if user-specific given given, overwrite the default ones
        user_settings = os.environ.get("RECIPE_SCRAPERS_SETTINGS", False)
        if user_settings != getattr(self, "_user_settings"):
            setattr(self, "_user_settings", user_settings)
            user_settings = importlib.import_module(user_settings)  # type: ignore [arg-type,assignment]
            for item in dir(user_settings):
                if item.isupper():
                    setattr(self, item, getattr(user_settings, item))


settings = RecipeScraperSettings()


__all__ = ["settings"]
