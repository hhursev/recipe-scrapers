from recipe_scrapers.plugins import (  # SchemaOrgPrioriotyPlugin,
    Bcp47ValidatePlugin,
    ExceptionHandlingPlugin,
    HTMLTagStripper,
    NormalizeStringPlugin,
    OpenGraphImageFetchPlugin,
    SchemaOrgFill,
)

PLUGINS = (
    ExceptionHandlingPlugin,
    HTMLTagStripper,
    NormalizeStringPlugin,
    OpenGraphImageFetchPlugin,
    Bcp47ValidatePlugin,
    SchemaOrgFill,
    # SchemaOrgPrioriotyPlugin,
)


EXCEPTION_HANDLING = False
META_HTTP_EQUIV = False
TEST_MODE = False

# Applicable only if EXCEPTION_HANDLING is True
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
