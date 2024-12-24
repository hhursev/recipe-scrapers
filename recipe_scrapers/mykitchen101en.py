from ._abstract import AbstractScraper


class MyKitchen101en(AbstractScraper):
    @classmethod
    def host(cls):
        return "mykitchen101en.com"

    def equipment(self):
        return list(
            {
                ("".join(item.stripped_strings).split("(")[0].strip())
                for item in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
            }
        )
