from recipe_scrapers.twopeasandtheirpod import TwoPeasAndTheirPod
from tests import ScraperTest


class TestTwoPeasAndTheirPodScraper(ScraperTest):

    scraper_class = TwoPeasAndTheirPod
    test_file_name = "twopeasandtheirpod_2"

    def test_host(self):
        self.assertEqual("twopeasandtheirpod.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.twopeasandtheirpod.com/mango-salad/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Mango Salad")

    def test_author(self):
        self.assertEqual(self.harvester_class.author(), "Maria Lichty")

    def test_total_time(self):
        self.assertEqual(10, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "2 ripe mangos, (chopped)",
                "2 cups peeled and chopped jicama",
                "2 cups chopped English cucumber",
                "1 red bell pepper, (seeds removed and chopped)",
                "2 scallions, (sliced)",
                "2 tablespoons chopped cilantro leaves",
                "2 tablespoons chopped fresh mint leaves",
                "2 small limes",
                "Kosher salt, (to taste)",
                "Tajin, (for sprinkling on salad, optional)",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a large bowl, combine the mango, jicama, cucumber, red pepper, scallions, cilantro, and mint.\nSqueeze fresh lime juice over the salad and toss. Sprinkle with salt and Tajin, if using. Toss again.\nServe and enjoy!",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        return self.assertEqual(
            "https://www.twopeasandtheirpod.com/wp-content/uploads/2023/07/Mango-Salad-0715.jpg",
            self.harvester_class.image(),
        )
