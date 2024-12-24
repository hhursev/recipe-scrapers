from ._abstract import AbstractScraper
from ._utils import normalize_string


class Reishunger(AbstractScraper):
    @classmethod
    def host(cls):
        return "reishunger.de"

    def _filter_ingredients(self):
        """
        Sort through the 'ingredients' heading from the page; this can contain
        a mixture of food ingredients and also kitchen equipment items.
        """
        # Find the "ingredients" heading (Zutaten in German)
        heading = self.soup.find("h2", {"id": "zutaten"})

        ingredients, equipment = [], []
        in_equipment = False

        # Skip past the "portions" (Portionnen in German) heading
        portions = heading.find_next_sibling("div")
        container = portions.find_next_sibling("div")

        # Iterate through the ingredient list
        for element in container.find_all("div"):
            # If we reach an item that says "Helpful for the preparation", then all
            # remaining items are kitchen equipment (optional, but useful for the recipe).
            if "Hilfreich für die Zubereitung" in element.text:
                in_equipment = True

            # Find leaf-node div elements; these are the item descriptions
            description = element.find("div")
            if description and not description.find("div"):
                ingredient = normalize_string(description.text)
                (equipment if in_equipment else ingredients).append(ingredient)

        return ingredients, equipment

    def ingredients(self):
        filtered_ingredients, _ = self._filter_ingredients()
        return filtered_ingredients

    def equipment(self):
        _, filtered_equipment = self._filter_ingredients()
        return filtered_equipment

    def instructions(self):
        # Find the "instructions" heading (Zubereitung in German)
        heading = self.soup.find("h2", {"id": "zubereitung"})

        chose_method = False
        results = []

        container = heading.find_next_sibling("div")

        # Iterate through the instruction list
        for step in container.find("div").find_next_siblings("div"):

            # Sometimes recipes provide multiple rice prep options; choose the first so
            # that we produce a complete recipe.
            if step.find("span", string=lambda text: text.startswith("Ausgewählte")):

                # Skip method headings after the first one
                if chose_method:
                    continue

                # Add the title of the first method
                for method in step.find("section").find_all("div", {"id": True}):
                    title = method.find("p")
                    results.append(normalize_string(title.text))
                    break

                # Include all the steps from the first method
                for substep in method.find_all("li"):
                    results.append(normalize_string(substep.text))

                chose_method = True
                continue

            # Skip step number introductions (Schritt 01, ...)
            if "leading-normal" in step.attrs.get("class", []):
                continue

            # Split HTML linebreaks and return each line/sentence as an individual instruction
            for br in step.find_all("br"):
                br.replace_with("\n")
            for line in step.text.split("\n"):
                instruction = normalize_string(line)
                if instruction:
                    results.append(instruction)

        # filter out empty lines
        results = [instruction for instruction in results if instruction]
        return "\n".join(results)
