from ._abstract import AbstractScraper
from ._exceptions import SchemaOrgException
from ._utils import normalize_string


class Lecker(AbstractScraper):
    @classmethod
    def host(cls):
        return "lecker.de"

    def title(self):
        try:
            return self.schema.title()
        except TypeError:
            return (
                self.soup.find(
                    "header", {"class": "article-header article-header--article"}
                )
                .find("h1")
                .get_text()
            )

    def instructions(self):
        if self.schema.instructions():
            return self.schema.instructions()
        else:
            divs = self.soup.find_all("div", {"class": "js-quizToggle"})
            for d in divs:
                if d.find("span", "article__shifted-jump-label"):
                    instructions = []
                    found_content = False
                    for element in d:
                        if not element.name:
                            continue

                        if element.name.startswith("h"):
                            if "Schritt" in element.text:
                                found_content = True
                                continue
                            elif found_content:
                                break

                        if not found_content:
                            continue

                        if element.name == "p" and element.text.strip():
                            instructions.append(element.text)

                    return "\n".join(instructions)

    def cuisine(self):
        try:
            return self.schema.cuisine()
        except SchemaOrgException:
            return None

    def description(self):
        cleaned_description = self.schema.description()
        return normalize_string(cleaned_description)

    def site_name(self):
        return "lecker.de"
