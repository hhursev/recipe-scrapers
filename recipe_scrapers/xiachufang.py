import json
from typing import cast

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._utils import normalize_string


class XiaChuFang(AbstractScraper):
    @classmethod
    def host(cls):
        return "xiachufang.com"

    def site_name(self):
        return "下厨房"

    def language(self):
        return "zh-CN"

    def canonical_url(self):
        url = self.soup.select_one("link[rel='canonical']")
        if not url:
            raise ElementNotFoundInHtml("Could not find canonical url")
        return normalize_string(url.attrs["href"])

    def title(self):
        title_tag = self.soup.select_one("h1.page-title")
        if not title_tag:
            raise ElementNotFoundInHtml("Could not find title")
        return normalize_string(title_tag.get_text())

    def author(self):
        author_tag = self.soup.select_one("div.author")
        if not author_tag:
            raise ElementNotFoundInHtml("Could not find author")
        return normalize_string(author_tag.get_text())

    def description(self):
        description_tag = self.soup.select_one("div.desc")
        if not description_tag:
            raise ElementNotFoundInHtml("Could not find description")
        desc = normalize_string(description_tag.get_text())
        tip_tag = self.soup.select_one("div.tip")
        if tip_tag:
            desc += f"\n[小贴士]: {normalize_string(tip_tag.get_text())}"
        return desc

    def image(self):
        image_tag = self.soup.select_one("meta[property='og:image']")
        if not image_tag:
            raise ElementNotFoundInHtml("Could not find image")
        return normalize_string(image_tag.attrs["content"])

    def category(self):
        category_tags = self.soup.select("div.recipe-cats > a")
        return ", ".join((normalize_string(t.get_text()) for t in category_tags))

    def total_time(self):
        return None

    def yields(self):
        return None

    def ingredients(self):
        ingredient_table = self.soup.select_one("div.ings")
        if not ingredient_table:
            raise ElementNotFoundInHtml("Could not find ingredients")

        def combiner(ing):
            name = ing.select_one("td.name")
            unit = ing.select_one("td.unit")
            if not name or not unit:
                return None
            return (
                normalize_string(unit.get_text())
                + " "
                + normalize_string(name.get_text())
            ).strip()

        ings = ingredient_table.find_all("tr")
        return list(filter(None, (combiner(ing) for ing in ings)))

    def _parse_instructions(self) -> list[dict[str, str]]:
        instructions = self.soup.select("div.steps li")
        if not instructions:
            return []

        def extractor(ins):
            text = ins.select_one("p.text")
            if not text:
                return None
            img = ins.select_one("img")
            return {
                "text": normalize_string(text.get_text()),
                "img": img.attrs["src"] if img else None,
            }

        return list(filter(None, (extractor(ins) for ins in instructions)))

    def instructions(self):
        return "\n".join((ins["text"] for ins in self._parse_instructions()))

    def _get_recipe(self) -> dict[str, str | list[str] | dict[str, str | int]] | None:
        recipe_json = self.soup.select_one("script[type='application/ld+json']")
        if not recipe_json:
            return None
        return json.loads(recipe_json.get_text())

    def ratings(self):
        recipe = self._get_recipe()
        if not recipe:
            return None
        aggregate_rating = cast(dict[str, str | int], recipe["aggregateRating"])
        if not aggregate_rating:
            return None
        return float(aggregate_rating["ratingValue"])

    def ratings_count(self):
        recipe = self._get_recipe()
        if not recipe:
            return None
        aggregate_rating = cast(dict[str, str | int], recipe["aggregateRating"])
        if not aggregate_rating:
            return None
        return float(aggregate_rating["reviewCount"])

    def keywords(self):
        recipe = self._get_recipe()
        if not recipe:
            return []
        keywords = cast(list[str], recipe["keywords"])
        return [normalize_string(k) for k in keywords]
