import inspect
import json
from typing import Optional, Tuple, Union

import requests

from recipe_scrapers.settings import settings

from ._abstract import AbstractScraper
from ._schemaorg import SchemaOrg
from ._utils import url_path_to_dict

# some sites close their content for 'bots', so user-agent must be supplied
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}


class Woolworths(AbstractScraper):
    def __init__(
        self,
        url,
        proxies: Optional[str] = None,  # allows us to specify optional proxy server
        timeout: Optional[
            Union[float, Tuple, None]
        ] = None,  # allows us to specify optional timeout for request
        wild_mode: Optional[bool] = False,
    ):
        if settings.TEST_MODE:  # when testing, we load a file
            page_data = url.read()
            url = "https://test.example.com/"
        else:
            # get the actual URL based on the provided input
            target = url_path_to_dict(url)["path"].split("/")[-1]
            url = "https://foodhub.woolworths.com.au/content/woolworths-foodhub/en/{0}.model.json".format(
                target
            )
            page_data = requests.get(
                url, headers=HEADERS, proxies=proxies, timeout=timeout
            ).content

        self.url = url
        page_data = (
            json.loads(page_data)
            .get(":items")
            .get("root")
            .get(":items")
            .get("recipe_seo_data")
        )
        self.schema = SchemaOrg(page_data, raw=True)

        # attach the plugins as instructed in settings.PLUGINS
        if not hasattr(self.__class__, "plugins_initialized"):
            for name, func in inspect.getmembers(self, inspect.ismethod):
                current_method = getattr(self.__class__, name)
                for plugin in reversed(settings.PLUGINS):
                    if plugin.should_run(self.host(), name):
                        current_method = plugin.run(current_method)
                setattr(self.__class__, name, current_method)
            setattr(self.__class__, "plugins_initialized", True)

    @classmethod
    def host(cls):
        return "woolworths.com.au"

    def canonical_url(self):
        return self.url

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def cook_time(self):
        return self.schema.cook_time()

    def prep_time(self):
        return self.schema.prep_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def nutrients(self):
        return self.schema.nutrients()

    def language(self):
        return "en-AU"

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def author(self):
        return self.schema.author()

    def reviews(self):
        return self.schema.reviews()

    def links(self):
        return []

    def site_name(self):
        return "Woolworths | Fresh Ideas For You"

    def cuisine(self):
        return self.schema.cuisine()
