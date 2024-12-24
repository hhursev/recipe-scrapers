from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, StaticValueException
from ._utils import get_minutes, get_yields, normalize_string


class WikiCookbook(AbstractScraper):
    @classmethod
    def host(cls):
        return "en.wikibooks.org"

    def site_name(self):
        raise StaticValueException(return_value="Wikibooks")

    def title(self):
        return (
            self.soup.find("h1", {"id": "firstHeading"})
            .get_text()
            .replace("Cookbook:", "")
        )

    def total_time(self):
        return get_minutes(self.soup.find("th", string="Time").find_next_sibling("td"))

    def yields(self):
        return get_yields(
            self.soup.find("th", string="Servings").find_next_sibling("td")
        )

    def image(self):
        image = self.soup.find("a", {"class": "mw-file-description"}).find(
            "img", {"src": True}
        )
        return image["src"] if image else None

    def ingredients(self):
        ingredients_section = self.soup.find("h2", {"id": "Ingredients"})
        if not ingredients_section:
            raise ElementNotFoundInHtml(element="//h2[@id='Ingredients']")
        ingredients = ingredients_section.find_next("ul").findAll("li")
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions_section = self.soup.find("h2", {"id": "Procedure"})
        if not instructions_section:
            raise ElementNotFoundInHtml(element="//h2[@id='Procedure']")
        instructions = instructions_section.find_next("ol").findAll("li")
        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    def description(self):
        paragraphs = list()
        for tag in self.soup.find(class_="mw-parser-output"):
            try:
                # get all paragraphs except for links
                if (
                    tag.text.strip()
                    and tag.name == "p"
                    and not tag.find("span", {"id": "displaytitle"})
                ):
                    paragraphs.append(tag)
                # End at the TOC or second section
                if tag.attrs.get("id") == "toc" or tag.name == "h2":
                    break
            except AttributeError:
                # Ignore tags that are not <p> but raise errors
                pass

        return "\n\n".join(
            [normalize_string(paragraph.get_text()) for paragraph in paragraphs]
        )
