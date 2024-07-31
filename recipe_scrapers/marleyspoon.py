import json
import re
from urllib.parse import urljoin

import requests

from ._abstract import HEADERS, AbstractScraper
from ._exceptions import ElementNotFoundInHtml, RecipeScrapersExceptions
from ._utils import get_host_name, normalize_string

ID_PATTERN = re.compile(r"/(\d+)-")
SCRIPT_PATTERN = re.compile(
    'gon\\.current_brand="(?P<brand>[^"]+?)".*?'
    'gon\\.current_country="(?P<country>[^"]+?)".*?'
    'gon\\.api_token="(?P<token>[^"]+?)".*?'
    'gon\\.api_host="(?P<host>[^"]+?)".*?'
)

PREPARATION_DICT = {  # these values I was able to retrieve from website
    "time_level_1": 10,  # on the website they are displayed like `5-10 minutes`, I used avg or similar rounded value
    "time_level_2": 15,
    "time_level_3": 20,
    "time_level_4": 25,
    "time_level_5": 35,
}


class MarleySpoon(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, proxies=proxies, timeout=timeout, *args, **kwargs)

        # The website's html does not contain any recipe data, but it loads it with a json request.
        # We read the request parameters from html and preform additional request it to fetch recipe data.
        api_url, api_token = self._get_json_params()
        self.page_data = requests.get(
            api_url,
            headers={"authorization": api_token, **HEADERS},
            proxies=proxies,
            timeout=timeout,
        ).content

        self.data = json.loads(self.page_data)

    def _get_json_params(self):
        recipe_id = None
        api_url = None
        api_token = None

        match = ID_PATTERN.search(self.canonical_url())
        if match:
            recipe_id = match.group(1)

        scripts = self.soup.find_all("script")
        for script in scripts:
            matches = SCRIPT_PATTERN.search(str(script.string))
            if matches:
                data = matches.groupdict()
                host = data["host"].replace("\\", "")
                api_url = f"{host}/recipes/{recipe_id}?brand={data['brand']}&country={data['country']}&product_type=web"
                api_token = f"Bearer {data['token']}"

        if recipe_id is None:
            raise ElementNotFoundInHtml("Recipe ID is unknown.")

        if api_url is None or api_token is None:
            raise ElementNotFoundInHtml("Required script not found.")

        from . import SCRAPERS

        scraper_name = self.__class__.__name__
        try:
            next_url = urljoin(self.url, api_url)
            host_name = get_host_name(next_url)
            next_scraper = type(None)
            # check: api.foo.xx.example, foo.xx.example, xx.example
            while host_name and host_name.count("."):
                next_scraper = SCRAPERS.get(host_name)
                if next_scraper:
                    break
                _, host_name = host_name.split(".", 1)
            if not isinstance(self, next_scraper):
                msg = f"Attempted to scrape using {next_scraper} from {scraper_name}"
                raise ValueError(msg)
        except Exception as e:
            raise RecipeScrapersExceptions(f"Unexpected API URL: {api_url}") from e

        return api_url, api_token

    @classmethod
    def host(cls, domain="com"):
        return f"marleyspoon.{domain}"

    def title(self):
        return self.data.get("name_with_subtitle")

    def total_time(self):
        return PREPARATION_DICT.get(self.data.get("preparation_time"), 60)

    def yields(self):
        # The backend of MarleySpoon always returns ingredients for 2 servings
        # This conclusion is made based on personal observations and available plans https://marleyspoon.com/select-plan
        return "2 servings"

    def image(self):
        return self.data.get("image").get("large")

    def nutrients(self):
        return self.data.get("nutrition")

    def ingredients(self):
        ingredients = [
            normalize_string(ingredient.get("name"))
            for ingredient in self.data.get("ingredients")
        ]
        assumed = [
            normalize_string(ingredient.get("name"))
            for ingredient in self.data.get("assumed_ingredients")
        ]
        return ingredients + assumed

    def instructions(self):
        return "\n".join(
            [
                normalize_string(instruction.get("description").replace("__", ""))
                for instruction in self.data.get("steps")
            ]
        )

    def author(self):
        return self.data.get("chef").get("name")

    def description(self):
        return self.data.get("description")

    def links(self):
        links = super().links()
        # this is a useful link to a print card, maybe someone needs it
        links.append({"href": self.data.get("recipe_card_url")})
        return links

    def language(self):
        try:
            # in normal scenario, there will be html `lang` tag and language can be retrieved from it
            return super().language()
        except AttributeError:
            # but during the test, we load json as main resource, but using the `country` property, we can guess it
            return self.data.get("country")
