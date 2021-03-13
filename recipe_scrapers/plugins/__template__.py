import functools
from typing import Tuple


class PluginTemplate:
    """
    write docstring
    """

    run_on_methods: Tuple = (
        "title",
        # ... others
    )

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            # in here you'll have self.soup, self.schema and the other
            # instance attributes/methods you can work with.
            # check other plugins for examples
            return decorated(self, *args, **kwargs)

        return decorated_method_wrapper
