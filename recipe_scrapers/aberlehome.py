from ._abstract import AbstractScraper
from ._utils import normalize_string
from ._exceptions import RecipeSchemaNotFound

NUTRIENT_MAP = {
    "calories"              : ".mv-create-nutrition-calories",
    "fatContent"            : ".mv-create-nutrition-total-fat",
    "saturatedFatContent"   : ".mv-create-nutrition-saturated-fat",
    "unsaturatedFatContent" : ".mv-create-nutrition-unsaturated-fat",
    "transFatContent"       : ".mv-create-nutrition-trans-fat",
    "carbohydrateContent"   : ".mv-create-nutrition-carbohydrates",
    "sugarContent"          : ".mv-create-nutrition-sugar",
    "proteinContent"        : ".mv-create-nutrition-protein",
    "sodiumContent"         : ".mv-create-nutrition-sodium",
    "fiberContent"          : ".mv-create-nutrition-fiber",
    "cholesterolContent"    : ".mv-create-nutrition-cholesterol",
}

class AberleHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "aberlehome.com"

    def ingredients(self):
        ingredients = self.schema.ingredients()
        if ingredients == []:
            ingredients = self.soup.select(".mv-create-ingredients li")
            ingredients = [normalize_string(ingredient.get_text()) for
                           ingredient in ingredients]
            if ingredients == []:
                raise Exception
        return ingredients

    def title(self):
        try:
            title = self.schema.title()
        except TypeError as e:
            title = self.soup.select('.entry-title')[0].get_text()
            if title is None:
                raise Exception
        return title

    def author(self):
        author = None
        def find_author_in_meta(self):
            author = None
            author_meta = self.soup.find("meta", attrs={"name": "author"})
            if author_meta:
                author = author_meta.get("content")
            return author
        try:
            author = self.schema.author()
            if author is None:
                author = find_author_in_meta(self)
        except TypeError as e:
            author = find_author_in_meta(self)
            if author is None:
                raise Exception
        return author


    def category(self):
        category = self.schema.category()
        if category is None:
            category = self.soup.find_all(class_="mv-create-category")[0].get_text()
            category = category.removeprefix("Category: ")
        return category

    def total_time(self):
        try:
            time = self.soup.total_time()
        except TypeError:
            time = self.soup.select('.mv-create-time-total .mv-time-part')[0].get_text()
        return time

    def cook_time(self):
        try:
            time = self.soup.cook_time()
        except TypeError:
            time = self.soup.select('.mv-create-time-active .mv-time-part')[0].get_text()
        return time

    def prep_time(self):
        try:
            time = self.soup.prep_time()
        except TypeError:
            time = self.soup.select('.mv-create-time-prep .mv-time-part')[0].get_text()
        return time

    def description(self):
        try:
            description = self.soup.description()
        except TypeError:
            description = self.soup.select('.mv-create-description p')[0].get_text()
        return description

    def instructions(self):
        instructions = self.schema.instructions()
        if instructions == [] or instructions == '':
            instructions = self.soup.select(".mv-create-instructions li")
            instructions = [normalize_string(ingredient.get_text()) for
                           ingredient in instructions]
            if instructions == [] or instructions == '':
                raise Exception
        return instructions

    def ratings(self):
        try:
            ratings = self.schema.ratings()
        except Exception as e:
            ratings = self.soup.select_one(".mv-create-reviews").get("data-mv-create-rating")
        return ratings

    def ratings_count(self):
        try:
            ratings_count = self.schema.ratings_count()
        except Exception as e:
            ratings_count = self.soup.select_one(".mv-create-reviews").get("data-mv-create-total-ratings")
        return ratings_count

    def yields(self):
        try:
            yields = self.schema.yields()
        except Exception as e:
            yields = self.soup.select_one(".mv-create-time-yield .mv-create-time-format").get_text()
        return yields

    def nutrients(self):
        nutrients = self.schema.nutrients()
        if nutrients == {}:
            for k,v in NUTRIENT_MAP.items():
                item = self.soup.select_one(v)
                label_tag = item.find(class_="mv-create-nutrition-label")
                label_tag.decompose()
                value = item.get_text(strip=True)
                nutrients[k] = value
        return nutrients

