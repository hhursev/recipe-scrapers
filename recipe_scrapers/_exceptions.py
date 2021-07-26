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
    """Error when wild_mode fails to locate schema at the url"""

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


class SchemaOrgException(RecipeScrapersExceptions):
    """Error in parsing or missing portion of the Schema.org data org the page"""

    def __init__(self, message):
        super().__init__(message)
