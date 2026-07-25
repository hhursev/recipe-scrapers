from ._abstract import AbstractScraper
from ._utils import get_minutes


class Abril(AbstractScraper):
    @classmethod
    def host(cls):
        return "claudia.abril.com.br"

    def instructions(self):
        instructions = []
        for item in self.soup.select("section.receita-preparo .preparo-item"):
            text = item.get_text(" ", strip=True)
            if text:
                instructions.append(text)
        return "\n".join(instructions)

    def _extract_time_element(self, label_keywords):
        for box in self.soup.select("section.receita-lista-preparo .box-primario"):
            title = box.select_one(".box-primario-title")
            if title:
                title_text = title.get_text(strip=True).lower()
                if any(keyword in title_text for keyword in label_keywords):
                    value = box.select_one(".progress-text")
                    if value:
                        time_str = value.get_text(strip=True)
                        return get_minutes(time_str)
        return None

    def prep_time(self):
        return self._extract_time_element(["preparo"])

    def cook_time(self):
        return self._extract_time_element(["cocção", "coccao"])
