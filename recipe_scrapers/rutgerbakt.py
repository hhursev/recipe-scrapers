from ._abstract import AbstractScraper


class RutgerBakt(AbstractScraper):
    @classmethod
    def host(cls):
        return "rutgerbakt.nl"

    def author(self):
        return "Rutger van den Broek"

    def title(self):
        title_raw = self.schema.title()
        return title_raw.replace(" – recept", "").replace(" – Recept", "")

    def category(self):
        category = (
            self.url.split("rutgerbakt.nl/")[-1]
            .split("/")[0]
            .replace("-recepten", "")
            .replace("-", " ")
        )
        return category

    def yields(self):
        # The yields are all over the place. There is no way to parse this.
        return None

    def instructions(self):
        # Find the "instructions" heading. It is not really clear when that is.
        # So several steps need to be taken.

        # 1. Filter all the headings.
        # Some h2 headers contain photos. Those are not what we want.
        def filter_heading(headings_old):
            headings_new = []
            for _heading in headings_old:
                if "class" in _heading.attrs:
                    h_class = _heading.attrs["class"]
                    if any("photo" in attr.lower() for attr in h_class):
                        continue
                headings_new.append(_heading)
            return headings_new

        headings = filter_heading(self.soup.find_all("h2"))

        # 2. Find the instructions heading
        # Usually the last heading are the instructions
        # (therefore headings.reverse()).
        # But it's double checked whether the heading contains any of
        # the keywords.
        # I split the heading into words so I keep word boundaries in check.
        headings.reverse()
        for heading in headings:
            tokens = heading.getText().lower().split(" ")
            keywords = ["recept", "bereiding", "maken", "maak"]
            if any(keyword in tokens for keyword in keywords):
                break

        # This function iterates over every next element after the heading.
        def parse_instructions(element):
            for instruction in element.next_siblings:
                if instruction.name not in ["p", "h2", "h3", "h4"]:
                    continue
                if any(
                    item in instruction.text.lower()
                    for item in ["foto: ", "foto's: ", "foto’s: "]
                ):
                    continue
                yield instruction.text.replace("\n", " ").strip()

        instructions = parse_instructions(heading)
        return "\n".join(instructions)

    def description(self):
        # Assuming the first paragraph is the description.
        return self.soup.find("p").text.replace("\n", " ")
