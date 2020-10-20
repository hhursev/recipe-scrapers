import logging
import functools


ON_EXCEPTION_RETURN_VALUES = {
    "title": "",
    "total_time": 0,
    "yields": "",
    "image": "",
    "ingredients": [],
    "instructions": "",
    "ratings": -1,
    "reviews": None,
    "links": [],
    "language": "en",
}


def exception_handling(decorated):
    @functools.wraps(decorated)
    def exception_handling_wrapper(self, *args, **kwargs):
        if self.exception_handling:
            try:
                return decorated(self, *args, **kwargs)
            except Exception as e:
                logging.info("exception_handling silencing exception: {}".format(e))
                logging.debug(
                    "exception_handling silencing exception: {}".format(e),
                    exc_info=True,
                )
                return ON_EXCEPTION_RETURN_VALUES.get(decorated.__name__)
        else:
            return decorated(self, *args, **kwargs)

    return exception_handling_wrapper


class ExceptionHandlingMetaclass(type):
    """
    As web scraping is too unpredictable in nature, handle
    whatever exceptions may arise with defaulting values.

    This metaclass will decorate all methods with names found in
    ON_EXCEPTION_RETURN_VALUES, to return the corresponding value
    if exception occurs.

    -----

    If you wish to handle exceptions on your own you can pass the
    exception_handling=False flag or write exception_handling
    function of your own.

    Example:
    from recipe_scrapers import scrape_me
    scraper = scrape_me('<recipe_url>', exception_handling=False)
    scraper.total_time()  # and etc.
    """

    def __new__(cls, class_name, bases, attributes):
        """
        Go through all class attributes.
        If the attribute name is in the ON_EXCEPTION_RETURN_VALUES.keys
        Decorate the "code" behind that attribute name with exception_handling.
        """
        for key, value in attributes.items():
            if key in ON_EXCEPTION_RETURN_VALUES.keys():
                attributes.update({key: exception_handling(value)})
        return type.__new__(cls, class_name, bases, attributes)
