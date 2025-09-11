from ._abstract import AbstractScraper


class StreetKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "streetkitchen.hu"

    def ingredients(self):
        ingredients_list = []
        for item in self.soup.select(
            "div.w-full.rounded-b-md div.my-2.flex.items-center.gap-2.text-lg"
        ):
            divs = [
                child
                for child in item.children
                if getattr(child, "name", None) == "div"
            ]
            parts = [
                div.get_text(" ", strip=True)
                for div in divs
                if div.get_text(strip=True)
            ]
            if parts:
                ingredients_list.append(" ".join(parts))
        return ingredients_list

    def instructions(self):
        article = self.soup.select_one("article.recipe-article")
        if article:
            instructions = []
            for child in article.children:
                if getattr(child, "name", None) == "p":
                    text = child.get_text(" ", strip=True)
                    if text:
                        instructions.append(text)
                elif getattr(child, "name", None) is not None:
                    break
            return "\n".join(instructions)
        return ""
