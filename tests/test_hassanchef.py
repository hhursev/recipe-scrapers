from recipe_scrapers.hassenchef import Hassanchef
from tests import ScraperTest


class TestClosetCooking(ScraperTest):

    scraper_class = Hassanchef

    def test_host(self):
        self.assertEqual("hassanchef.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://www.hassanchef.com/2019/06/chicken-lollipop-recipe-lollipop-chicken.html",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual(self.harvester_class.title(), "Chicken lollipop recipe")

    def test_total_time(self):
        self.assertEqual(30, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("2 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertCountEqual(
            [
                "For chicken lollipop dry",
                "6-8 pieces of chicken wings.",
                "1/2 teaspoon red chilly sauce.",
                "1/2 teaspoon schezwan sauce.",
                "1/2 teaspoon red chilly paste",
                "1/2 teaspoon chopped garlic",
                "1/2 teaspoon chopped ginger",
                "1 teaspoon chopped celery",
                "1/2 teaspoon green chilly paste",
                "1/2 cup corn flour",
                "1/4 cup Maida",
                "1 egg beaten",
                "1/2 teaspoon salt",
                "1/2 teaspoon white pepper powder",
                "1/2 teaspoon lemon juice",
                "For masala chicken lollipop",
                "1/2 teaspoon red chilly paste",
                "1/3 teaspoon schezwan sauce",
                "1/2 teaspoon chopped garlic",
                "1/2 teaspoon ginger chopped",
                "1/3 cup chopped onions.",
                "Small handful chopped spring onions.",
                "1 teaspoon cooking oil",
                "Salt as per taste",
                "2 teaspoon corn flour slurry",
                "For chicken lollipop gravy",
                "1 cup water",
                "1/3 teaspoon dark soya sauce",
                "1/4 teaspoon red chilly sauce",
                "1/3 teaspoon red chilly paste",
                "1/4 teaspoon tomato soup",
                "1/4 teaspoon schezwan sauce",
                "1/3 teaspoon green chilli paste",
                "1/3 teaspoon white pepper powder",
                "small pinch of sugar",
                "3 teaspoon corn flour slurry",
                "salt as per taste",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        return self.assertEqual(
            "How to make the recipe\nMake lollipop batter\nTake corn flour and all purpose flour in a mixing bowl and mix the chopped ginger, chopped garlic, red chilly paste, red chilly sauce, schezwan sauce, green chilli paste and chopped celery.\nThen add salt, white pepper powder, lemon juice and beaten egg.\nGive everything a fine mix to make a smooth batter. If required add little amount of water.\nMake chicken lollipop dry\nWash and clean the lollipop pieces and pat them dry completely.\nMix these lollipops with the batter evenly so that all parts are covered with the batter\nLet them marinate for 2 to 4 hours or overnight.\nHeat oil in a deep vessel pan or kadai in medium flame.\nBring the marinated lollipops and remove excess marinate from them\nPour then into the oil one by one carefully. Keep the heat flame to low\nFry the lollipops for 7 to 8 minutes in slow flame till crisp golden.\nRemove them in an absorbent paper to absorb any excess oil from them.\nRemove them in an absorbent paper to absorb any excess oil from them.\nGarnish a plate and serve the chicken lollipop dry with schezwan sauce.\nMake masala chicken lollipop\nHeat half teaspoon oil in a wok or deep vessel pan in high flame.\nAdd half teaspoon of ginger and garlic and saute. Then add half of the chopped onions and fry them in high flame\nWhen onions become translucent lower the heat and add red chilly paste and schezwan sauce. Mix and pour little water. Stir everything well.\nNow add the fried chicken lollipops and mix well. Add 1/3 teaspoon white pepper powder and salt as per taste\nThen pour corn flour slurry into the above mixture and continue to stir.\nWhen the mixture become little dry and the masala coated the lollipops evenly switch off the flame and remove them in a serving plate. Garnish with chopped spring onions and serve\nMake chicken lollipop gravy\nHeat 1/2 teaspoon oil in a wok in high flame and add the chopped ginger, garlic and onion. Fry them till onions become translucent in high flame.\nLower the flame and add 1/3 teaspoon red chilly paste, 1/4 teaspoon red chilly sauce, 1/4 teaspoon tomato ketchup and schezwan sauce. Mix everything\nAdd 1 cup water into the above mixture and simmer for a while.\nThen add salt as per taste, 1/4 teaspoon white pepper powder, 1/3 teaspoon green chili paste and a small pinch of sugar.\nFurther add 1/3 teaspoon dark soya sauce into the mixture.\nNow pour the corn flour slurry, mix and summer for one minute. The gravy will start to become thick and glossy.\nAdd the fried chicken lollipops and further simmer for a minute. Sprinkle chipped spring onions into the gravy\nCheck the seasoning and thickness of the gravy and remove to serve with fried rice and noodles.",
            self.harvester_class.instructions(),
        )
