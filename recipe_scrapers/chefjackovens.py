from ._abstract import AbstractScraper


class ChefJackOvens(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefjackovens.com"

    def instructions(self):
        groups = self.soup.select("div.wprm-recipe-instruction-group")
        if groups and any(g.find("h4") for g in groups):
            steps = []
            for group in groups:
                if group.find("h4"):
                    for li in group.select(
                        "ul.wprm-recipe-instructions li.wprm-recipe-instruction"
                    ):
                        text = li.select_one(".wprm-recipe-instruction-text")
                        if text:
                            steps.append(text.get_text(strip=True))
            return "\n".join(steps)
        return self.schema.instructions()
