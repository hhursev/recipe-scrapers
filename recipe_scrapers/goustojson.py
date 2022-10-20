# mypy: disallow_untyped_defs=False
import requests

from ._abstract import HEADERS, AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string, url_path_to_dict


class GoustoJson(AbstractScraper):
    """
    Ad-hoc solution to https://github.com/hhursev/recipe-scrapers/issues/376
    Let's see if it stands the test of time and reevaluate.
    """

    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        recipe_slug = url_path_to_dict(url).get("path").split("/")[-1]
        data_url = (
            f"https://production-api.gousto.co.uk/cmsreadbroker/v1/recipe/{recipe_slug}"
        )

        recipe_json = requests.get(
            data_url,
            headers=HEADERS,
            proxies=proxies,
            timeout=timeout,
        ).json()

        self.page_data = recipe_json.get("data")
        self.data = self.page_data.get("entry")

    @classmethod
    def host(cls):
        return "gousto.co.uk"

    def title(self):
        return self.data.get("title")

    def total_time(self):
        return get_minutes(sorted(self.data.get("prep_times").values())[-1])

    def yields(self):
        return get_yields(sorted(self.data.get("prep_times").keys())[-1])

    def image(self):
        return self.data.get("seo").get("open_graph_image")

    def ingredients(self):
        return [
            normalize_string(ingredient.get("label"))
            for ingredient in self.data.get("ingredients")
            if isinstance(ingredient, dict) and "label" in ingredient.keys()
        ]

    def instructions(self):
        return "\n".join(
            [
                normalize_string(instruction.get("instruction"))
                for instruction in self.data.get("cooking_instructions")
                if isinstance(instruction, dict) and "instruction" in instruction.keys()
            ]
        )

    def ratings(self):
        return self.data.get("rating").get("average")
