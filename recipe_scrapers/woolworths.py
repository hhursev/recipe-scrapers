# mypy: disallow_untyped_defs=False
import requests

from ._abstract import HEADERS, AbstractScraper
from ._schemaorg import SchemaOrg
from ._utils import url_path_to_dict


class Woolworths(AbstractScraper):
    def __init__(self, url, proxies=None, timeout=None, *args, **kwargs):
        super().__init__(url=url, *args, **kwargs)

        target = url_path_to_dict(url)["path"].split("/")[-1]
        data_url = f"https://foodhub.woolworths.com.au/content/woolworths-foodhub/en/{target}.model.json"

        self.page_data = (
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
        self.schema = SchemaOrg(self.page_data, raw=True)

    @classmethod
    def host(cls):
        return "woolworths.com.au"

    def canonical_url(self):
        return self.url

    def nutrients(self):
        return self.schema.nutrients()

    def language(self):
        return self.schema.language() or super().language()

    def site_name(self):
        return "Woolworths | Fresh Ideas For You"
