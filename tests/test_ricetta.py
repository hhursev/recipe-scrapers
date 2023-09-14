# mypy: allow-untyped-defs

from recipe_scrapers.ricetta import Ricetta
from tests import ScraperTest


class TestRicettaScraper(ScraperTest):

    scraper_class = Ricetta

    def test_host(self):
        self.assertEqual("ricetta.it", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Luca Gatti", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Lasagne al radicchio e formaggio", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual("Lasagne", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(60, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("4 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://ricetta.it/Uploads/Imgs/lasagne-al-radicchio-e-formaggio_medium.jpg.webp",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "250 g di sfoglie di pasta fresca per lasagne",
                "300 g di radicchio",
                "200/250 g di Fontina",
                "q.b. parmigiano grattugiato",
                "q.b. sale",
                "q.b. olio extra vergine d'oliva",
                "80 g di burro",
                "80 g di farina",
                "1 l di latte",
                "q.b. noce moscata",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        expected_instructions = "\n".join(
            [
                "Per prima cosa procediamo a pulire il radicchio e a tagliarlo in due nel verso della lunghezza, e poi a listarelle. Mettiamolo in una pentola capiente con un filo d'olio extra vergine d’oliva e lasciamo stufare a fiamma dolce per dieci minuti circa [1].",
                "Saliamo e mescoliamo di tanto in tanto. Per preparare la besciamella invece mettiamo il latte a bollire e in un altro pentolino facciamo sciogliere il burro [2].",
                "Quando è del tutto fuso, uniamo la farina [3] e facciamo addensare mescolando per un paio di minuti.",
                "Dopodiché trasferiamo questo composto nel latte giunto ad ebollizione [4].",
                "Insaporiamo con noce moscata [5] e un pizzico di sale, mescoliamo il tutto e togliamo dal fuoco.",
                "Teniamone 3-4 mestolini da parte, quindi uniamo il resto al radicchio stufato [6].",
                "Infine tagliamo a cubetti la fontina. Possiamo ora comporre le nostre lasagne: prendiamo una pirofila (noi ne abbiamo utilizzata una di 15x25 cm), distribuiamo un po' di besciamella e radicchio sul fondo, poi stendiamo le sfoglie di pasta fresca senza cuocerla in precedenza [7].",
                "Aggiungiamo poi altra besciamella al radicchio, sopra un po' di fontina [8] e una spolverata di parmigiano grattugiato [9].",
                "Ricopriamo con altre sfoglie di pasta e ripetiamo gli strati fino ad esaurimento degli ingredienti [10].",
                "Completiamo distribuendo la besciamella bianca, tenuta da parte inizialmente e abbondante parmigiano grattugiato [11], che in cottura creerà una crosticina croccante.",
                "Versiamo un filo d'olio extra vergine d'oliva e mettiamo a cuocere in forno ventilato preriscaldato a 200° per 20-25 minuti [12].",
                "Come accennato in precedenza, il formaggio dovrà aver formato una bella crosticina, se però così non fosse, possiamo accendere la funzione grill del nostro forno e terminare la cottura per qualche minuto prestando però particolare attenzione che le lasagne non brucino. Una volta cotte, attendiamo giusto un paio di minuti per tagliarle, poi serviamole molto calde, così da valorizzare l’effetto fondente del formaggio.",
            ]
        )
        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.6, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual("Italiana", self.harvester_class.cuisine())

    def test_description(self):
        expected_description = "Le lasagne al radicchio e formaggio sono un primo piatto invernale molto gustoso, adatto anche a chi segue una dieta vegetariana. Prepariamole insieme."
        self.assertEqual(expected_description, self.harvester_class.description())

    def test_language(self):
        self.assertEqual("it", self.harvester_class.language())
