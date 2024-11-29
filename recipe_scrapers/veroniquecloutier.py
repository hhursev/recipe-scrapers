from ._abstract import AbstractScraper
from ._utils import normalize_string


class VeroniqueCloutier(AbstractScraper):
    @classmethod
    def host(cls):
        return "veroniquecloutier.com"

    def author(self):
        return self.soup.find("strong").get_text()

    def title(self):
        return self.soup.find("h1", {"class": "title -main -page-title"}).get_text()

    def category(self):
        return (
            self.soup.find("div", {"class": "categories"})
            .findChild("span", {"class": "separator"})
            .get_text()
        )

    # chose not to implement total_time because it often not present in the recipe
    # def total_time(self):
    #     return None

    def yields(self):
        potion_line = self.soup.find(
            string=lambda text: text and "portions" in text.lower()
        )
        french_numbers = [
            "un",
            "deux",
            "trois",
            "quatre",
            "cinq",
            "six",
            "sept",
            "huit",
            "neuf",
            "dix",
            "onze",
            "douze",
            "treize",
            "quatorze",
            "quinze",
        ]
        special_cases = {"dizaine": 10, "douzaine": 12}
        if potion_line:
            words = potion_line.split()  # Split text into words
            for word in words:
                if word.isdigit():
                    return str(word) + " portions"
                elif word.lower() in french_numbers:
                    return str(french_numbers.index(word.lower()) + 1) + " portions"
                elif word.lower() in special_cases:
                    return str(special_cases[word.lower()]) + " portions"
        return None

    def image(self):
        return self.soup.find("figure", {"class": "attachment- size- wp-post-image"})[
            "src"
        ]

    def ingredients(self):
        start = self.soup.find(
            string=lambda text: text and text.lower() == "ingrédients"
        )
        end = self.soup.find(string=lambda text: text and text.lower() == "préparation")

        ingredient_list = []

        if start and end:
            for sibling in start.find_all_next():
                if sibling.string and "préparation" in sibling.string.lower():
                    break
                if sibling.name == "ul":
                    ingredient_list.extend([li.text for li in sibling.find_all("li")])

        return ingredient_list

    def instructions(self):
        start = self.soup.find(
            string=lambda text: text and text.lower() == "préparation"
        )

        instruction_list = []

        if start:
            for sibling in start.find_all_next():
                if sibling.name == "div":
                    break
                if sibling.name == "ol":
                    instruction_list.extend([li.text for li in sibling.find_all("li")])
                elif sibling.name == "p" and sibling.text[0].isdigit():
                    instruction_list.append(sibling.text[3:])

        return "\n".join(instruction_list)

    def description(self):
        return normalize_string(
            self.soup.find("div", {"class": "post-excerpt"}).get_text()
        )
