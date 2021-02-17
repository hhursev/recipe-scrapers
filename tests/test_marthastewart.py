from recipe_scrapers.marthastewart import MarthaStewart
from tests import ScraperTest


class TestMarthaStewart(ScraperTest):

    scraper_class = MarthaStewart

    maxDiff = None

    def test_host(self):
        self.assertEqual("marthastewart.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.marthastewart.com/336792/breaded-chicken-breasts",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Breaded Chicken Breasts")

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fassets.marthastewart.com%2Fstyles%2Fwmax-750%2Fd31%2Fbreaded-chicken-cutlets-d104370%2Fbreaded-chicken-cutlets-d104370_horiz.jpg%3Fitok%3DdnK5TccB",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertSetEqual(
            set(
                [
                    "3 large eggs",
                    "Coarse salt",
                    "1/3 cup all-purpose flour",
                    "3 1/2 cups fresh breadcrumbs",
                    "1 cup vegetable oil",
                    "8 thin chicken cutlets (about 1 1/2 pounds total)",
                    "Lemon wedges, for serving (optional)",
                ]
            ),
            set(self.harvester_class.ingredients()),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "In a shallow dish, whisk eggs with teaspoon salt; let stand 5 minutes. In another shallow dish, season flour with 1/4 teaspoon salt. In a third shallow dish, season breadcrumbs with 1 teaspoon salt.",
                    "In a large cast-iron skillet or other heavy deep skillet, heat oil over medium. Meanwhile, pat chicken dry with paper towels. Coat in flour, shaking off excess, then dip in egg (letting excess drip off). Dredge in breadcrumbs, turning twice and patting to adhere.",
                    "Increase heat to medium-high. Working in batches, add chicken to skillet; cook, gently shaking skillet occasionally, until chicken is browned, about 4 minutes. Turn with tongs; cook until browned and opaque throughout, 2 to 3 minutes more (if browning too quickly, lower heat). Between batches, skim off brown crumbs from oil with a slotted spoon. Drain chicken on paper towels; season with salt.",
                ]
            ),
            self.harvester_class.instructions(),
        )
