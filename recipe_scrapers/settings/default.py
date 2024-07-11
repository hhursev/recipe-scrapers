from recipe_scrapers.plugins import (
    ExceptionHandlingPlugin,
    HTMLTagStripperPlugin,
    NormalizeStringPlugin,
    OpenGraphFillPlugin,
    OpenGraphImageFetchPlugin,
    SchemaOrgFillPlugin,
    StaticValueExceptionHandlingPlugin,
)

# Plugins to be attached.
# The upper most plugin is the "outer most" executed.
# Check recipe_scrapers.settings.template.py for ways to extend.
PLUGINS = (
    ExceptionHandlingPlugin,
    StaticValueExceptionHandlingPlugin,
    HTMLTagStripperPlugin,
    NormalizeStringPlugin,
    OpenGraphImageFetchPlugin,
    OpenGraphFillPlugin,
    SchemaOrgFillPlugin,
)

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
    "instructions_list": None,
    "ratings": None,
    "reviews": None,
    "links": None,
    "language": None,
    "nutrients": None,
}


# logging.DEBUG     # 10
# logging.INFO      # 20
# logging.WARNING   # 30
# logging.ERROR     # 40
# logging.CRITICAL  # 50
# https://docs.python.org/3/howto/logging.html
LOG_LEVEL = 30
