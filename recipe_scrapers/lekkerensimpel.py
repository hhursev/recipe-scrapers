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

    def ingredients(self):
        schema_ingredients = self.schema.ingredients()
        if schema_ingredients:
            return schema_ingredients

        ingredient_header = self.soup.find("strong", string="Benodigdheden:")
        if ingredient_header:
            ul = ingredient_header.parent.parent.find_next(name="ul")
            if ul:
                return [normalize_string(li.get_text()) for li in ul.find_all("li")]

        ingredient_header = self.soup.find("p", string="Benodigdheden:")
        if ingredient_header:
            ul = ingredient_header.parent.find_next(name="ul")
            if ul:
                return [normalize_string(li.get_text()) for li in ul.find_all("li")]

        necessities_div = self.soup.find("div", class_="recipe__necessities")
        if necessities_div:
            ul = necessities_div.find("ul")
            if ul:
                ingredients = []
                for li in ul.find_all("li", recursive=False):
                    parts = []
                    value = li.find("span", class_="value")
                    measure = li.find("span", class_="measure")
                    ingredient = li.find("span", class_="ingredient")
                    description = li.find("span", class_="description")

                    if value and value.get_text(strip=True):
                        parts.append(value.get_text(strip=True))
                    if measure and measure.get_text(strip=True):
                        parts.append(measure.get_text(strip=True))
                    if ingredient and ingredient.get_text(strip=True):
                        parts.append(ingredient.get_text(strip=True))
                    if description and description.get_text(strip=True):
                        parts.append(f"({description.get_text(strip=True)})")

                    # If no structured spans, fallback to li text
                    if not parts:
                        text = li.get_text(strip=True)
                        if text:
                            parts.append(text)

                    if parts:
                        ingredients.append(normalize_string(" ".join(parts)))
                if ingredients:
                    return ingredients

        raise ElementNotFoundInHtml("Could not find ingredients.")

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
