from ._abstract import AbstractScraper
from ._grouping_utils import IngredientGroup, group_ingredients

class FortyAprons(AbstractScraper):
    @classmethod
    
    def host(cls):
        return "40aprons.com"
    
    def author(self):
        return self.schema.author()

    def description(self):
        return self.schema.description()
    
    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()
    
    def instructions(self):
        return self.schema.instructions()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def category(self):
        return self.schema.category()

    def cook_time(self):
        return self.schema.cook_time()

    def cuisine(self):
        return self.schema.cuisine()

    def nutrients(self):
        return self.schema.nutrients()
    
    def prep_time(self):
        return self.schema.prep_time()
    
    def ratings(self):
        reviews_data = self.schema.data.get("review", [])
        if not reviews_data:
            return float(0)
        
        ratings = [
            float(review.get("reviewRating", {}).get("ratingValue"))
            for review in reviews_data
            if review.get("reviewRating", {}).get("ratingValue")
        ]

        return (sum(ratings) / len(ratings)) if ratings else float(0)

    def ratings_count(self):
        aggregate_rating = self.schema.data.get("aggregateRating", {})
        rating_count = aggregate_rating.get("ratingCount")

        return float(rating_count) if rating_count else float(0)

    def reviews(self):
        reviews_data = self.schema.data.get("review", [])
        reviews_list = []
        for review in reviews_data:
            review_body = review.get("reviewBody")
            reviewer_name = review.get("author", {}).get("name")
            if review_body and reviewer_name:
                reviews_list.append({
                    "name": reviewer_name,
                    "review": review_body
                })

        return reviews_list if reviews_list else None


    def equipment(self):
        equipment_elements = self.soup.select(".wprm-recipe-equipment-name")
        return [element.get_text() for element in equipment_elements] if equipment_elements else None

    # def cooking_method(self):
    #     return 

    def keywords(self):
        return self.schema.keywords()

    def ingredient_groups(self):
        groups = group_ingredients(
            self.ingredients(),
            self.soup,
            "h4.wprm-recipe-group-name",
            "li.wprm-recipe-ingredient",
        )
        return groups if groups else self.ingredients()

    # def dietary_restrictions(self):
    #     return 
    
   
