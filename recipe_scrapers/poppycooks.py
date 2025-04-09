from ._abstract import AbstractScraper
from ._utils import normalize_string, get_yields


class PoppyCooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "poppycooks.com"

    def title(self):
        return normalize_string(
            self.soup.find("h1", class_="fl-post-title").get_text()
        )

    def yields(self):
        return get_yields(
            self.soup.find("div", class_="kw-recipe-servings").get_text()
        )

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
        img_section = self.soup.find("div", class_="fl-post-thumb")
        img_tag = img_section.find("img")

        largest_image_url = ''
        if img_tag:
            srcset = img_tag.get("data-srcset", "")
            if srcset:
                images = []
                for item in srcset.split(","):
                    parts = item.strip().split(" ")
                    if len(parts) == 2:
                        url_candidate, width_str = parts
                        try:
                            width = int(width_str.rstrip("w"))
                        except ValueError:
                            width = 0
                        images.append((width, url_candidate))
                if images:
                    largest_image_url = max(images, key=lambda x: x[0])[1]
            else:
                largest_image_url = img_tag.get("src", "")
        return largest_image_url

