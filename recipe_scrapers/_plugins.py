from .plugins import (  # SchemaOrgPrioriotyPlugin,
    Bcp47ValidatePlugin,
    ExceptionHandlingPlugin,
    NormalizeStringPlugin,
    OpenGraphImageFetchPlugin,
    SchemaOrgFill,
)


class PluginsRunner(type):
    """
    TODO: write docstring
    """

    plugins = (
        ExceptionHandlingPlugin,
        NormalizeStringPlugin,
        OpenGraphImageFetchPlugin,
        Bcp47ValidatePlugin,
        SchemaOrgFill,
        # SchemaOrgPrioriotyPlugin,
    )

    def __new__(cls, class_name, bases, attributes):
        for key, value in attributes.items():
            for plugin in reversed(cls.plugins):
                if key in plugin.run_on_methods:
                    current_method = attributes.get(key)
                    attributes.update({key: plugin.run(current_method)})
        return type.__new__(cls, class_name, bases, attributes)
