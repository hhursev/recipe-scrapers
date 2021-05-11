import functools

from language_tags import tags

from ._interface import PluginInterface


class Bcp47ValidatePlugin(PluginInterface):
    """
    If you wish to use this plugin make sure you
    pip install language-tags>=1.0.0

    Validates if the value returned by .language() is a truthfully a language abbreviation
    For more info read https://github.com/OnroerendErfgoed/language-tags and the corresponding links there

    - https://tools.ietf.org/html/bcp47
    - https://tools.ietf.org/html/rfc5646
    - https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry
    """

    run_on_hosts = ("*",)
    run_on_methods = ("language",)

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            tag = tags.tag(decorated(self, *args, **kwargs))
            return str(tag) if tag.valid else None

        return decorated_method_wrapper
