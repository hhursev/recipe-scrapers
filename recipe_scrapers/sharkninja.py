from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields


class SharkNinja(AbstractScraper):
    @classmethod
    def host(cls):
        return "sharkninja.com"

    def author(self):
        author_tag = self.soup.select_one(
            "div.recipe-author__section span.recipe-author__name"
        )
        if author_tag:
            return author_tag.get_text(strip=True).replace("By ", "", 1)

    def ingredients(self):
        container = self.soup.select_one(
            "div.recipe-pdp-ingredients__ingredients-body div[data-method-type]:not(.d-none)"
        )
        if container:
            return [li.get_text(strip=True) for li in container.select("ul > li")]

    def instructions(self):
        container = self.soup.select_one(
            "div.recipe-pdp-instructions__steps div[data-method-type]:not(.d-none)"
        )
        if not container:
            return

        instructions = []
        for step in container.select("p"):
            text = step.get_text(" ", strip=True)
            parts = text.split(" ", 2)
            if len(parts) == 3 and parts[0].lower() == "step":
                instructions.append(parts[2].strip())

        return "\n".join(instructions)

    def description(self):
        meta = self.soup.select_one('meta[name="description"]')
        if not meta:
            return
        return meta["content"]

    def yields(self):
        table = self.soup.select_one("div.recipe-table")
        if table:
            for cell in table.select("div.recipe-table-cell"):
                label = cell.select_one("div.recipe-table-label")
                if label and "servings" in label.get("data-attr-icon", "").lower():
                    value = cell.select_one("div.recipe-table-value")
                    if value:
                        return get_yields(value.get_text(strip=True))

    def total_time(self):
        table = self.soup.select_one("div.recipe-table")
        if table:
            for cell in table.select("div.recipe-table-cell"):
                label = cell.select_one("div.recipe-table-label")
                if label and "total time" in label.get_text(strip=True).lower():
                    value = cell.select_one("div.recipe-table-value")
                    if value:
                        return get_minutes(value.get_text(strip=True))

    def equipment(self):
        container = self.soup.select_one("section.recipe-pdp-ingredients__utensils")
        if container:
            return [li.get_text(strip=True) for li in container.select("ul > li")]
