from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class Epicurious(AbstractScraper):
    @classmethod
    def host(cls):
        return "epicurious.com"

    def title(self):
        return normalize_string(self.soup.find("h1", {"itemprop": "name"}).get_text())

    def total_time(self):
        total_time = self.soup.find("dd", {"class": "total-time"})

        return get_minutes(total_time)

    def yields(self):
        return get_yields(self.soup.find("dd", {"itemprop": "recipeYield"}))

    def image(self):
        image = self.soup.find("img", {"class": "photo", "srcset": True})
        return image["srcset"] if image else None

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"itemprop": "ingredients"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("li", {"class": "preparation-step"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def ratings(self):
        rating = self.soup.find("span", {"class": "rating"})
        rating = rating.get_text().split("/")[0] if rating is not None else None
        rating = float(rating) if rating is not None else None
        return rating

    def reviews(self):
        result = []
        reviews = self.soup.find("div", {"class": "reviews"})
        if len(reviews.find_all("li")):
            for li in reviews.find_all("li"):
                rating = li.find("img", {"class": "fork-rating"})
                try:
                    rating_value = int(rating.get("src").split("_forks.png")[0][-1])
                except Exception:
                    rating_value = 0

                result.append(
                    {
                        "review_text": normalize_string(li.find("p").get_text()),
                        "rating": rating_value,
                    }
                )

        return result
