import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, SchemaOrgException
from ._utils import normalize_string


class LekkerEnSimpel(AbstractScraper):
    @classmethod
    def host(cls):
        return "lekkerensimpel.com"

    def author(self):
        return self.soup.find("meta", {"name": "author"})["content"]

    def title(self):
        title = self.soup.find("h1", {"class": "hero__title"}).text
        return normalize_string(title)

    def image(self):
        image = self.soup.find("meta", {"property", "og:image"})
        return image["content"] if image else None

    def ingredients(self):
        if self.schema.ingredients():
            return self.schema.ingredients()

        ingredient_header = self.soup.find("strong", string="Benodigdheden:")
        if ingredient_header:
            ingredients = ingredient_header.parent.parent.find_next(
                name="ul"
            ).findChildren("li")
            return [normalize_string(i.get_text()) for i in ingredients]

        ingredient_header = self.soup.find("p", string="Benodigdheden:")
        if ingredient_header:
            ingredients = ingredient_header.parent.find_next(name="ul").findChildren(
                "li"
            )
            return [normalize_string(i.get_text()) for i in ingredients]

        raise ElementNotFoundInHtml("Could not find ingredients.")

    def process_ingredients(self, container):
        ingredients = container.findChildren("li")

        return [normalize_string(i.get_text()) for i in ingredients]

    def instructions(self):
        if self.schema.instructions():
            return self.schema.instructions()

        instructions_head = self.soup.find("strong", string="Bereidingswijze:")
        if instructions_head:
            p_tag = instructions_head.find_parent().find_next(name="p")
            if p_tag:
                lines = []
                for child in p_tag.children:
                    if getattr(child, "name", None) == "b":
                        break
                    text = (
                        child.get_text(strip=True)
                        if hasattr(child, "get_text")
                        else str(child).strip()
                    )
                    if text:
                        lines.append(text)
                return "\n".join(lines)

        instructions_head = self.soup.find(string=re.compile("Bereidingswijze"))
        if instructions_head and instructions_head.parent:
            grandparent = instructions_head.parent.parent
            if grandparent:
                return grandparent.get_text(separator="\n", strip=True)

        heading = self.soup.find("h2", class_="wp-block-heading")
        if heading:
            lines = []
            for tag in heading.find_all_next():
                if tag.name and tag.name.startswith("h"):
                    break
                if tag.name == "p":
                    if tag.find("strong"):
                        break
                    lines.append(tag.get_text(strip=True))
                elif tag.name == "strong":
                    break
                elif tag.name == "br" and tag.next_sibling:
                    sibling_text = tag.next_sibling.strip()
                    if sibling_text:
                        lines.append(sibling_text)
                elif tag.name is None and isinstance(tag, str):
                    text = tag.strip()
                    if text:
                        lines.append(text)
            if lines:
                return "\n".join(lines)

        raise ElementNotFoundInHtml("Could not find instructions.")

    def description(self):
        try:
            return self.schema.description()
        except SchemaOrgException:
            description = self.soup.find("meta", {"name": "description"})
            return description["content"] if description else None

    def language(self):
        return super().language()
