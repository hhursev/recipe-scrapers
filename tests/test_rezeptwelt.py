import unittest

from recipe_scrapers.rezeptwelt import Rezeptwelt
from tests import ScraperTest


class TestRezeptweltScraper(ScraperTest):
    scraper_class = Rezeptwelt

    def test_host(self):
        self.assertEqual("rezeptwelt.de", self.harvester_class.host())

    @unittest.skip("canonical_url is not available from this webpage")
    def test_canonical_url(self):
        self.assertEqual(
            "https://www.rezeptwelt.de/vorspeisensalate-rezepte/italienischer-nudelsalat/wbtt7xp3-9544c-831497-cfcd2-6bis4hp6",
            self.harvester_class.canonical_url(),
        )

    def test_author(self):
        self.assertEqual("Kräuterwiese", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Italienischer Nudelsalat", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Vorspeisen/Salate", self.harvester_class.category())

    def test_total_time(self):
        self.assertEqual(50, self.harvester_class.total_time())

    def test_yields(self):
        self.assertEqual("6 servings", self.harvester_class.yields())

    def test_image(self):
        self.assertEqual(
            "https://de.rc-cdn.community.thermomix.com/recipeimage/wbtt7xp3-9544c-831497-cfcd2-6bis4hp6/d60b5483-c12d-4c2a-871d-05748e5aa06c/main/italienischer-nudelsalat.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        self.assertEqual(
            [
                "250 g Nudeln z.B. Fusilli,Penne",
                "1000 g Wasser",
                "1 EL Gemüsebrühe",
                "100 g Tomaten getrocknet, ohne Öl",
                "500 g Kirschtomaten halbiert",
                "1 Kugel Mozarella, halbiert",
                "8 Stück schwarze Oliven, entsteint",
                "100 g Rucola/Rauke",
                "2 Zehen Knoblauch",
                "1 Bund Basilkum (ohne Stiele)",
                "45 g Weißweinessig",
                "40 g Olivenöl",
                "1 TL Salz",
                "2 Prisen Pfeffer",
            ],
            self.harvester_class.ingredients(),
        )

    def test_instructions(self):
        raw_instructions = [
            "Salat",
            "1. Wasser und Gemüsebrühe in den Mixtopf geben und 8Min./100°/Stufe 1 aufkochen",
            '2. Nudeln zugeben, je nach Packungsanweisung ca. 8-10Min./100°/"Linkslauf" /Stufe "Sanftrührstufe" garen, Nudeln in den Gareinsatz abgießen und Garflüssigkeit dabei auffangen. Nudeln in eine große Schüssel umfüllen und etwas abkühlen lassen.',
            '3. getrocknete Tomaten in den Mixtopf geben, 5Sek./"Linkslauf deaktiviert" /Stufe 4 zerkleinern und zu den Nudeln geben.',
            "4.Mozarella in den Mixtopf geben, 2 Sek./Stufe 4 zerkleinern und zu den Nudeln geben.",
            "5. Alle weiteren Salatzutaten (Rucola, schwarze Oliven und Kirschtomaten) in die große Schüssel zugeben und vermischen",
            "Dressing:",
            "6. Knoblauch und Basilikum in den Mixtopf geben 4 Sek./Stufe 7 zerkleinern.",
            "7. Übrige Zutaten und 120 g Garflüssigkeit zugeben und 15Sek./Stufe 3-4 verrühren, zum Salat geben und vermischen.",
        ]

        expected_instructions = "\n".join(raw_instructions)

        self.assertEqual(expected_instructions, self.harvester_class.instructions())

    def test_ratings(self):
        self.assertEqual(4.68, self.harvester_class.ratings())

    def test_cuisine(self):
        self.assertEqual(
            None, self.harvester_class.cuisine()
        )  # other recipes contain cuisine information

    def test_description(self):
        self.assertEqual(
            "Italienischer Nudelsalat, ein Rezept der Kategorie Vorspeisen/Salate.",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("de_DE", self.harvester_class.language())
