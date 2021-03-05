from recipe_scrapers.ambitiouskitchen import AmbitiousKitchen
from tests import ScraperTest


class TestAmbitiousKitchenScraper(ScraperTest):

    scraper_class = AmbitiousKitchen

    def test_host(self):
        self.assertEqual("ambitiouskitchen.com", self.harvester_class.host())

    def test_author(self):
        self.assertEqual(
            "Monique of AmbitiousKitchen.com", self.harvester_class.author()
        )

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.ambitiouskitchen.com/vegetarian-spinach-pumpkin-lasagna/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(), "Vegetarian Spinach Pumpkin Lasagna"
        )

    def test_total_time(self):
        self.assertEqual(70, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("12 serving(s)", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://www.ambitiouskitchen.com/wp-content/uploads/2019/10/Vegetarian-Spinach-Pumpkin-Lasagna-5sq.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "For the noodles:",
                "10 lasagna noodles",
                "For the ricotta mixture:",
                "1/2 tablespoon olive oil",
                "6 ounces spinach (from 1 bag spinach)",
                "1 (15 ounce) container part skim ricotta",
                "1 egg",
                "½ teaspoon garlic powder",
                "1/2 teaspoon salt",
                "Freshly ground black pepper",
                "For the pumpkin layer:",
                "2 (15 ounce) cans pumpkin puree",
                "½ cup milk (I like unsweetened almond milk, but any milk will work)",
                "¼ teaspoon cinnamon",
                "¼ teaspoon nutmeg",
                "¼ teaspoon ginger",
                "¼ teaspoon allspice",
                "3/4 teaspoon salt",
                "Freshly ground black pepper",
                "For the layers:",
                "3 cups shredded mozzarella cheese, divided (approximately 12 ounces)",
                "1 cup grated parmesan cheese, divided",
                "To garnish:",
                "Fresh chopped parsley or small sage leaves",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "Preheat oven to 400 degrees F. Grease a 9x13 inch baking pan with nonstick cooking spray.\nBring a large pot of water to a boil. Cook the lasagna noodles for 5-6 minutes, then drain. Immediately lay the noodles flat on an oiled baking sheet or cutting board so you can easily assemble the lasagna when ready. Another option is to soak the lasagna noodles in very warm (hot) water for 20-30 minutes if you do not want to boil them. (You can also use no cook lasagna noodles, but they aren't my favorite!)\nWhile the lasagna noodles are boiling, cook the spinach: add ½ tablespoon olive oil to a medium pan or skillet and place over medium heat. Add spinach, season with a little salt and pepper and cook until spinach wilts down. Add to a medium bowl and allow to cool for a minute or two.\nIn the small bowl, add the spinach, ricotta, egg, garlic powder, salt and pepper. Set aside.\nNext make the pumpkin mixture: add pumpkin, milk, cinnamon, nutmeg, ginger, allspice, salt and pepper to a large bowl. Mix to combine.\nTo assemble the lasagna, spread 1 heaping cup of pumpkin mixture over the bottom of the baking dish. Place 5 of the cooked lasagna noodles on top laying 4 vertically and 1 horizontally. Spread half of the spinach-ricotta cheese mixture on top of the noodles, then top with ¾ cup shredded mozzarella.\nNext, add 1 heaping cup of the pumpkin mixture on top of the mozzarella and then sprinkle with 1/2 cup of parmesan cheese.\nRepeat layers once more: adding remaining noodles, remaining spinach-ricotta mixture, ¾ cup shredded mozzarella, then top with any remaining pumpkin and ½ cup parmesan cheese. Finally, top with remaining 1 ½ cups shredded mozzarella cheese.\nCover with foil and bake covered for 25 minutes. Remove foil and bake another 15-20 minutes until cheese starts to brown just a bit. Garnish with extra parmesan and either chopped sage or parsley. Cool for 15 minutes before cutting and serving. Serves 12.",
            self.harvester_class.instructions(),
        )

    def test_ratings(self):
        self.assertEqual(5.0, self.harvester_class.ratings())
