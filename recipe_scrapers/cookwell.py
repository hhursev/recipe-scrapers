from ._abstract import AbstractScraper
import re


class CookWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookwell.com"

    def nutrients(self):
        nutrition = None
        nutrition_pattern = re.compile(
            r"{\\\"calories\\\":(?P<calories>\d+),\\\"carbohydrates\\\":(?P<carbohydrates>\d+),\\\"fat\\\":(?P<fat>\d+),\\\"protein\\\":(?P<protein>\d+)}"
        )

        nutrition_script = self.soup.find("script", string=nutrition_pattern)
        if nutrition_script:
            nutrition_info = nutrition_pattern.search(
                nutrition_script.string
            ).groupdict()
            if nutrition_info:
                nutrition = {
                    "calories": f'{nutrition_info["calories"]} calories',
                    "carbohydrateContent": f'{nutrition_info["carbohydrates"]} g',
                    "fatContent": f'{nutrition_info["fat"]} g',
                    "proteinContent": f'{nutrition_info["protein"]} g',
                }

        return nutrition if nutrition else super().nutrients()
