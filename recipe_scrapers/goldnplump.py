from ._abstract import AbstractScraper


class GoldnPlump(AbstractScraper):
    @classmethod
    def host(cls):
        return "goldnplump.com"

    def ingredients(self):
        container = self.soup.select_one(".recipe-ingredeients .field-item p")
        if not container:
            return []

        lines = [line.strip() for line in container.stripped_strings]

        return [line for line in lines if not line.isupper()]
