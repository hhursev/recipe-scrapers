import importlib
import os


class RecipeScraperSettings:
    """
    TODO: write docstring
    """

    def __init__(self, *args, **kwargs):
        self._configured = False
        self._user_settings = False
        self.configure()
        super().__init__(*args, **kwargs)

    def configure(self):
        if not getattr(self, "_configured"):
            default_settings = importlib.import_module(
                "recipe_scrapers.settings.default"
            )
            for item in dir(default_settings):
                if item.isupper():
                    setattr(self, item, getattr(default_settings, item))
            self._configured = True

        user_settings = os.environ.get("RECIPE_SCRAPERS_SETTINGS", False)
        if user_settings != getattr(self, "_user_settings"):
            setattr(self, "_user_settings", user_settings)
            user_settings = importlib.import_module(user_settings)
            for item in dir(user_settings):
                if item.isupper():
                    setattr(self, item, getattr(user_settings, item))


settings = RecipeScraperSettings()


__all__ = ["settings"]
