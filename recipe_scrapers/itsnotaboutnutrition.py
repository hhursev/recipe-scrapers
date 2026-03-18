from ._abstract import AbstractScraper


class ItsNotAboutNutrition(AbstractScraper):
    @classmethod
    def host(cls):
        return "itsnotaboutnutrition.com"

    def instructions(self):
        instructions = []
        for item in self.soup.select(".wprm-recipe-instruction"):
            text_elem = item.select_one(".wprm-recipe-instruction-text")
            if text_elem:
                text = text_elem.get_text(strip=True)
                if text:
                    instructions.append(text)
        return "\n".join(instructions)
