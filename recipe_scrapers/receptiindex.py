from ._abstract import AbstractScraper


class ReceptiIndex(AbstractScraper):
    @classmethod
    def host(cls):
        return "recepti.index.hr"

    def instructions(self):
        container = self.soup.select_one(
            "div.preparation-step-new__text div.html-container"
        )

        instructions = []

        if container:
            for tag in container.find_all(["p"]):
                text = tag.get_text(" ", strip=True)
                if text:
                    instructions.append(text)

        return "\n".join(instructions)
