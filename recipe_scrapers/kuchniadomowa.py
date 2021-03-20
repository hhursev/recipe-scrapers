from typing import Optional

from ._abstract import AbstractScraper


class KuchniaDomowa(AbstractScraper):
    @classmethod
    def host(cls):
        return "kuchnia-domowa.pl"

    def title(self) -> Optional[str]:
        return self.soup.find("h2").get_text().strip()

    def image(self) -> Optional[str]:
        urls = self.soup.findAll("img", {"class": "article-img", "id": "article-img-1"})
        return f"https:{urls[1]['src']}"

    def instructions(self) -> Optional[str]:
        instructions = self.soup.find("div", {"id": "recipe-instructions"}).findAll(
            "li"
        )
        instructions = [x.text for x in instructions]
        return "\n".join(instructions)
