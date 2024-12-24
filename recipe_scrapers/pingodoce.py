from ._abstract import AbstractScraper


class PingoDoce(AbstractScraper):
    @classmethod
    def host(cls):
        return "pingodoce.pt"

    def instructions(self):
        instructions = self.soup.findAll("div", {"class": "step-description"})
        return "\n".join([i.get_text() for i in instructions])
