from recipe_scrapers.settings import settings


class PluginsRunner(type):
    """
    TODO: write docstring
    """

    plugins = settings.plugins

    def __new__(cls, class_name, bases, attributes):
        for key, value in attributes.items():
            for plugin in reversed(cls.plugins):
                if key in plugin.run_on_methods:
                    current_method = attributes.get(key)
                    attributes.update({key: plugin.run(current_method)})
        return type.__new__(cls, class_name, bases, attributes)
