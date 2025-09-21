from ._abstract import AbstractScraper


class DeliciouslySprinkled(AbstractScraper):
    @classmethod
    def host(cls):
        return "deliciouslysprinkled.com"

    def equipment(self):
        return list(
            dict.fromkeys(
                equip.get_text(strip=True)
                for equip in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
                if equip.get_text(strip=True)
            )
        )
