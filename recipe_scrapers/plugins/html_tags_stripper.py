import functools
import logging
from html.parser import HTMLParser
from io import StringIO

from recipe_scrapers.settings import settings

from ._interface import PluginInterface

logging.basicConfig()
logger = logging.getLogger(__name__)


# Taken from @jksimoniii 's PR:
# - https://github.com/hhursev/recipe-scrapers/pull/346
# Modified to use the new "Plugin" system
# Taken from https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False  # this setting appears to do nothing
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def stripper(string):
    # Deal with HTML and HTML Encoded Characters
    string = strip_tags(
        f"<tag>{string}<tag>"
    )  # This is a workaround, since HTMLParser expects valid markup
    string = strip_tags(
        f"<tag>{string}<tag>"
    )  # This is another workaround, handles "&amp;amp;"

    return string


class HTMLTagStripperPlugin(PluginInterface):
    """
    Run the output from the methods listed through the stripper function
    defined above.

    It is intended to strip away <html><tags></tags></html> seen inside the strings.
    We do not want em.
    """

    decorate_hosts = ("*",)
    run_on_methods = ("title", "instructions", "ingredients")

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            logger.setLevel(settings.LOG_LEVEL)
            class_name = self.__class__.__name__
            method_name = decorated.__name__
            logger.debug(
                f"Decorating: {class_name}.{method_name}() with HTMLTagStripperPlugin plugin."
            )

            decorated_func_result = decorated(self, *args, **kwargs)

            if type(decorated_func_result) is list:
                return [stripper(item) for item in decorated_func_result]
            else:
                return stripper(decorated_func_result)

        return decorated_method_wrapper
