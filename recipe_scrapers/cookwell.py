from ._abstract import AbstractScraper
import re


class CookWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookwell.com"

    def nutrients(self):
        nutrition_pattern = re.compile(
            r'{\\"calories\\":(?P<calories>\d+),\\"carbohydrates\\":(?P<carbohydrates>\d+),\\"fat\\":(?P<fat>\d+),\\"protein\\":(?P<protein>\d+)}'
        )

        nutrition_script = self.soup.find("script", string=nutrition_pattern)
        if nutrition_script:
            match = nutrition_pattern.search(nutrition_script.string)
            if match:
                nutrition_info = match.groupdict()
                return {
                    "calories": nutrition_info["calories"],
                    "carbohydrateContent": f'{nutrition_info["carbohydrates"]} g',
                    "fatContent": f'{nutrition_info["fat"]} g',
                    "proteinContent": f'{nutrition_info["protein"]} g',
                }

        return self.schema.nutrients()
