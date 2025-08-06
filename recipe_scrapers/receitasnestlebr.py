import re

from ._abstract import AbstractScraper


class ReceitasNestleBR(AbstractScraper):
    @classmethod
    def host(cls):
        return "receitasnestle.com.br"

    def total_time(self):
        total_time = self.schema.total_time()
        if total_time is None:
            time_div = self.soup.find("div", {"class": "recipeDetail__infoItem--time"})
            if time_div:
                time_str = "".join(time_div.stripped_strings)
                total_time_str = re.search(r"\d+", time_str)
                if total_time_str:
                    total_time = int(total_time_str.group())
        return total_time

    def instructions(self):
        steps_div = self.soup.find("div", {"class": "recipeDetail__steps"})
        instructions = []
        if steps_div:
            step_items = steps_div.find_all("li")
            for step_item in step_items:
                div_content = step_item.find("div")
                if div_content:
                    instruction = div_content.get_text().strip()
                    cleaned_instruction = re.sub(r"^\d+\.\s*", "", instruction)
                    instructions.append(cleaned_instruction)
        return "\n".join(instructions)

    def ratings(self):
        rating_div = self.soup.find("div", {"class": "rating"})
        if rating_div:
            star_div = rating_div.find("div", {"class": "stars"})
            if star_div:
                star_class = star_div.get("class", [])
                for cls in star_class:
                    if cls.startswith("stars--"):
                        rating_str = cls.split("--")[-1]
                        if rating_str.isdigit():
                            return int(rating_str)
