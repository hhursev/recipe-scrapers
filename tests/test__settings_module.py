import os
import unittest

from recipe_scrapers.settings import settings


class SettingsModuleTest(unittest.TestCase):
    def test_default_settings(self):

        os.environ["RECIPE_SCRAPERS_SETTINGS"] = "recipe_scrapers.settings.default"

        self.assertTrue(
            len(settings.PLUGINS) > 0,
            "There should be some plugins in the default project's settings",
        )

        self.assertFalse(
            settings.SUPPRESS_EXCEPTIONS,
            "SUPPRESS_EXCEPTIONS should be set to False in the project's default settings",
        )

    def test_settings_change_when_new_module_set(self):
        self.assertFalse(
            settings.SUPPRESS_EXCEPTIONS,
            "SUPPRESS_EXCEPTIONS should be set to False in the project's default settings",
        )

        os.environ[
            "RECIPE_SCRAPERS_SETTINGS"
        ] = "tests.test_data.test_settings_module.test_settings"

        self.assertTrue(
            settings.SUPPRESS_EXCEPTIONS,
            "SUPPRESS_EXCEPTIONS should be set to True after settings are changed with the testing ones",
        )
