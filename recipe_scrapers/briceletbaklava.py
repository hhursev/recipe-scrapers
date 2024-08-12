from ._abstract import AbstractScraper
from ._utils import normalize_string


class BricelEtBaklava(AbstractScraper):
    @classmethod
    def host(cls):
        return "briceletbaklava.ch"

    def title(self):
        return self.soup.find("h1", {"class": "Post-title"}).get_text().strip()

    def category(self):
        return "\n".join(
            [
                normalize_string(category.get_text())
                for category in self.soup.find_all("a", {"class": "Post-tag"})
            ]
        )

    def yields(self):
        post = self.soup.find("div", {"class": "Post-body"})
        section = post.find_all("div", {"class": "ob-section ob-section-html"})
        return normalize_string(section[1].find("p").get_text())

    def image(self):
        return self.soup.find("a", {"class": "ob-link-img"})["href"]

    def instructions(self):
        post = self.soup.find("div", {"class": "Post-body"})
        return "\n".join(
            [
                normalize_string(instruction.get_text())
                for instruction in post.find_all("ul")
            ]
        )

    def ingredients(self):
        post = self.soup.find("div", {"class": "Post-body"})
        sections = post.find_all("div", {"class": "ob-section ob-section-html"})
        return [
            normalize_string(ingredient.get_text())
            for ingredient in sections[1].find_all("b")
        ]

    def description(self):
        return normalize_string(
            self.soup.find("div", {"class": "ob-section ob-section-html"}).get_text()
        )

    def author(self):
        return "Michel/Bricelet & Baklava"
