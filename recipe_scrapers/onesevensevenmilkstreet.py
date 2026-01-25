from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields
from ._grouping_utils import group_ingredients


class OneSevenSevenMilkStreet(AbstractScraper):
    @classmethod
    def host(cls):
        return "177milkstreet.com"

    def title(self):
        title_tag = self.soup.find("h1", class_="RecipeHeader_title__omDuT")
        if title_tag:
            return title_tag.get_text(strip=True)

    def author(self):
        author_span = self.soup.find("span", attrs={"data-authors-text": True})
        author_link = author_span.find("a") if author_span else None
        if author_link:
            return author_link.get_text(strip=True)

    def _find_li_by_text(self, search_text, split_text):
        for li in self.soup.select("li"):
            text = li.get_text(strip=True).lower()
            if search_text in text:
                return li.get_text(strip=True).split(split_text)[-1].strip()

    def yields(self):
        yield_text = self._find_li_by_text("makes", "Makes")
        return get_yields(yield_text)

    def total_time(self):
        total_time_text = self._find_li_by_text("cook time", "Cook Time")
        return get_minutes(total_time_text)

    def prep_time(self):
        prep_time_text = self._find_li_by_text(
            "active time", "Active time plus cooling"
        )
        return get_minutes(prep_time_text)

    def ingredients(self):
        section = self.soup.find("div", class_=lambda x: x and "sidebarContent" in x)
        if not section:
            return []

        ingredients = []
        for li in section.select("ul li"):
            if (
                li.find("span")
                and "lineheading" in " ".join(li.get("class", [])).lower()
            ):
                continue
            if li.find("p"):
                text = li.get_text(separator=" ", strip=True)
                if text and not text.lower().startswith(
                    ("story", "radio episode", "tv episode")
                ):
                    ingredients.append(text)
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "li[class*=ingredientSectionHeadingItemContainer] span[class*=LineHeading_title]",
            "ul[class*=ItemLabelList_list] li:has(p)",
        )

    def instructions(self):
        container = self.soup.find("div", class_=lambda x: x and "instructions" in x)
        if not container:
            return

        instructions = []
        seen = set()
        for step in container.select("div"):
            p = step.find("p")
            if p:
                text = p.get_text(strip=True)
                if text and text not in seen:
                    instructions.append(text)
                    seen.add(text)
        return "\n".join(instructions)
