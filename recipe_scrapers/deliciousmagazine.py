import re

from ._abstract import AbstractScraper
from ._exceptions import ElementNotFoundInHtml
from ._utils import normalize_string


class DeliciousMagazine(AbstractScraper):
    @classmethod
    def host(cls):
        return "deliciousmagazine.co.uk"

    def author(self):
        for link in self.soup.select(
            "p.recipe-author-details a, .author-name a[href*='/contributors/'], .author-name a[href*='/authors/']"
        ):
            text = normalize_string(link.get_text())
            if text:
                return text
        plain = self.soup.select_one(".author-name")
        if plain:
            text = normalize_string(plain.get_text())
            text = re.sub(r"^Recipe by:\s*", "", text, flags=re.IGNORECASE).strip()
            if text:
                return text
        raise ElementNotFoundInHtml("Author not found.")

    def site_name(self):
        return self.opengraph.site_name()

    def title(self):
        title = self.soup.select_one(
            ".recipe-title h1, article section.two-column h1.h2"
        )
        if title:
            return normalize_string(title.get_text())
        raise ElementNotFoundInHtml("Recipe title not found.")

    def total_time(self):
        for li in self.soup.select(".list-guidance li, .recipe-guidance li"):
            text = li.get_text(" ", strip=True)
            if "Prep time" not in text or "Cook time" not in text:
                continue
            prep = re.search(r"Prep time\s+(\d+)\s*min", text)
            cook = re.search(r"Cook time\s+(\d+)\s*min", text)
            if prep and cook:
                return int(prep.group(1)) + int(cook.group(1))
        raise ElementNotFoundInHtml("Prep and cook times not found.")

    def yields(self):
        for li in self.soup.select(".list-guidance li, .recipe-guidance li"):
            text = li.get_text(" ", strip=True)
            if "Serves" in text:
                match = re.search(r"Serves\s+(\d+)", text)
                if match:
                    return f"{match.group(1)} servings"
            if "Makes" in text:
                match = re.search(r"Makes\s+(\d+)", text)
                if match:
                    return f"Makes {match.group(1)}"
        raise ElementNotFoundInHtml("Yield (serves/makes) not found.")

    def image(self):
        return self.opengraph.image()

    def ingredients(self):
        items = [
            normalize_string(li.get_text())
            for li in self.soup.select("#ingredients ul li")
        ]
        items = [i for i in items if i]
        if not items:
            raise ElementNotFoundInHtml("No ingredients found.")
        return items

    def instructions(self):
        steps = []
        for li in self.soup.select("#method ol li"):
            if "ad-li" in li.get("class", []):
                continue
            step = normalize_string(li.get_text())
            if step:
                steps.append(step)
        if not steps:
            raise ElementNotFoundInHtml("No method steps found.")
        return "\n".join(steps)
