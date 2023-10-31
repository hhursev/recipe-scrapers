# mypy: allow-untyped-defs

from recipe_scrapers.briceletbaklava import BricelEtBaklava
from tests import ScraperTest


class TestBricelEtBaklavaScraper(ScraperTest):
    scraper_class = BricelEtBaklava

    def test_host(self):
        self.assertEqual("briceletbaklava.ch", self.harvester_class.host())

    def test_canonical_url(self):
        self.assertEqual(
            "https://briceletbaklava.ch/2021/08/burli-de-saint-gall-st.galler-burli.html",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Michel/Bricelet & Baklava", self.harvester_class.author())

    def test_title(self):
        self.assertEqual(
            "Bürli de Saint-Gall (St. Galler Bürli)", self.harvester_class.title()
        )

    def test_category(self):
        self.assertEqual(
            "Boulangerie\nRecettes de pains", self.harvester_class.category()
        )

    def test_yields(self):
        self.assertEqual(
            "Recette pour 4 pains doubles 8 pièces de 140 g",
            self.harvester_class.yields(),
        )

    def test_image(self):
        self.assertEqual(
            "https://image.over-blog.com/D913ECH_mmWHTy8_qRECetDo6PU=/filters:no_upscale()/image%2F3215825%2F20210816%2Fob_e19375_pain-buerli-6374.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "150 g de farine bise (type 1100) *",
                "150 g d'eau légèrement tiède",
                "10 g de levain chef actif ou 1 g de levure fraîche",
                "300 g du levain de la veille",
                "470 g de farine mi-blanche (type 720) *",
                "325 g (+ ou – 1 cl) d’eau froide",
                "6 g de levure fraîche",
                "14 g de sel",
                "ICI",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        self.assertEqual(
            "Mettre le levain chef dans un bol,\nVerser l’eau tiédie (25°C) par dessus et à l’aide d’un fouet, bien mélanger l’ensemble.\nAjouter la farine\net mélanger pour en faire une pâte un peu collante.\nCouvrir et laisser le levain commencer sa fermentation pendant 3 heures à température ambiante. Déposer ensuite le bol au réfrigérateur (5 à 6°C) pendant au moins 12 heures jusqu’à 24 heures au maximum.\nSortir le levain du réfrigérateur 2 heures avant son emploi afin qu’il se remette en température.\nAjouter par dessus la levure fraîche\net ajouter encore l’eau froide\nafin de le décoller\net verser le tout dans la cuve du pétrin. Ajouter la farine et commencer le pétrissage en vitesse lente, ceci pour 10 bonnes minutes. Après 3 minutes de pétrissage, ajouter le sel. A la fin des 10 minutes, la pâte sera bien collante car très hydratée, c’est normal. Continuer le pétrissage maintenant en 2ème vitesse pendant encore 5 minutes, la pâte doit être très pétrie. Afin de contrôler son élasticité, étirer un morceau de pâte entre les doigts, elle devrait être aussi fine que du papier.\nAvec un peu d’huile, graisser légèrement un grand bol et y déposer la pâte.\nRecouvrir d’un torchon humide ou d’un couvercle et laisser lever entre 3 et 4 heures /selon la saison) à température ambiante. Durant ces 4 heures de pousse, procéder à plusieurs rabats, par exemple toutes les 30 minutes. Il s’agit de rabattre la pâte 3 à 4 fois sur elle-même. Une fois le pointage terminé, la pâte aura bien doublé de volume\nla verser sur le plan de travail fariné et découpez des pâtons de 140 g chacun.\nEnsuite, façonnez délicatement les pâtons en boule sans trop les serrer afin de ne pas les dégazer\nDéposer ces pâtons par deux, l'un à côté de l'autre en se touchant légèrement, sur un torchon bien fariné avec la soudure vers le haut.\nFaire un pli avec le torchon afin que la pâte ne s'étale pas trop et les recouvrir d’un deuxième torchon fariné puis d’un plastique et laisser lever entre 30 et 40 minutes, cette opération se nomme « L’apprêt ». Pendant ce temps, allumer le four sur 240°C en ayant soin d’y déposer une pierre de cuisson ou une plaque métallique retournée. L’apprêt terminé, retourner les pâtons, toujours accolés l’un l’autre et les déposer sur une planchette en bois bien farinée et d’un coup sec, les glisser sur la pierre ou la plaque brûlante, sans oublier de verser au fond du four un verre d’eau avant de fermer la porte. Après 15 minutes de cuisson, entrouvrir rapidement la porte du four afin d’en évacuer la vapeur puis, baisser la température à 220 et poursuivre la cuisson pendant encore 20 minutes. Une fois cuits, les bürli doivent être foncés et croustillant, les sortir et les laisser refroidir sur une grille.",
            self.harvester_class.instructions(),
        )

    def test_description(self):
        self.assertEqual(
            "Le Bürli de Saint-Gall est un petit pain en pâte levée, en forme de ballon. Juste avant l’enfournement ils sont accolés par deux et même quelquefois par 4 avec une cuisson très intense car les saint-gallois les apprécient bien cuits et croustillants. On les associe spontanément à la célèbre saucisse de veau du même canton, car lors de fêtes populaires, à la OLMA notamment, ces deux produits sont indissociables. On tient la saucisse grillée d’une main et le Bürli de l’autre et on les déguste alternativement, sans moutarde. Ces pains sont confectionnés à partir de farine mi-blanche et bise, La pâte est très hydratée ce qui leurs confère une mie très alvéolée et goûteuse. Et juste encore quelques mots sur la saucisse de Saint-Gall. La première mention officielle de celle-ci remonte à 1438. Dans les statuts de la société des bouchers de l’époque, il était indiqué que cette saucisse comprenait une part de viande de veau, une de porc et de lard et une de lait frais. J’y ai travaillé dans ce canton, plus précisément dans le Toggenburg et je peux dire que la recette a très peu changé depuis son origine à part quelques petites variantes, comme le lait frais qui s’est transformé en poudre de lait par exemple. Cette saucisse est vraiment délicieuse et il s’en transforme des tonnes par là-bas et elle a même obtenu le label IGP en 2008. On en mangeait tous les jours, plus précisément lors du « znüni », en français : les « neuf heures ».",
            self.harvester_class.description(),
        )
