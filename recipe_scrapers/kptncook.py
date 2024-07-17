from urllib.parse import parse_qs, urlparse

import requests

from ._abstract import AbstractScraper

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}
# These languages use measurements like cups and spoons rather than grams and liters
IMPERIAL_LANGUAGES = ["en"]
KPTN_DEFAULT_LANGUAGE = "en"


class KptnCook(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url, proxies=proxies, timeout=timeout, *args, **kwargs)
        parsed_url = urlparse(self.url)
        # Extract language from URL
        query = parse_qs(parsed_url.query)
        self.lang = query["lang"][0] if "lang" in query else KPTN_DEFAULT_LANGUAGE

        # Build final recipe url (of type mobile.kptncook.com/*)
        self.final_url = "".join(
            ["https://", parsed_url.hostname, parsed_url.path, f"?lang={self.lang}"]
        )
        # Extract recipe id from the url path
        recipe_uid = parsed_url.path.split("/")[-1]

        # Request the final recipe json from the kptncook api
        api_url = f"https://mobile.kptncook.com/recipes/search?kptnkey=6q7QNKy-oIgk-IMuWisJ-jfN7s6&lang={self.lang}"
        json_request_body = [{"uid": recipe_uid}]
        self.recipe_json = requests.post(
            api_url,
            headers=HEADERS,
            proxies=proxies,
            timeout=timeout,
            json=json_request_body,
        ).json()[0]

    @classmethod
    def host(cls, subdomain="mobile"):
        return f"{subdomain}.kptncook.com"

    def author(self):
        author = self.recipe_json["authors"][0]
        return f"{author['name']} ({author['link']})"

    def title(self):
        return self.recipe_json["title"]

    def category(self):
        return self.recipe_json["rtype"]

    def total_time(self):
        return self.recipe_json["cookingTime"] + self.recipe_json["preparationTime"]

    def cook_time(self):
        return self.recipe_json["cookingTime"]

    def prep_time(self):
        return self.recipe_json["preparationTime"]

    def yields(self):
        return 1

    def nutrients(self):
        return self.recipe_json["recipeNutrition"]

    def canonical_url(self):
        return self.final_url

    def image(self):
        return f"{self.recipe_json['imageList'][0]['url']}?kptnkey=6q7QNKy-oIgk-IMuWisJ-jfN7s6"

    def ingredients(self):
        return [
            " ".join(
                str(x)
                for x in
                # The filter is needed because "measure" and "quantity" fields are not always provided
                filter(
                    None,
                    (
                        [
                            ingredient.get("quantity"),
                            ingredient.get("measure"),
                            ingredient["ingredient"]["title"],
                        ]
                        if self.lang not in IMPERIAL_LANGUAGES
                        else [
                            ingredient.get("quantityUS"),
                            ingredient.get("measureUS"),
                            ingredient["ingredient"]["title"],
                        ]
                    ),
                )
            )
            for ingredient in self.recipe_json["ingredients"]
        ]

    def instructions(self):
        return "\n".join(step["title"] for step in self.recipe_json["steps"])

    def ratings(self):
        return None

    def cuisine(self):
        return None

    def description(self):
        return self.recipe_json["authorComment"]

    def language(self):
        return self.lang
