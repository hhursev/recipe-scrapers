from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TasteAU(AbstractScraper):
    @classmethod
    def host(cls):
        return "taste.com.au"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "li.section-heading h3",
            "div.ingredient-description",
        )

    def instructions(self):
        steps = self.soup.select(
            "ul.recipe-method-steps li .recipe-method-step-content"
        )
        return "\n".join(step.get_text(strip=True) for step in steps)
