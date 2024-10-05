from ._abstract import AbstractScraper
from ._utils import change_keys, get_max_res_src


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
        return get_max_res_src(image) if image else None

    def instructions(self):
        """
        Standard Schema.org implementation, except removes HowToSection with generic 'Oppskrift' header.
        These are "pseudo" sections that are not rendered on the actual website.
        """
        return "\n".join(
            [i for i in self.schema.instructions().split("\n") if i != "Oppskrift"]
        )
