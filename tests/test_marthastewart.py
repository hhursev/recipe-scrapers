from recipe_scrapers.marthastewart import MarthaStewart
from tests import ScraperTest


class TestMarthaStewart(ScraperTest):
    scraper_class = MarthaStewart

    def test_host(self):
        self.assertEqual("marthastewart.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.marthastewart.com/336792/breaded-chicken-breasts",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Breaded Chicken Breasts")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Martha Stewart Test Kitchen")

    def test_total_time(self):
        self.assertEqual(25, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.marthastewart.com/thmb/nvxNpKLIet99N9F5m3dHhHu0g_4=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/336792_breaded-chicken-breasts-12-877d76b08e44450fa77c20a0e449a741.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "3 large eggs",
                "Coarse salt",
                "0.333 cup all-purpose flour",
                "3.5 cups fresh breadcrumbs",
                "1 cup vegetable oil",
                "8 thin chicken cutlets (about 1 ½ pounds total)",
                "Lemon wedges, for serving (optional)",
            ],
            (self.harvester_class.ingredients()),
        )

    def test_instructions(self):
        return self.assertEqual(
            "\n".join(
                [
                    "Whisk eggs and set out breading: In a shallow dish, whisk eggs with teaspoon salt; let stand 5 minutes. In another shallow dish, season flour with 1/4 teaspoon salt. In a third shallow dish, season breadcrumbs with 1 teaspoon salt.",
                    "Prep chicken cutlets: In a large cast-iron skillet or other heavy deep skillet, heat oil over medium. Meanwhile, pat chicken dry with paper towels. Coat in flour, shaking off excess. Then dip in egg (letting excess drip off). Dredge in breadcrumbs, turning twice and patting to adhere.",
                    "Cook chicken cutlets: Increase heat to medium-high. Working in batches, add chicken to skillet; cook, gently shaking skillet occasionally, until chicken is browned, about 4 minutes. Turn with tongs; cook until browned and opaque throughout, 2 to 3 minutes more (if browning too quickly, lower heat). Between batches, skim off brown crumbs from oil with a slotted spoon. Drain chicken on paper towels; season with salt.",
                ]
            ),
            self.harvester_class.instructions(),
        )
