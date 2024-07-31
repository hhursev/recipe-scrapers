import requests
from bs4 import BeautifulSoup

from ._abstract import HEADERS, AbstractScraper
from ._utils import get_minutes, get_url_slug, get_yields, normalize_string


class GoustoJson(AbstractScraper):
    """
    Ad-hoc solution to https://github.com/hhursev/recipe-scrapers/issues/376
    Let's see if it stands the test of time and reevaluate.
    """

    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        recipe_slug = get_url_slug(url)
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

    def description(self):
        return normalize_string(self.data.get("description"))

    def total_time(self):
        return get_minutes(sorted(self.data.get("prep_times").values())[0])

    def yields(self):
        return get_yields(sorted(self.data.get("prep_times").keys())[0])

    def image(self):
        return self.data.get("seo").get("open_graph_image")

    def ingredients(self):
        return [
            normalize_string(ingredient.get("label"))
            for ingredient in self.data.get("ingredients")
            if isinstance(ingredient, dict)
            and ingredient.get("label", None) is not None
        ]

    def instructions_list(self):
        instructions = []
        for instruction in self.data.get("cooking_instructions"):
            if isinstance(instruction, dict) and "instruction" in instruction.keys():
                single_step = instruction.get("instruction")
                soup = BeautifulSoup(single_step, "html.parser")
                instruction_paragraphs = soup.findAll("p")
                if instruction_paragraphs:
                    instructions.append(
                        "\n".join(
                            [
                                normalize_string(paragraph.get_text())
                                for paragraph in instruction_paragraphs
                            ]
                        )
                    )

        return instructions

    def instructions(self):
        return "\n".join(self.instructions_list())

    def ratings(self):
        return self.data.get("rating").get("average")
