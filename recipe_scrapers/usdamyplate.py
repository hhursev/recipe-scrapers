from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_minutes, get_yields, normalize_string


class USDAMyPlate(AbstractScraper):
    @classmethod
    def host(cls):
        return "myplate.gov"

    def site_name(self):
        raise StaticValueException(return_value="MyPlate")

    def title(self):
        return self.soup.h1.get_text().strip()

    def total_time(self):
        # not in every recipe has time given
        full_detail = self.soup.find(
            "div", {"class": "mp-recipe-full__overview desktop:grid-col-5 grid-row"}
        )

        minutes = 0
        for span in full_detail.findAll(
            "span", {"class": "mp-recipe-full__detail--data"}
        ):
            if "minute" in span.get_text().lower() or "hour" in span.get_text().lower():
                minutes += get_minutes(span)

        if minutes == 0:
            return None

        return minutes

    def yields(self):
        full_detail = self.soup.find(
            "div", {"class": "mp-recipe-full__overview desktop:grid-col-5 grid-row"}
        )

        spans = full_detail.findAll("span")
        i = 0
        for span in spans:
            if "Makes:" in span:
                return get_yields(spans[i + 1])
            i += 1

    def image(self):
        div = self.soup.find(
            "div",
            {
                "class": "field field--name-field-recipe-image field--type-image field--label-visually_hidden"
            },
        )
        url = div.find("img")["src"]
        # return only the portion before the question mark
        return url.split("?")[0]

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"class": "field--name-field-ingredients"}
        ).findAll("li")

        return [normalize_string(paragraph.get_text()) for paragraph in ingredients]

    def instructions(self):
        div = self.soup.find(
            "div",
            {
                "class": "clearfix text-formatted field field--name-field-instructions field--type-text-long field--label-above"
            },
        )
        instructions = div.find("div", {"class", "field__item"})

        return "\n".join(instructions.stripped_strings)

    def nutrients(self):
        nutrition = {}

        table = self.soup.find(
            "form", {"class": "mp-recipe-full__nutrition-form"}
        ).find("table")
        rows = table.find_all("tr")

        elements = []
        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            elements.append([ele for ele in cols if ele])

        for el in elements:
            if len(el) > 1:
                nutrition[el[0]] = el[1]

        return nutrition

    def serving_size(self):
        return normalize_string(
            self.soup.find("div", {"class": "field--name-field-recipe-serving-size"})
            .find("span", {"class": "field__item"})
            .get_text()
        )

    def description(self):
        return normalize_string(
            self.soup.find("div", {"class": "mp-recipe-full__description"})
            .find("p")
            .get_text()
        )

    def recipe_source(self):
        return normalize_string(
            self.soup.find("span", {"class": "field--name-field-source"})
            .find("p")
            .get_text()
        )
