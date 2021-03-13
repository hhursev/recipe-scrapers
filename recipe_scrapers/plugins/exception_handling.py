import functools
import logging

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


class ExceptionHandlingPlugin:
    """
    TODO: write docstring
    """

    run_on_methods = (
        "title",
        "total_time",
        "yields",
        "image",
        "ingredients",
        "instructions",
        "ratings",
        "reviews",
        "links",
        "language",
        "nutrients",
    )

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            if self.exception_handling:
                try:
                    return decorated(self, *args, **kwargs)
                except Exception as e:
                    # TODO: write logging. Configure logging.
                    logging.debug(f"TODO: write {str(e)}", exc_info=True)
                    return ON_EXCEPTION_RETURN_VALUES.get(decorated.__name__, None)
            return decorated(self, *args, **kwargs)

        return decorated_method_wrapper
