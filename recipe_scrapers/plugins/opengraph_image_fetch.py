import functools
import logging

from ._interface import PluginInterface


class OpenGraphImageFetchPlugin(PluginInterface):
    """
    TODO: write docstring
    """

    run_on_hosts = ("*",)
    run_on_methods = ("image",)

    @classmethod
    def run(cls, decorated):
        @functools.wraps(decorated)
        def decorated_method_wrapper(self, *args, **kwargs):
            image = None
            try:
                image = decorated(self, *args, **kwargs)
            except Exception:
                pass

            if image:
                return image
            else:
                # TODO: write logging. Configure logging.
                logging.debug("TODO: write", exc_info=True)
                image = self.soup.find(
                    "meta", {"property": "og:image", "content": True}
                )
                return image.get("content")

        return decorated_method_wrapper
