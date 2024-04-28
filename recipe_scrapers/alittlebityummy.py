# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import normalize_string


class ALittleBitYummy(AbstractScraper):
    @classmethod
    def host(cls):
        return "alittlebityummy.com"

    def author(self):
        author_tag = self.soup.find(
            "h4", string=lambda text: text and "Author:" in text
        )
        if author_tag:
            return author_tag.text.replace("Author:", "").strip()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredient_blocks = self.soup.select(".ingredients-tab-content div")
        seen = set()
        ingredients_list = []
        for ing in ingredient_blocks:
            bold_text = ing.find("b")
            span_text = ing.find("span")
            if bold_text and span_text:
                ingredient_text = f"{normalize_string(bold_text.get_text())} {normalize_string(span_text.get_text())}"
                if ingredient_text not in seen:
                    seen.add(ingredient_text)
                    ingredients_list.append(ingredient_text)
        return ingredients_list

    def instructions(self):
        instruction_steps = self.soup.select("#method ol li")
        return "\n".join(
            normalize_string(step.get_text())
            for step in instruction_steps
            if step.get_text()
        )

    def description(self):
        return self.schema.description()
