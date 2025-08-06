from ._abstract import AbstractScraper


class CookingCircle(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookingcircle.com"

    def author(self):
        return (
            self.soup.find("div", {"class": "recipe-author"})
            .findChild("span", {"class": "text-uppercase"})
            .get_text()
        )

    def ingredients(self):
        ul_list = (
            self.soup.find(
                "div", {"class": "single-ingredients__group", "data-unit": "metric"}
            )
            .findChild("ul", {"class": "single-ingredients__list"})
            .findChildren("li")
        )

        ingredients = []
        for li in ul_list:
            ingredients.append(
                li.get_text().replace("\t", "").replace("\n\n", " ").replace("\n", "")
            )
        return ingredients

    def instructions(self):
        ul_list = self.soup.find("ul", {"class": "single-method__method"}).findChildren(
            "li"
        )

        instructions = []
        for li in ul_list:
            instructions.append(li.get_text().strip().replace("\n", " "))

        return "\n".join(instructions)
