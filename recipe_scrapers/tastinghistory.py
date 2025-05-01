from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class TastingHistory(AbstractScraper):
    @classmethod
    def host(cls):
        return "tastinghistory.com"

    def site_name(self):
        return "Tasting History"

    def author(self):
        return "Max Miller"

    def title(self):
        return self.soup.find("h1").get_text()

    def category(self):
        tags = self.soup.find_all("a", {"class": "blog-item-tag"})
        if tags:
            return ", ".join([tag.text.strip() for tag in tags])
        return None

    def total_time(self):
        return None

    def yields(self):
        return None

    def image(self):
        img_elem = self.soup.find("img", {"data-image": True})
        return img_elem.get("data-image") if img_elem else None

    def ingredients(self):
        ingredients = []
        ingredients_lists = self.soup.select(
            "div.sqs-col-4.span-4 .sqs-block-content ul"
        )
        if ingredients_lists:
            for ingredients_list in ingredients_lists:
                for li in ingredients_list.find_all("li"):
                    ingredients.append(li.text.strip())
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.sqs-col-4.span-4 .sqs-block-markdown .sqs-block-content p",
            "div.sqs-col-4.span-4 .sqs-block-content li",
        )

    def instructions(self):
        instructions = []
        instructions_list = self.soup.select_one(
            "div.sqs-col-8.span-8 .sqs-block-content ol"
        )
        if instructions_list:
            for li in instructions_list.find_all("li"):
                instructions.append(li.text.strip())
        return "\n".join(instructions)

    def description(self):
        desc_elem = self.soup.find("meta", {"property": "og:description"})
        return desc_elem.get("content") if desc_elem else None
