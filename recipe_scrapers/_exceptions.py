class RecipeScrapersExceptions(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"recipe-scrapers exception: {self.message}"


class WebsiteNotImplementedError(RecipeScrapersExceptions):
    """Error when website is not supported by this library."""

    def __init__(self, domain):
        self.domain = domain
        message = f"Website ({self.domain}) not supported."
        super().__init__(message)


class NoSchemaFoundInWildMode(RecipeScrapersExceptions):
    """The scraper was unable to locate schema.org metadata within the webpage."""

    def __init__(self, url):
        self.url = url
        message = f"No Recipe Schema found at {self.url}."
        super().__init__(message)


class ElementNotFoundInHtml(RecipeScrapersExceptions):
    """Error when we cannot locate the HTML element on the page"""

    def __init__(self, element):
        self.element = element
        message = (
            "Element not found in html (self.soup.find returned None). Check traceback."
        )
        super().__init__(message)


class FillPluginException(RecipeScrapersExceptions):
    """Inability to locate an element on a page by using a fill plugin"""

    def __init__(self, message):
        super().__init__(message)


class OpenGraphException(FillPluginException):
    """Unable to locate element on the page using OpenGraph metadata"""

    ...


class SchemaOrgException(FillPluginException):
    """Error in parsing or missing portion of the Schema.org data on the page"""

    ...


class RecipeSchemaNotFound(SchemaOrgException):
    """No recipe schema metadata found on the page"""

    def __init__(self, url):
        self.url = url
        message = f"No Recipe Schema found at {self.url}."
        super().__init__(message)


class StaticValueException(RecipeScrapersExceptions):
    """Error to communicate that the scraper is returning a fixed/static value."""

    def __init__(self, *, return_value):
        self.return_value = return_value
        message = f"Suggested return value {return_value} is not from recipe source."
        super().__init__(message)


class FieldNotProvidedByWebsiteException(StaticValueException):
    """Error when, as far as we know, the website does not provide this info for any recipes."""

    ...
