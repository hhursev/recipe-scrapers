from recipe_scrapers.simplywhisked import SimplyWhisked
from tests import ScraperTest


class TestSimplyWhiskedScraper(ScraperTest):

    scraper_class = SimplyWhisked

    def test_host(self):
        self.assertEqual("simplywhisked.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.simplywhisked.com/buffalo-chicken-chili/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Buffalo Chicken Chili")

    def test_total_time(self):
        self.assertEqual(45, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("8 servings", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "2 tablespoons olive oil",
                "1 small onion, chopped (about 1 cup)",
                "2 stalks celery, chopped",
                "6 garlic cloves, minced",
                "1 1/2 – 2 pounds ground chicken",
                "1 cup water (or reduced-sodium broth)",
                "1 15-ounce can petite diced tomatoes",
                "2 15-ounce cans chili beans, with sauce",
                "2 tablespoos chili powder",
                "2 teaspoons ground cumin",
                "2 teaspoons paprika",
                "1 bay leaf",
                "1 teaspoon salt",
                "1/2 teaspoon pepper",
                "1/2 cup buffalo wing sauce",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "In a large stockpot or dutch oven *affiliate link, heat olive oil to medium-high. Add the bell pepper, onion, celery and garlic. Sauté until onions are translucent, about 5 minutes.\nAdd ground chicken. Breaking up the meat as chicken browns, cook until no longer pink, about 5 minutes.\nAdd water, tomatoes, beans, chili powder, cumin, bay leaf, buffalo sauce, and salt & pepper. Bring to a simmer.\nCover and allow chili to cook for at least 15 minutes, simmering to desired thickness.\nBefore serving, remove bay leaf and adjust seasoning with salt & pepper, to taste.",
            self.harvester_class.instructions(),
        )

    def test_image(self):
        return self.assertEqual(
            "https://www.simplywhisked.com/wp-content/uploads/2016/02/Buffalo-Chicken-Chili-4-1-225x225.jpg",
            self.harvester_class.image(),
        )
