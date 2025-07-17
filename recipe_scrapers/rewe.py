from ._abstract import AbstractScraper


class Rewe(AbstractScraper):
    @classmethod
    def host(cls):
        return "rewe.de"

    def equipment(self):
        header = self.soup.find("h2", string="Utensilien")
        if header:
            section = header.find_parent("div")
            if section:
                tools = section.find("p", class_="kitchen-tools-entries")
                if tools:
                    text = tools.get_text(separator=",", strip=True)
                    return [item.strip() for item in text.split(",") if item.strip()]
        return []

    def instructions(self):
        instructions = self.schema.instructions()
        filtered_instructions = "\n".join(
            line for line in instructions.split("\n") if not line.startswith("Schritt")
        )
        return filtered_instructions
