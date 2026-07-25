from ._abstract import AbstractScraper


class CookingCircle(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookingcircle.com"

    def author(self):
        return (
            self.soup.find("div", {"class": "recipe-author"})
            .find("span", {"class": "text-uppercase"})
            .get_text()
        )

    def ingredients(self):
        ul_list = (
            self.soup.find(
                "div", {"class": "single-ingredients__group", "data-unit": "metric"}
            )
            .find("ul", {"class": "single-ingredients__list"})
            .find_all("li")
        )

        ingredients = []
        for li in ul_list:
            ingredients.append(
                li.get_text().replace("\t", "").replace("\n\n", " ").replace("\n", "")
            )
        return ingredients

    def instructions(self):
        ul_list = self.soup.find("ul", {"class": "single-method__method"}).find_all(
            "li"
        )

        instructions = []
        for li in ul_list:
            instructions.append(li.get_text().strip().replace("\n", " "))

        return "\n".join(instructions)
