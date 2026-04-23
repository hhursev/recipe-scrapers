from ._abstract import AbstractScraper
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
        og_title = self.soup.find("meta", {"property": "og:title"})
        if og_title:
            return normalize_string(og_title.get("content"))
        heading = self.soup.find("h1", class_="section__title-text")
        if heading:
            return normalize_string(heading.get_text())
        return None

    def image(self):
        og_image = self.soup.find("meta", {"property": "og:image:secure_url"})
        if og_image:
            return og_image.get("content")
        og_image = self.soup.find("meta", {"property": "og:image"})
        if og_image:
            return og_image.get("content")
        return None

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
