import re

from ._abstract import AbstractScraper
from ._utils import change_keys


def fix_json_ld_property_keys(k):
    if k == "ItemListElement":
        return "itemListElement"
    return k


class TineNo(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fix incorrect property naming
        self.schema.data = change_keys(self.schema.data, fix_json_ld_property_keys)

    @classmethod
    def host(cls):
        return "tine.no"

    def image(self):
        image = self.soup.find("img", {"id": "HeaderMediaContent"})
        if not image:
            # No image available
            return None
        # Prefer data src set for higher image resolution
        srcset_str = image.get("data-srcset", None)
        if not srcset_str:
            # Fallback to regular img source
            return image.get("src", None)
        # Convert source set string to cleaner list
        srcset = srcset_str.split(",")
        # Find image with the best resolution
        max_res = None
        max_res_src = None
        res_pattern = re.compile(r"(\d+)w")
        for src_str in srcset:
            src = src_str.strip().split(" ")
            res_match = res_pattern.findall(src[1])
            res = None
            if res_match:
                try:
                    res = int(res_match[0])
                except ValueError:
                    pass
            if max_res is None or res > max_res:
                max_res = res
                max_res_src = src[0]
        return max_res_src

    def instructions(self):
        """
        Standard Schema.org implementation, except removes HowToSection with generic 'Oppskrift' header.
        These are "pseudo" sections that are not rendered on the actual website.
        """
        return "\n".join(
            [i for i in self.schema.instructions().split("\n") if i != "Oppskrift"]
        )
