import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml, SchemaOrgException
from ._grouping_utils import IngredientGroup
from ._utils import get_minutes


_STREETKITCHEN_TIME_UL_LI = re.compile(
    r"^(Elkészítési|Sütési|Hűtési|Pácolási|Pihentetési)\s+idő\s*:",
    re.IGNORECASE,
)


class StreetKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "streetkitchen.hu"

    def ingredients(self):
        ingredients_list = []
        for item in self.soup.select(
            "div.w-full.rounded-b-md div.my-2.flex.items-center.gap-2.text-lg"
        ):
            divs = [
                child
                for child in item.children
                if getattr(child, "name", None) == "div"
            ]
            parts = [
                div.get_text(" ", strip=True)
                for div in divs
                if div.get_text(strip=True)
            ]
            if parts:
                text = " ".join(parts)
                text = text.replace("( ", "(").replace(" )", ")")
                ingredients_list.append(text)
        return ingredients_list

    def ingredient_groups(self):
        groups = []
        for group_block in self.soup.select("div.w-full.rounded-b-md > div > div"):
            heading_tag = group_block.select_one("h5.text-lg.font-bold")
            purpose = heading_tag.get_text(strip=True) if heading_tag else None

            if purpose == "":
                return [IngredientGroup(ingredients=self.ingredients())]

            ingredients = []
            for item in group_block.select("div.my-2.flex.items-center.gap-2.text-lg"):
                divs = [
                    child
                    for child in item.children
                    if getattr(child, "name", None) == "div"
                ]
                parts = [
                    div.get_text(" ", strip=True)
                    for div in divs
                    if div.get_text(strip=True)
                ]
                if parts:
                    text = " ".join(parts)
                    text = text.replace("( ", "(").replace(" )", ")")
                    ingredients.append(text)

            if ingredients:
                groups.append(IngredientGroup(ingredients=ingredients, purpose=purpose))

        if not groups:
            return [IngredientGroup(ingredients=self.ingredients())]
        return groups

    def total_time(self):
        if self.schema.data.keys() & {"totalTime", "prepTime", "cookTime"}:
            try:
                t = self.schema.total_time()
            except SchemaOrgException:
                t = None
            else:
                if t is not None:
                    return t
        return self._total_time_from_page()

    def _total_time_from_page(self):
        for p in self.soup.find_all("p"):
            text = p.get_text(" ", strip=True)
            m = re.match(
                r"Elkészítési\s+idő\s*:\s*(.+)$",
                text,
                flags=re.IGNORECASE,
            )
            if not m:
                continue
            minutes = get_minutes(m.group(1).strip())
            if minutes is not None:
                return minutes
        raise ElementNotFoundInHtml("total_time")

    def instructions(self):
        container = self.soup.select_one(
            "article.recipe-article"
        ) or self.soup.select_one("div.recipe-article")
        if not container:
            return ""

        instructions = []
        for child in container.children:
            name = getattr(child, "name", None)
            if name in ["p", "span"]:
                text = child.get_text(" ", strip=True)
                if text:
                    instructions.append(text)
            elif name == "ol":
                for li in child.find_all("li", recursive=False):
                    text = li.get_text(" ", strip=True)
                    if text:
                        instructions.append(text)
            elif name == "ul":
                if not instructions and self._is_times_metadata_ul(child):
                    continue
                break
            elif name in ["h2", "h3", "figure"]:
                continue
            elif name is not None:
                break

        return "\n".join(instructions)

    @staticmethod
    def _is_times_metadata_ul(ul) -> bool:
        items = ul.find_all("li", recursive=False)
        if not items:
            return False
        for li in items:
            t = li.get_text(" ", strip=True)
            if not t or not _STREETKITCHEN_TIME_UL_LI.match(t):
                return False
        return True
