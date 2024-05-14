# mypy: allow-untyped-defs
import requests

from ._abstract import HEADERS, AbstractScraper
from ._utils import url_path_to_dict


class Bergamot(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, proxies=proxies, timeout=timeout, *args, **kwargs)

        url_dict = url_path_to_dict(url)
        path = url_dict.get("path")
        recipe_id = path.split("/")[-1]

        data_url = f"https://api.bergamot.app/recipes/shared?r={recipe_id}"
        response = requests.get(
            data_url, headers=HEADERS, proxies=proxies, timeout=timeout
        )
        self.data = response.json()

    @classmethod
    def host(cls):
        return "dashboard.bergamot.app"

    def canonical_url(self):
        return self.data.get("sourceUrl") or self.url

    def author(self):
        return self.data.get("sourceDomain")

    def title(self):
        return self.data.get("title")

    def category(self):
        return None

    def total_time(self):
        return self._get_time_value("totalTime")

    def yields(self):
        servings = self.data.get("servings")
        return f"{servings} servings"

    def image(self):
        photos = self.data.get("photos")
        if not photos:
            return

        photo = photos[0]
        return photo.get("sourceUrl")

    def ingredients(self):
        return self._map_list("ingredients")

    def instructions(self):
        instructions_list = self._map_list("instructions")
        return "\n".join(instructions_list)

    def ratings(self):
        return None

    def cuisine(self):
        return None

    def description(self):
        return self.data.get("description")

    def prep_time(self):
        return self._get_time_value("prepTime")

    def cook_time(self):
        return self._get_time_value("cookTime")

    def _map_list(self, data_key):
        output = []
        for entry in self.data.get(data_key):
            output.extend(entry.get("data"))
        return output

    def _get_time_value(self, time_key):
        time_values = self.data.get("time")
        if not time_values:
            return None

        return time_values.get(time_key)
