import functools

from recipe_scrapers.plugins._interface import PluginInterface


class TemplatePlugin(PluginInterface):
    """
    write docstring
    """

    run_on_hosts = ("*",)
    run_on_methods = (
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
