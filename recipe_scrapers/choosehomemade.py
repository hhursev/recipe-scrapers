from ._abstract import AbstractScraper


class ChooseHomemade(AbstractScraper):
    @classmethod
    def host(cls):
        return "choosehomemade.org"

    def ingredients(self):
        ingredients = []
        for el in self.soup.select(
            "ul.recipe-ingredients__inner-list li .recipe-ingredient__label"
        ):
            text = el.get_text()
            first_non_space = next(
                (i for i, c in enumerate(text) if not c.isspace()), len(text)
            )
            cleaned_text = text[first_non_space:]
            if cleaned_text:
                ingredients.append(cleaned_text)
        return ingredients

    def instructions(self):
        return "\n".join(
            el.get_text(strip=True)
            for el in self.soup.select("ol.recipe-steps__inner li .recipe-step__inner")
        )
