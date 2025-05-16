from ._abstract import AbstractScraper
from ._utils import normalize_string, get_yields


class PoppyCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "poppycooks.com"

    def author(self):
        author_meta = self.soup.find("div", itemprop="author")
        name_meta = author_meta.find("meta", itemprop="name")
        return normalize_string(name_meta["content"])

    def title(self):
        return normalize_string(self.soup.find("h1", class_="fl-post-title").get_text())

    def yields(self):
        return get_yields(self.soup.find("div", class_="kw-recipe-servings").get_text())

    def ingredients(self):
        ingredients_list = []
        ingredients_section = self.soup.find("ul", class_="ingredients-list")
        if ingredients_section:
            ingredients = ingredients_section.find_all("li", class_="metric")
            ingredients_list = [
                normalize_string(ingredient.get_text()) for ingredient in ingredients
            ]
        return ingredients_list

    def instructions(self):
        instructions_list = []
        method_section = self.soup.find("ol", class_="method")
        if method_section:
            steps = method_section.find_all("li")
            for step in steps:
                instruction_text = normalize_string(step.get_text())
                if instruction_text:
                    instructions_list.append(instruction_text)
        return "\n".join(instructions_list)

    def image(self):
        img_tag = self.soup.find("div", class_="fl-post-thumb").find("img")
        if not img_tag:
            return ""

        srcset = img_tag.get("data-srcset", "")
        if not srcset:
            return img_tag.get("src", "")

        images = [
            (int(width_str.rstrip("w")), url_candidate)
            for item in srcset.split(",")
            if (parts := item.strip().split(" ")) and len(parts) == 2
            for url_candidate, width_str in [parts]
            if width_str.rstrip("w").isdigit()
        ]

        return max(images, key=lambda x: x[0])[1] if images else ""
