from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class AllRecipes:
    @classmethod
    def host(cls):
        return "allrecipes.com"

    def __new__(cls, url, *args, **kwargs):
        if AllRecipesUser.host() in url:
            return AllRecipesUser(url, *args, **kwargs)
        return AllRecipesCurated(url, *args, **kwargs)


class AllRecipesCurated(AbstractScraper):
    @classmethod
    def host(cls):
        return "allrecipes.com"

    def ingredients(self):
        def get_ingredient_text(item, key):
            span = item.find("span", {"data-ingredient-" + key: True})
            return normalize_string(span.text) if span else ""

        def match_ingredient_class(tag):
            return tag.has_attr("class") and any(
                cls.endswith("structured-ingredients__list-item")
                for cls in tag["class"]
            )

        ingredients_list = []
        keys = ["quantity", "unit", "name"]
        for item in self.soup.find_all(match_ingredient_class):
            ingredient_parts = [get_ingredient_text(item, key) for key in keys]
            ingredients_list.append(" ".join(filter(None, ingredient_parts)))

        return ingredients_list


class AllRecipesUser(AbstractScraper):
    """Parse "unpublished" personal recipes on AllRecipes.com.

    Unpublised recipes are not structured, unlike curated recipes.
    Certain information is not always available, as it relies on what the
    users provided.
    """

    @classmethod
    def host(cls):
        return "allrecipes.com/cook"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # meta contains servings and yields, as well as preparation, cooking,
        # and total times
        # Possible keys are 'servings', 'yield', 'cook', 'prep', 'total'
        meta = zip(
            self.soup.findAll("div", {"class": "recipe-meta-item-header"}),
            self.soup.findAll("div", {"class": "recipe-meta-item-body"}),
        )
        self.meta = {
            k.text.lower().rstrip(":"): normalize_string(v.text) for k, v in meta
        }

    def title(self):
        title = self.soup.find("h1", {"class": "heading-content"}).text
        return title

    def total_time(self):
        if "total" in self.meta:
            return get_minutes(self.meta.get("total") or 0)
        else:
            return self.prep_time() + self.cook_time()

    def prep_time(self):
        return get_minutes(self.meta.get("prep") or 0)

    def cook_time(self):
        return get_minutes(self.meta.get("cook") or 0)

    def yields(self):
        yield_data = self.meta.get("yield")
        if yield_data is None:
            yield_data = self.meta.get("servings")
        return get_yields(yield_data)

    def image(self):
        image = self.soup.find("div", {"class": "lead-media", "data-src": True})
        image = image.get("data-src")
        return image

    def nutrients(self):
        raise NotImplementedError("Not available for personal recipes.")

    def ingredients(self):
        ingredients = self.soup.findAll("span", {"class": "ingredients-item-name"})
        ingredients = [normalize_string(i.text) for i in ingredients]
        return ingredients

    def instructions(self):
        instructions = self.soup.findAll("div", {"class": "paragraph"})
        instructions = "\n".join(normalize_string(i.text) for i in instructions)
        return instructions

    def ratings(self):
        lacks_rating = self.soup.find("a", {"class": "no-ratings"})
        if lacks_rating:
            return None

        ratings = self.soup.find("span", {"class": "review-star-text"})
        return float(ratings.text.lstrip("Ratings:").rstrip("stars"))

    def author(self):
        author = self.soup.find("span", {"class": "author-name"}).text
        return author

    def reviews(self):
        """Return a list of dictionaries containing reviews.

        Each dictionary contains the author, datePublished, reviewRating, reviewBody.
        These keys follow the JSON-LD format.
        """
        reviews = []
        for element in zip(
            self.soup.findAll("span", {"class": "reviewer__name"}),  # name
            self.soup.findAll("span", {"class": "feedback__reviewDate"}),  # date
            self.soup.findAll("span", {"class": "review-star-text"}),  # rating
            self.soup.findAll("div", {"class": "feedback__reviewBody"}),  # comment
        ):
            name, date, rating, comment = element
            name = normalize_string(name.text)
            date = date.text
            # The value is "Ratings: 4 stars"
            rating = float(rating.text.lstrip("Ratings:").rstrip("stars"))
            comment = normalize_string(comment.text)

            reviews.append(
                {
                    "author": name,
                    "datePublished": date,
                    "reviewRating": rating,
                    "reviewBody": comment,
                }
            )
        return reviews

    def cuisine(self):
        return None

    def category(self):
        return None
