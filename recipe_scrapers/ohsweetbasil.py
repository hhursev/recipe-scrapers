from ._abstract import AbstractScraper


class OhSweetBasil(AbstractScraper):
    @classmethod
    def host(cls):
        return "ohsweetbasil.com"

    def ingredients(self):
        return [
            " ".join(
                span.get_text(strip=True)
                for span in i.select(
                    ".wprm-recipe-ingredient-amount, "
                    ".wprm-recipe-ingredient-unit, "
                    ".wprm-recipe-ingredient-name, "
                    ".wprm-recipe-ingredient-notes"
                )
            )
            for i in self.soup.select(".wprm-recipe-ingredient")
        ]
