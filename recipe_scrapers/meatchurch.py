from ._abstract import AbstractScraper
from ._exceptions import FieldNotProvidedByWebsiteException
from ._utils import normalize_string


class MeatChurch(AbstractScraper):
    @classmethod
    def host(cls):
        return "meatchurch.com"

    def site_name(self):
        return "Meat Church"

    def author(self):
        return "Meat Church"

    def title(self):
        return self.soup.find("meta", property="og:title")["content"]

    def ingredients(self):
        article = self.soup.find("div", class_="article__content")
        if not article:
            return []
        ingredients = []
        for ul in article.find_all("ul"):
            for li in ul.find_all("li"):
                text = normalize_string(li.get_text())
                if text:
                    ingredients.append(text)
        return ingredients

    def instructions(self):
        article = self.soup.find("div", class_="article__content")
        if not article:
            return ""

        lists = article.find_all("ul")
        if not lists:
            return ""

        last_list = lists[-1]
        steps = []
        for sibling in last_list.next_siblings:
            if sibling.name == "p":
                text = normalize_string(sibling.get_text())
                if text:
                    steps.append(text)
        return "\n".join(steps)

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)

    def yields(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)
