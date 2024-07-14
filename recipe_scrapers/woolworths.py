import requests

from ._abstract import HEADERS, AbstractScraper
from ._utils import url_path_to_dict


class Woolworths(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        target = url_path_to_dict(url)["path"].split("/")[-1]
        data_url = f"https://foodhub.woolworths.com.au/content/woolworths-foodhub/en/{target}.model.json"

        self.schema.data = (
            requests.get(
                data_url,
                headers=HEADERS,
                proxies=proxies,
                timeout=timeout,
            )
            .json()
            .get(":items")
            .get("root")
            .get(":items")
            .get("recipe_seo_data")
        )

    @classmethod
    def host(cls):
        return "woolworths.com.au"

    def canonical_url(self):
        return self.url

    def nutrients(self):
        return self.schema.nutrients()

    def language(self):
        return super().language()

    def site_name(self):
        return "Woolworths | Fresh Ideas For You"
