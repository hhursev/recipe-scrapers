import re
from typing import List, Optional

from ._abstract import AbstractScraper


class OneHundredOneCookBooks(AbstractScraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.soup = self.soup.find("div", id="recipe")

    @classmethod
    def host(cls):
        return "101cookbooks.com"

    def author(self) -> Optional[str]:
        return self.schema.author()

    def title(self) -> Optional[str]:
        return self.soup.find("h1").get_text()

    def total_time(self) -> Optional[int]:
        return self.schema.total_time()

    def yields(self) -> Optional[str]:
        data = self.soup.find_all("p", limit=3, recursive=False)[-1].get_text()
        return re.search("([0-9]+) servings", data).group(1)

    def image(self) -> Optional[str]:
        return self.schema.image()

    def ingredients(self) -> Optional[List[str]]:
        ingredients = self.soup.find("blockquote").p.stripped_strings
        return list(ingredients)

    def instructions(self) -> Optional[str]:
        return self.soup.find_all("p", limit=2, recursive=False)[1].get_text(
            "\n", strip=True
        )

    def ratings(self) -> Optional[float]:
        return None
