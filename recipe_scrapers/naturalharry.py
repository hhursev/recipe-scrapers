from ._abstract import AbstractScraper
from ._utils import normalize_string


class NaturalHarry(AbstractScraper):
    @classmethod
    def host(cls):
        return "naturalharry.com.au"

    def author(self):
        author = self.soup.find("a", class_="author")
        return author.get_text(strip=True) if author else None

    def title(self):
        title = self.soup.find("h1", class_="wd-entities-title")
        return normalize_string(title.get_text(strip=True)) if title else None

    def language(self):
        return "en-US"

    def description(self):
        description_tag = self.soup.find("meta", attrs={"property": "og:description"})
        if description_tag:
            return normalize_string(description_tag.get("content", ""))
        return None

    def category(self):
        category = self.soup.find("div", class_="wd-post-cat")
        return (
            [
                normalize_string(cat.get_text(strip=True))
                for cat in category.find_all("a")
            ]
            if category
            else None
        )

    def total_time(self):
        pre_blocks = self.soup.find_all("pre", class_="wp-block-preformatted")

        for block in pre_blocks:
            block_text = block.get_text()
            if "Prep time:" in block_text and "Cook time:" in block_text:
                total_time = 0
                for line in block_text.splitlines():
                    if "Prep time:" in line or "Cook time:" in line:
                        time_number = "".join(filter(str.isdigit, line))
                        total_time += int(time_number) if time_number else 0

                return f"{total_time} minutes" if total_time > 0 else None

        return None

    def ingredients(self):
        content = self.soup.find("div", class_="wd-entry-content")
        if content:
            pre_blocks = content.find_all("pre", class_="wp-block-preformatted")
            ingredients = []
            for pre in pre_blocks:
                pre_text = pre.get_text()
                if any(
                    keyword in pre_text
                    for keyword in ["CRISPY CAULIFLOWER", "CHIPOTLE MAYO", "TO SERVE"]
                ):
                    lines = pre_text.splitlines()
                    for line in lines:
                        if any(
                            unit in line
                            for unit in [
                                "cup",
                                "teaspoon",
                                "tablespoon",
                                "head",
                                "ripe",
                                "mini",
                            ]
                        ):
                            ingredients.append(normalize_string(line))
            return ingredients
        return []

    def instructions_list(self):
        instructions = self.instructions()
        if isinstance(instructions, list):
            return instructions  # Already a list
        elif isinstance(instructions, str):
            return [
                normalize_string(step)
                for step in instructions.split("\n")
                if step.strip()
            ]
        return []

    def instructions(self):
        content = self.soup.find("div", class_="wd-entry-content")
        if content:
            instructions = []
            pre_blocks = content.find_all("pre")
            for pre in pre_blocks:
                if any(
                    keyword in pre.get_text()
                    for keyword in ["Preheat oven", "Coat cauliflower", "Serve"]
                ):
                    instructions.extend(pre.get_text().splitlines())
            return [normalize_string(step) for step in instructions if step.strip()]
        return []

    def image(self):
        img_container = self.soup.find("div", class_="wd-single-post-img")
        img = img_container.find("img") if img_container else None
        return img["src"] if img else None

    def yields(self):
        pre_blocks = self.soup.find_all("pre", class_="wp-block-preformatted")

        for block in pre_blocks:
            block_text = block.get_text()
            if "Makes:" in block_text:
                for line in block_text.splitlines():
                    if "Makes:" in line:
                        return normalize_string(line.split(":")[-1])

        return None

    def cuisine(self):
        return None
