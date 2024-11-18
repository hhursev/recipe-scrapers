from ._abstract import AbstractScraper


class Cookomix(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookomix.com"

    def instructions(self):
        instructions_html = self.soup.select_one(".instructions.dsb-select ol")

        instructions = instructions_html.find_all("li")
        return "\n".join(li.get_text() for li in instructions)
