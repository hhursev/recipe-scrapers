from recipe_scrapers.plugins import (  # SchemaOrgPriorityPlugin,; Bcp47ValidatePlugin,
    ExceptionHandlingPlugin,
    HTMLTagStripperPlugin,
    NormalizeStringPlugin,
    OpenGraphImageFetchPlugin,
    SchemaOrgFillPlugin,
)

# Plugins to be attached.
# The upper most plugin is the "outer most" executed.
# Check recipe_scrapers.settings.template.py for ways to extend.
PLUGINS = (
    ExceptionHandlingPlugin,
    HTMLTagStripperPlugin,
    NormalizeStringPlugin,
    OpenGraphImageFetchPlugin,
    SchemaOrgFillPlugin,
    # Bcp47ValidatePlugin,
    # SchemaOrgPriorityPlugin,
)

META_HTTP_EQUIV = True


SUPPRESS_EXCEPTIONS = False
# Applicable only if SUPPRESS_EXCEPTIONS is True, otherwise ignored
# silence <anyScraper>.[method]() exception and return the value
# as listed in the config here.
ON_EXCEPTION_RETURN_VALUES = {
    "title": None,
    "total_time": None,
    "yields": None,
    "image": None,
    "ingredients": None,
    "instructions": None,
    "ratings": None,
    "reviews": None,
    "links": None,
    "language": None,
    "nutrients": None,
}


TEST_MODE = False


# logging.DEBUG     # 10
# logging.INFO      # 20
# logging.WARNING   # 30
# logging.ERROR     # 40
# logging.CRITICAL  # 50
# https://docs.python.org/3/howto/logging.html
LOG_LEVEL = 30
