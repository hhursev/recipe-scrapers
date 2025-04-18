from ._abstract import AbstractScraper


class SkinnyTaste(AbstractScraper):
    @classmethod
    def host(cls):
        return "skinnytaste.com"

    def equipment(self):
        equipment_container = self.soup.find(
            "div", class_="wprm-recipe-equipment-container"
        )
        if equipment_container:
            return [
                item.get_text(strip=True)
                for item in equipment_container.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
            ]
        return None
