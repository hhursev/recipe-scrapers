from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml


class VeganSociety(AbstractScraper):
    @classmethod
    def host(cls):
        return "vegansociety.com"

    def _find_content_heading(self, expected_title):
        for heading in self.soup.find_all("h2"):
            if expected_title in heading.text:
                return heading

        for heading in self.soup.find_all("h3"):
            if expected_title in heading.text:
                return heading

    def _find_content_list(self, expected_title, ordered):
        content_heading = self._find_content_heading(expected_title)
        if not content_heading:
            return None
        return content_heading.find_next_sibling("ol" if ordered else "ul")

    def author(self):
        instructions_list = self._find_content_list("Method", ordered=True)
        if instructions_list:
            authors = []
            for paragraph in instructions_list.find_next_siblings("p"):
                emphasis = paragraph.find("em")
                if emphasis and " by " in emphasis.text:
                    authors.append(emphasis.text.strip())
            if authors:
                return "; ".join(authors)

        # Fallback: credit the Vegan Society
        return self.site_name()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredient_elements = self._find_content_list("Ingredients", ordered=False)
        if not ingredient_elements:
            raise ElementNotFoundInHtml("Could not find ingredients.")

        ingredients = []
        for li in ingredient_elements.find_all("li"):
            ingredients.append(li.text.strip())
        return ingredients

    def instructions(self):
        instruction_elements = self._find_content_list("Method", ordered=True)
        if not instruction_elements:
            raise ElementNotFoundInHtml("Could not find instructions.")

        instructions = []
        for li in instruction_elements.find_all("li"):
            instructions.append(li.text.strip())
        return "\n".join(instructions)

    def description(self):
        return self.schema.description()
