from ._abstract import AbstractScraper


class PingoDoce(AbstractScraper):
    @classmethod
    def host(cls):
        return "pingodoce.pt"

    def instructions(self):
        instructions = self.soup.find_all("div", {"class": "step-description"})
        return "\n".join([i.get_text() for i in instructions])

    def category(self):
        return None

    def cuisine(self):
        return None
