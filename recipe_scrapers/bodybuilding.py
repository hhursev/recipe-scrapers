from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class Bodybuilding(AbstractScraper):
    @classmethod
    def host(cls):
        return "bodybuilding.com"

    def author(self):
        return self.soup.find("span", {"class": "bb-recipe-author-name"}).get_text()

    def title(self):
        return self.soup.find("h1", {"class": "bb-recipe-headline-title"}).get_text()

    def category(self):
        tagList = self.soup.find(
            "div", {"class": "bb-recipe__desktop-tags"}
        ).findChildren("div", {"class": "bb-recipe__topic"})

        categories = []
        for tag in tagList:
            categories.append(tag.get_text())
        return ",".join(categories)

    def total_time(self):
        return get_minutes(
            self.soup.find("div", {"class": "bb-recipe__meta-time"})
            .find("div", {"class": "bb-recipe__meta-value-text"})
            .get_text()
        )

    def yields(self):
        return get_yields(
            self.soup.find("div", {"class": "bb-recipe__meta-servings"})
            .find("div", {"class": "bb-recipe__meta-value-text"})
            .get_text()
        )

    def image(self):
        container = self.soup.find("div", {"class": "bb-recipe-header-image"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None

    def ingredients(self):
        ulList = self.soup.find(
            "ul", {"class": "bb-recipe__ingredient-list"}
        ).findChildren("li")

        ingredients = []
        for li in ulList:
            ingredients.append(" ".join(li.get_text().split()))
        return ingredients

    def instructions(self):
        olList = self.soup.find(
            "ol", {"class": "bb-recipe__directions-list"}
        ).findChildren("li")

        count = 0
        instructions = []

        for li in olList:
            count += 1
            instructions.append(str(count) + ". " + " ".join(li.get_text().split()))

        return "\n".join(instructions)

    def description(self):
        return (
            self.soup.find("p", {"class": "BBCMS__content--article-description"})
            .get_text()
            .strip()
        )
