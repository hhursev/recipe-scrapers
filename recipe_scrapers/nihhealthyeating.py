from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class NIHHealthyEating(AbstractScraper):
    @classmethod
    def host(cls):
        return "healthyeating.nhlbi.nih.gov"

    def title(self):
        return self.soup.h1.get_text().strip()

    def total_time(self):
        time_table = self.soup.find("table", {"class": "recipe_time_table"})

        return sum([get_minutes(td) for td in time_table.find_all("td")])

    def yields(self):
        time_table = self.soup.find("table", {"class": "recipe_time_table"})

        i = 0
        for t in time_table.findAll("th"):
            if "Yields" in t:
                break
            i += 1

        if i >= len(time_table.findAll("td")):
            return
        return get_yields(time_table.find_all("td")[i])

    def ingredients(self):
        ingredients = self.soup.find("div", {"id": "ingredients"}).findAll("p")

        return [normalize_string(paragraph.get_text()) for paragraph in ingredients]

    def instructions(self):
        instructions = self.soup.find("div", {"id": "recipe_directions"}).findAll(
            "div", {"class": "steptext"}
        )

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )
