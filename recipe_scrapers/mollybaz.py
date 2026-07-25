import functools

from bs4 import Tag

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._grouping_utils import IngredientGroup
from ._utils import get_minutes, get_yields, normalize_string


class MollyBaz(AbstractScraper):
    @classmethod
    def host(cls):
        return "mollybaz.com"

    def author(self):
        return "Molly Baz"

    @functools.cached_property
    def _page_rows(self):
        # data-node is a Beaver Builder attribute present only on top-level
        # layout rows, not on nested content wrappers with the same fl-row class
        return [r for r in self.soup.find_all(class_="fl-row") if r.get("data-node")]

    @functools.cached_property
    def _hero_row(self):
        for row in self._page_rows:
            if "recipe-hero" in row.get("class", []):
                return row
        raise ElementNotFoundInHtml("recipe-hero row")

    @functools.cached_property
    def _hero_modules(self):
        return [
            m for m in self._hero_row.find_all(class_="fl-module") if m.get("data-node")
        ]

    @functools.cached_property
    def _ingredient_column(self):
        for row in self._page_rows:
            if "recipe-hero" in row.get("class", []):
                continue
            col_group = row.find(class_="fl-col-group")
            if not col_group:
                continue
            direct_cols = [
                c
                for c in col_group.children
                if hasattr(c, "get") and "fl-col" in c.get("class", [])
            ]
            if len(direct_cols) != 2:
                continue
            modules = [
                m
                for m in direct_cols[0].find_all(class_="fl-module")
                if m.get("data-node")
            ]
            if any(
                "fl-module-rich-text" in m.get("class", []) and m.find("li")
                for m in modules
            ):
                return modules
        raise ElementNotFoundInHtml("ingredient column")

    @functools.cached_property
    def _ingredient_groups(self):
        groups = []
        current_heading = None
        current_items = []

        for mod in self._ingredient_column:
            classes = mod.get("class", [])
            if "fl-module-heading" in classes:
                if current_heading is not None and current_items:
                    groups.append(
                        IngredientGroup(
                            ingredients=current_items, purpose=current_heading
                        )
                    )
                current_heading = normalize_string(mod.get_text())
                current_items = []
            elif "fl-module-rich-text" in classes:
                lis = mod.find_all("li")
                if lis:
                    current_items = [normalize_string(li.get_text()) for li in lis]

        if current_heading is not None and current_items:
            groups.append(
                IngredientGroup(ingredients=current_items, purpose=current_heading)
            )

        return groups

    def title(self):
        h1 = self._hero_row.find("h1")
        if h1:
            return normalize_string(h1.get_text())
        raise ElementNotFoundInHtml("h1 title")

    def yields(self):
        for mod in self._hero_modules:
            text = mod.get_text().strip()
            if text.upper().startswith(("SERVES", "MAKES")):
                return get_yields(text)
        raise ElementNotFoundInHtml("serves/makes heading")

    def description(self):
        for mod in self._hero_modules:
            if "fl-module-rich-text" in mod.get("class", []):
                return normalize_string(mod.get_text())
        raise ElementNotFoundInHtml("description rich-text")

    def total_time(self):
        for mod in self._hero_modules:
            text = mod.get_text().strip()
            if "Total Time:" in text:
                return get_minutes(text)
        raise ElementNotFoundInHtml("total time heading")

    def ingredients(self):
        return [i for group in self._ingredient_groups for i in group.ingredients]

    def ingredient_groups(self):
        return self._ingredient_groups

    def instructions(self):
        instructions_mod = self.soup.find(class_="instructions")
        if not instructions_mod:
            raise ElementNotFoundInHtml("instructions module")
        rich_text = instructions_mod.find(class_="fl-rich-text")
        if not rich_text:
            raise ElementNotFoundInHtml("fl-rich-text in instructions")

        steps = []
        for elem in rich_text.children:
            if not isinstance(elem, Tag):
                continue
            if elem.name in ("h2", "h3", "h4"):
                steps.append(normalize_string(elem.get_text()))
            elif elem.name == "ul":
                for li in elem.find_all("li"):
                    steps.append(normalize_string(li.get_text()))

        return "\n".join(steps)

    def category(self):
        cat_mod = self.soup.find(string=lambda s: s and "Filed Under:" in s)
        if cat_mod:
            parent = cat_mod.find_parent()
            if parent:
                link = parent.find("a")
                if link:
                    return normalize_string(link.get_text())
        raise ElementNotFoundInHtml("category")
