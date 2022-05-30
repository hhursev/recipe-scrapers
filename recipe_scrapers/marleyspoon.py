import json
import re
import requests

from ._abstract import AbstractScraper, HEADERS
from ._exceptions import ElementNotFoundInHtml
from ._utils import normalize_string

SCRIPT_PATTERN = re.compile("gon\\.current_brand=\"(?P<brand>[^\"]+?)\".*?"
                            "gon\\.current_country=\"(?P<country>[^\"]+?)\".*?"
                            "gon\\.api_token=\"(?P<token>[^\"]+?)\".*?"
                            "gon\\.api_host=\"(?P<host>[^\"]+?)\".*?")

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

        if url != "https://test.example.com/":  # skip during the test, we will test the method separately
            # The website's html does not contain any recipe data, but it loads it with a json request.
            # We read the request parameters from html and preform additional request it to fetch recipe data.
            api_url, api_token = self._get_json_params()
            self.page_data = requests.get(
                api_url, headers={"authorization": api_token, **HEADERS}, proxies=proxies, timeout=timeout
            ).content

        self.data = json.loads(self.page_data)

    def _get_json_params(self):
        api_url = None
        api_token = None

        scripts = self.soup.find_all("script")
        for script in scripts:
            matches = SCRIPT_PATTERN.search(str(script.string))
            if matches:
                data = matches.groupdict()
                api_url = (f"{data['host']}/recipes/113813?brand={data['brand']}&country={data['country']}"
                           f"&product_type=web").replace("\\", "")
                api_token = f"Bearer {data['token']}"

        if api_url is None or api_token is None:
            raise ElementNotFoundInHtml("Required script not found.")

        return api_url, api_token

    @classmethod
    def host(cls, domain="com"):
        return f"marleyspoon.{domain}"

    def title(self):
        return self.data.get("name_with_subtitle")

    def total_time(self):
        return PREPARATION_DICT.get(self.data.get("preparation_time"), 60)

    def yields(self):
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
                normalize_string(instruction.get("description"))
                for instruction in self.data.get("steps")
            ]
        )

    def author(self):
        return self.data.get("chef").get("name")

    def description(self):
        return self.data.get("description")

    def links(self):
        links = super().links()
        links.append({"href": self.data.get("recipe_card_url")})
        return links
