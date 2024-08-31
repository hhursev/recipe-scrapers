import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class MarleySpoon(AbstractScraper):
    @classmethod
    def host(cls, domain="de"):
        return f"marleyspoon.{domain}"

    def canonical_url(self):
        return self.soup.find("meta", {"property": "og:url"})["content"]

    def author(self):
        return normalize_string(self.soup.find(class_="author-info").a.get_text())

    def title(self):
        return normalize_string(
            self.soup.find("h3", {"class": "recipe-title"}).get_text()
        )

    def _specs(self):
        return self.soup.find("ul", {"class": "recipe-specs"}).find_all("li")

    def total_time(self):
        time = self._specs()[0].find_next("span").get_text()
        return get_minutes(re.sub(r" \S$| ", "", time))

    def category(self):
        return normalize_string(self._specs()[1].find_next("span").get_text())

    def nutrients(self):
        nutrients = self._specs()[2].find_next("p").get_text()
        nutrients = nutrients.split(",")
        nutrients = [nutrient.split()[1] for nutrient in nutrients]
        nutrients = {
            "calories": nutrients[0] + " calories",
            "fatContent": nutrients[1] + " grams fat",
            "proteinContent": nutrients[2] + " grams protein",
            "carbohydrateContent": nutrients[3] + " grams carbohydrates",
        }
        return nutrients

    def image(self):
        return self.schema.image()

    def ingredients(self):
        send = self.soup.find("div", {"class": "dish-detail__we-send"}).find_all("div")
        additional = self.soup.find(
            "div", {"class": "dish-detail__sidebar-section"}
        ).div.find_all("li")
        return [normalize_string(i.get_text()) for i in send + additional]

    def instructions(self):
        steps = self.soup.find("div", {"class": "dish-steps__container"}).find_all(
            "p", {"class": "dish-step__body-text"}
        )
        steps = [normalize_string(step.get_text()) for step in steps]
        return "\n".join(steps)

    def equipment(self):
        equipment = self.soup.find_all(
            "div", {"class": "dish-detail__sidebar-section"}
        )[1].find_all("li")
        return [normalize_string(e.get_text()) for e in equipment]

    def keywords(self):
        keywords = self.soup.find(class_="recipe-labels").find_all(
            class_="recipe-attributes__label"
        )
        return [normalize_string(keyword.get_text()) for keyword in keywords]

    def description(self):
        description = self.soup.find("div", {"class": "whats-cooking"}).p.get_text()
        return normalize_string(description)
