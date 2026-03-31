from ._abstract import AbstractScraper


class Cookomix(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookomix.com"

    def instructions(self):
        container = self.soup.select_one(".instructions.dsb-select")

        instructions = []

        if container:
            for child in container.find_all(recursive=False):
                if child.name == "h2":
                    text = child.get_text()
                    if text:
                        instructions.append(text)

                elif child.name == "ol":
                    for li in child.find_all("li"):
                        text = li.get_text()
                        if text:
                            instructions.append(text)

        return "\n".join(instructions)
