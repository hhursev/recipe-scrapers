from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class Instructables(AbstractScraper):
    @classmethod
    def host(cls):
        return "instructables.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".step-body p strong",
            ".step-body li",
        )

    def title(self):
        title_tag = self.soup.find("h2", class_="step-title sr-only")
        return normalize_string(title_tag.get_text())

    def author(self):
        author_tag = self.soup.find("span", class_="author-name")
        return normalize_string(author_tag.get_text().replace("By ", ""))

    def ingredients(self):
        ingredients_section = self.soup.find("section", id="stepsupplies")
        if not ingredients_section:
            return []

        ingredients_tags = ingredients_section.find_all("li", class_="ql-indent-1")
        return [normalize_string(tag.get_text()) for tag in ingredients_tags]

    def instructions(self):
        steps = self.soup.find_all("section", class_="step")
        instructions = []
        for step in steps:
            step_title = step.find("h2", class_="step-title")
            step_body = step.find("div", class_="step-body")
            if step_title and step_body:
                instructions.append(
                    f"{normalize_string(step_title.get_text())}: {normalize_string(step_body.get_text())}"
                )
        return "\n".join(instructions)

    def image(self):
        image_tag = self.soup.find("img", class_="photoset-image")
        return image_tag["src"] if image_tag else None
