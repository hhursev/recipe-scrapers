import os
import unittest

from recipe_scrapers.bbcfood import BBCFood


class TestBBCFoodScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'test_data',
            'bbc_food.testhtml'
        )) as file_opened:
            self.harvester_class = BBCFood(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            'bbc.com',
            self.harvester_class.host()
        )

    def test_host_domain(self):
        self.assertEqual(
            'bbc.co.uk',
            self.harvester_class.host(domain='co.uk')
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            'Irish cream and chocolate cheesecake'
        )

    def test_total_time(self):
        self.assertEqual(
            130,
            self.harvester_class.total_time()
        )

    def test_yields(self):
        self.assertEqual(
            "1 item(s)",
            self.harvester_class.yields()
        )

    def test_image(self):
        self.assertEqual(
            'https://ichef.bbci.co.uk/food/ic/food_16x9_608/recipes/baileysandchocolatec_72293_16x9.jpg',
            self.harvester_class.image()
        )

    def test_ingredients(self):
        self.assertCountEqual(
            [
                '100g/3½oz butter',
                '250g/8¾oz digestive biscuits, crushed',
                '600g/1lb 5oz cream cheese',
                '25ml/1fl oz Baileys or other Irish cream liqueur',
                '100ml/3½oz icing sugar',
                '300ml/10½oz double cream, whipped',
                '100g/3½oz grated chocolate',
                '200ml/7¼oz double cream, whipped',
                'cocoa powder, to dust'
            ],
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            'Melt the butter in a pan and add the crushed digestive biscuits. Mix well until the biscuits have absorbed all the butter.\nRemove from the heat and press into the bottom of a lined 18cm/7in springform tin. Place in the refrigerator and allow to set for one hour.\nMeanwhile, prepare the filling. Lightly whip the cream cheese then beat in the Irish cream and icing sugar. Fold in the whipped cream and grated chocolate. When smooth, spoon evenly onto the biscuits.\nRefrigerate and allow to set for a further two hours. Once set, remove and decorate with whipped cream and cocoa powder dusted over the top. Serve.',
            self.harvester_class.instructions()
        )

    def test_dict_gen(self):
        self.assertEqual(
            {'host': 'bbc.com',
             'image': 'https://ichef.bbci.co.uk/food/ic/food_16x9_608/recipes/baileysandchocolatec_72293_16x9.jpg',
             'ingredients': ['100g/3Â½oz butter',
                             '250g/8Â¾oz digestive biscuits, crushed',
                             '600g/1lb 5oz cream cheese',
                             '25ml/1fl oz Baileys or other Irish cream liqueur',
                             '100ml/3Â½oz icing sugar',
                             '300ml/10Â½oz double cream, whipped',
                             '100g/3Â½oz grated chocolate',
                             '200ml/7Â¼oz double cream, whipped',
                             'cocoa powder, to dust'],
             'instructions': 'Melt the butter in a pan and add the crushed digestive '
                             'biscuits. Mix well until the biscuits have absorbed all the '
                             'butter.\n'
                             'Remove from the heat and press into the bottom of a lined '
                             '18cm/7in springform tin. Place in the refrigerator and allow '
                             'to set for one hour.\n'
                             'Meanwhile, prepare the filling. Lightly whip the cream '
                             'cheese then beat in the Irish cream and icing sugar. Fold in '
                             'the whipped cream and grated chocolate. When smooth, spoon '
                             'evenly onto the biscuits.\n'
                             'Refrigerate and allow to set for a further two hours. Once '
                             'set, remove and decorate with whipped cream and cocoa powder '
                             'dusted over the top. Serve.',
             'links': [{'href': 'https://www.bbc.co.uk'},
                       {'href': '#orb-modules'},
                       {'href': '/accessibility/', 'id': 'orb-accessibility-help'},
                       {'href': 'https://account.bbc.com/account', 'id': 'idcta-link'},
                       {'href': 'https://www.bbc.co.uk'},
                       {'href': 'http://www.bbc.co.uk/news'},
                       {'href': 'http://www.bbc.co.uk/sport'},
                       {'href': 'http://www.bbc.co.uk/weather'},
                       {'href': 'http://www.bbc.co.uk/iplayer'},
                       {'href': 'http://www.bbc.co.uk/tv'},
                       {'href': 'http://www.bbc.co.uk/radio'},
                       {'href': 'http://www.bbc.co.uk/cbbc'},
                       {'href': 'http://www.bbc.co.uk/cbeebies'},
                       {'href': 'http://www.bbc.co.uk/food'},
                       {'href': 'http://www.bbc.co.uk/education'},
                       {'href': 'http://www.bbc.co.uk/music'},
                       {'href': 'http://www.bbc.com/earth'},
                       {'href': 'http://www.bbc.co.uk/arts'},
                       {'href': 'http://www.bbc.co.uk/makeitdigital'},
                       {'href': 'http://www.bbc.co.uk/taster'},
                       {'href': 'http://www.bbc.co.uk/local'},
                       {'href': 'http://www.bbc.co.uk/tomorrowsworld'},
                       {'class': ['istats-notrack'],
                        'data-alt': 'More',
                        'href': '#orb-footer'},
                       {'class': ['orb-search__button'],
                        'href': 'https://search.bbc.co.uk/search',
                        'title': 'Search the BBC'},
                       {'class': ['page-title__logo'],
                        'href': '/food/',
                        'title': 'Food homepage'},
                       {'class': ['main-menu__link'], 'href': '/food/'},
                       {'class': ['main-menu__link'], 'href': '/food/recipes'},
                       {'class': ['main-menu__secondary-link'], 'href': '/food/seasons'},
                       {'class': ['main-menu__secondary-link'], 'href': '/food/occasions'},
                       {'class': ['main-menu__secondary-link'], 'href': '/food/cuisines'},
                       {'class': ['main-menu__secondary-link'], 'href': '/food/dishes'},
                       {'class': ['main-menu__link'], 'href': '/food/chefs'},
                       {'class': ['main-menu__link'], 'href': '/food/programmes'},
                       {'class': ['main-menu__link'], 'href': '/food/ingredients'},
                       {'class': ['main-menu__link'], 'href': '/food/techniques'},
                       {'class': ['main-menu__link'], 'href': '/food/about'},
                       {'class': ['main-menu__link'], 'href': '/food/my/favourites'},
                       {'class': ['recipe-search-quick-link__link'],
                        'href': '#recipe-finder__box'},
                       {'class': ['recipe-metadata__dietary-vegetarian'],
                        'href': '/food/diets/vegetarian'},
                       {'class': ['chef__link'],
                        'href': '/food/chefs/rob_burns',
                        'itemprop': 'author'},
                       {'class': ['recipe-actions-link'],
                        'href': '/food/recipes/baileysandchocolatec_72293/share',
                        'id': 'send-to-mobile-link'},
                       {'class': ['recipe-actions-link'],
                        'href': '/food/recipes/baileysandchocolatec_72293/shopping-list',
                        'id': 'shopping-list-link'},
                       {'class': ['recipe-actions-link'],
                        'href': 'javascript:window.print()',
                        'id': 'print-link'},
                       {'class': ['recipe-ingredients__link'], 'href': '/food/butter'},
                       {'class': ['recipe-ingredients__link'],
                        'href': '/food/digestive_biscuit'},
                       {'class': ['recipe-ingredients__link'],
                        'href': '/food/cream_cheese'},
                       {'class': ['recipe-ingredients__link'], 'href': '/food/liqueur'},
                       {'class': ['recipe-ingredients__link'], 'href': '/food/icing_sugar'},
                       {'class': ['recipe-ingredients__link'],
                        'href': '/food/double_cream'},
                       {'class': ['recipe-ingredients__link'], 'href': '/food/chocolate'},
                       {'class': ['recipe-ingredients__link'],
                        'href': '/food/double_cream'},
                       {'class': ['recipe-ingredients__link'], 'href': '/food/cocoa'},
                       {'class': ['promo'],
                        'href': 'https://www.bbc.co.uk/food/occasions/halloween'},
                       {'class': ['related-recipes__image-link'],
                        'href': '/food/recipes/marys_victoria_sandwich_58140'},
                       {'class': ['related-recipes__title-link'],
                        'href': '/food/recipes/marys_victoria_sandwich_58140'},
                       {'class': ['related-recipes__more-link'],
                        'href': '/food/collections/decadent_desserts'},
                       {'class': ['related-recipes__image-link'],
                        'href': '/food/recipes/courgette_and_caraway_84359'},
                       {'class': ['related-recipes__title-link'],
                        'href': '/food/recipes/courgette_and_caraway_84359'},
                       {'class': ['related-recipes__more-link'],
                        'href': '/food/cream_cheese'},
                       {'class': ['related-recipes__image-link'],
                        'href': '/food/recipes/eton_mess_cheesecake_58338'},
                       {'class': ['related-recipes__title-link'],
                        'href': '/food/recipes/eton_mess_cheesecake_58338'},
                       {'class': ['related-recipes__more-link'],
                        'href': '/food/cheesecake'},
                       {'class': ['social-promo-twitter-link'],
                        'href': 'http://www.twitter.com/BBCFood'},
                       {'class': ['social-promo-facebook-link'],
                        'href': 'http://www.facebook.com/bbcfood'},
                       {'class': ['social-promo-pinterest-link'],
                        'href': 'http://www.pinterest.com/bbcfood'},
                       {'href': 'https://www.bbc.co.uk'},
                       {'href': 'http://www.bbc.co.uk/news'},
                       {'href': 'http://www.bbc.co.uk/sport'},
                       {'href': 'http://www.bbc.co.uk/weather'},
                       {'href': 'http://www.bbc.co.uk/iplayer'},
                       {'href': 'http://www.bbc.co.uk/tv'},
                       {'href': 'http://www.bbc.co.uk/radio'},
                       {'href': 'http://www.bbc.co.uk/cbbc'},
                       {'href': 'http://www.bbc.co.uk/cbeebies'},
                       {'href': 'http://www.bbc.co.uk/food'},
                       {'href': 'http://www.bbc.co.uk/education'},
                       {'href': 'http://www.bbc.co.uk/music'},
                       {'href': 'http://www.bbc.com/earth'},
                       {'href': 'http://www.bbc.co.uk/arts'},
                       {'href': 'http://www.bbc.co.uk/makeitdigital'},
                       {'href': 'http://www.bbc.co.uk/taster'},
                       {'href': 'http://www.bbc.co.uk/local'},
                       {'href': 'http://www.bbc.co.uk/tomorrowsworld'},
                       {'href': 'http://www.bbc.co.uk/usingthebbc/terms/'},
                       {'href': 'http://www.bbc.co.uk/aboutthebbc'},
                       {'href': 'http://www.bbc.co.uk/usingthebbc/privacy/'},
                       {'href': 'http://www.bbc.co.uk/usingthebbc/cookies/'},
                       {'href': 'http://www.bbc.co.uk/accessibility/'},
                       {'href': 'http://www.bbc.co.uk/guidance'},
                       {'href': 'http://www.bbc.co.uk/contact'},
                       {'href': 'http://www.bbc.co.uk/bbcnewsletter'},
                       {'class': ['orb-hilight'],
                        'href': 'http://www.bbc.co.uk/help/web/links/'}],
             'ratings': None,
             'reviews': None,
             'title': 'Irish cream and chocolate cheesecake',
             'total_time': 130,
             'url': None,
             'yields': '1 item(s)'},
            self.harvester_class.to_dict()
        )