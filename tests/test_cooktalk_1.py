# mypy: allow-untyped-defs

from recipe_scrapers.cooktalk import CookTalk
from tests import ScraperTest


class TestCookTalkScraper(ScraperTest):
    scraper_class = CookTalk
    test_file_name = "cooktalk_1"

    def test_host(self):
        self.assertEqual("cook-talk.com", self.harvester_class.host())

    def canonical_url(self):
        self.assertEqual("https://cook-talk.com/?p=3163", self.harvester_class.host())

    def test_author(self):
        self.assertEqual("Лариса Ивановна", self.harvester_class.author())

    def test_title(self):
        self.assertEqual("Курица с сыром пармезан", self.harvester_class.title())

    def test_category(self):
        self.assertEqual("Птица", self.harvester_class.category())

    def test_image(self):
        self.assertEqual(
            "https://cook-talk.com/archive/wp-content/uploads/2016/03/1-70.jpg",
            self.harvester_class.image(),
        )

    def test_ingredients(self):
        ingredients = [
            "куриное филе без кожи - 4 шт.",
            "молотые белые сухари - 25г",
            "сыр пармезан - 75 г",
            "зелёный лук - 2 стебля с листьями",
            "лимон - 1 шт (цедра и сок)",
            "сливочное масло - 50г",
            "петрушка - 2 ст л. мелко нарезанной",
            "соль, черный перец - по вкусу",
        ]
        self.assertEqual(ingredients, self.harvester_class.ingredients())

    def test_instructions(self):
        instructions = (
            "Разогреть духовку до 190 градусов С.\n"
            "Смешать сухари, растопленное масло, сыр и цедру лимона, натёртые на мелкой тёрке, измельчённый зеленый лук, соль и перец. Обмазать куриное филе этой смесью.\n"
            "Выложить в низкую огнеупорную форму и поместить в духовку на 20 минут.\n"
            "Вынуть филе из формы, выложить на тарелки. Добавить к жидкости, оставшейся в форме, лимонный сок и измельченную петрушку, перемешать, полить полученной подливкой куриное филе и подать немедленно."
        )
        self.assertEqual(instructions, self.harvester_class.instructions())

    def test_description(self):
        self.assertEqual(
            "Куриная грудка по этому рецепту получается очень сочной (!) и вполне нарядной.",
            self.harvester_class.description(),
        )

    def test_language(self):
        self.assertEqual("ru-RU", self.harvester_class.language())
