from recipe_scrapers.fitmencook import FitMenCook
from tests import ScraperTest

# test recipe's URL
# https://fitmencook.com/healthy-chili-recipe/


class TestFitMenCookScraper(ScraperTest):

    scraper_class = FitMenCook

    def test_host(self):
        self.assertEqual("fitmencook.com", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://fitmencook.com/healthy-chili-recipe/",
            self.harvester_class.canonical_url(),
        )

    def test_title(self):
        self.assertEqual("Lean Chili with Plantains", self.harvester_class.title())

    def test_total_time(self):
        self.assertEqual(35, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("5 serving(s)", self.harvester_class.yields())

    def test_ingredients(self):
        self.assertEqual(
            [
                "1 tablespoon avocado oil (or olive oil)",
                "1 tablespoon garlic, minced",
                "2/3 cup onion, diced",
                "1 bell pepper, diced",
                "1 1/2 lb 95% lean beef (I used lean bison)",
                "Seasonings 1 tablespoon chili powder 2 teaspoons smoked paprika 2 teaspoons "
                "cumin 1/2 teaspoon cinnamon 2 teaspoons (Mexican) oregano",
                "1 tablespoon chili powder",
                "2 teaspoons smoked paprika",
                "2 teaspoons cumin",
                "1/2 teaspoon cinnamon",
                "2 teaspoons (Mexican) oregano",
                "2 cups low sodium beef stock",
                "4 tablespoons tomato paste (NOT sauce)",
                "1 can (14.5oz /411g) no salt added diced tomatoes",
                "1 ripe plantain (~200g), cut into 1-inch pieces",
                "sea salt & pepper to taste",
                "Garnish cilantro jalapeño",
                "cilantro",
                "jalapeño",
                "1 cucharada de aceite de aguacate (o aceite de oliva)",
                "1 cucharada de ajo picado",
                "2/3 taza de cebolla, cortada en cubitos",
                "1 pimentón, cortado en cubitos",
                "1 1/2 lb 95% de carne magra (utilicé bisonte magro)",
                "Condimentos 1 cucharada de chile en polvo 2 cucharaditas de pimentón ahumado "
                "2 cucharaditas de comino 1/2 cucharadita de canela 2 cucharaditas de orégano "
                "(mexicano) 2 tazas de caldo de res bajo en sodio 4 cucharadas de pasta de "
                "tomate (NO salsa) 1 lata (13.5 oz) de tomates cortados en cubitos",
                "1 cucharada de chile en polvo",
                "2 cucharaditas de pimentón ahumado",
                "2 cucharaditas de comino",
                "1/2 cucharadita de canela",
                "2 cucharaditas de orégano (mexicano)",
                "2 tazas de caldo de res bajo en sodio",
                "4 cucharadas de pasta de tomate (NO salsa)",
                "1 lata (13.5 oz) de tomates cortados en cubitos",
                "1 plátano maduro grande, cortado en trozos de 1 pulgada",
                "sal marina y pimienta al gusto",
                "Adornos cilantro jalapeño",
                "cilantro",
                "jalapeño",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Set a pot on medium heat. Once hot, add the oil, garlic, onion and bell pepper. Cook for 2 – 3 minutes until the onion is browned along the edges.\nAdd the beef and chop it up finely as it cooks in the pot for 3 – 5 minutes. Sprinkle in the seasoning as the meat cooks.\nAdd the remaining ingredients EXCEPT plantain and stir everything together and bring to a light simmer. Cover and cook for 10 minutes.\nAdd the plantain after 10 minutes and stir everything together. ONLY if needed, add tablespoons of beef stock (or water) to the chili if it’s too thick, but also monitor the heat and make sure it’s not too high. Cover and cook for an additional 10 minutes.\nSeason to taste with sea salt & pepper (and lime) and garnish with cilantro and jalapeño.\nPon una olla a fuego medio. Una vez este caliente, agregue el aceite, el ajo, la cebolla y el pimentón. Cocine durante 2 a 3 minutos hasta que la cebolla se dore por los bordes.\nAgregue la carne y córtela finamente mientras se cocina en la olla durante 3 a 5 minutos. Espolvorea el condimento mientras la carne se cocina.\nAgregue los ingredientes restantes EXCEPTO el plátano y revuelva todo junto y cocine a fuego lento. Cubra y cocine por 10 minutos.\nAgregue el plátano después de 10 minutos y revuelva todo junto. SÓLO si es necesario, agregue cucharadas de caldo de carne (o agua) al chile si es demasiado espeso, pero también controle el calor y asegúrese de que no sea demasiado alto. Cubra y cocine por 10 minutos adicionales.\nSazone al gusto con sal marina y pimienta (y lima) y adorne con cilantro y jalapeño.",
            self.harvester_class.instructions(),
        )
