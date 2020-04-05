import re

from .allrecipes import AllRecipes
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bettycrocker import BettyCrocker
from .bonappetit import BonAppetit
from .budgetbytes import BudgetBytes
from .closetcooking import ClosetCooking
from .cookstr import Cookstr
from .copykat import CopyKat
from .cybercook import Cybercook
from .delish import Delish
from .epicurious import Epicurious
from .finedininglovers import FineDiningLovers
from .food import Food
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .giallozafferano import GialloZafferano
from .gonnawantseconds import GonnaWantSeconds
from .greatbritishchefs import GreatBritishChefs
from .heinzbrasil import HeinzBrasil
from .hellofresh import HelloFresh
from .hundredandonecookbooks import HundredAndOneCookbooks
from .ig import IG
from .inspiralized import Inspiralized
from .jamieoliver import JamieOliver
from .justbento import JustBento
from .kitchn import Kitchn
from .matprat import Matprat
from .mindmegette import Mindmegette
from .misya import Misya
from .mybakingaddiction import MyBakingAddiction
from .nihhealthyeating import NIHHealthyEating
from .panelinha import Panelinha
from .paninihappy import PaniniHappy
from .przepisy import Przepisy
from .realsimple import RealSimple
from .seriouseats import SeriousEats
from .simplyrecipes import SimplyRecipes
from .southernliving import SouthernLiving
from .steamykitchen import SteamyKitchen
from .tastesoflizzyt import TastesOfLizzyT
from .tastykitchen import TastyKitchen
from .thehappyfoodie import TheHappyFoodie
from .thepioneerwoman import ThePioneerWoman
from .thespruceeats import TheSpruceEats
from .thevintagemixer import TheVintageMixer
from .tineno import TineNo
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .whatsgabycooking import WhatsGabyCooking
from .wikicookbook import WikiCookbook
from .yummly import Yummly
from .geniuskitchen import GeniusKitchen

SCRAPERS = {
    AllRecipes.host(): AllRecipes,
    BBCFood.host(): BBCFood,
    BBCFood.host(domain='co.uk'): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BettyCrocker.host(): BettyCrocker,
    BonAppetit.host(): BonAppetit,
    BudgetBytes.host(): BudgetBytes,
    ClosetCooking.host(): ClosetCooking,
    Cookstr.host(): Cookstr,
    CopyKat.host(): CopyKat,
    Cybercook.host(): Cybercook,
    Delish.host(): Delish,
    Epicurious.host(): Epicurious,
    FineDiningLovers.host(): FineDiningLovers,
    Food.host(): Food,
    FoodNetwork.host(): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    GialloZafferano.host(): GialloZafferano,
    GonnaWantSeconds.host(): GonnaWantSeconds,
    GreatBritishChefs.host(): GreatBritishChefs,
    HeinzBrasil.host(): HeinzBrasil,
    HelloFresh.host(): HelloFresh,
    HelloFresh.host(domain='co.uk'): HelloFresh,
    HundredAndOneCookbooks.host(): HundredAndOneCookbooks,
    IG.host(): IG,
    Inspiralized.host(): Inspiralized,
    JamieOliver.host(): JamieOliver,
    JustBento.host(): JustBento,
    Kitchn.host(): Kitchn,
    Matprat.host(): Matprat,
    Mindmegette.host(): Mindmegette,
    Misya.host(): Misya,
    MyBakingAddiction.host(): MyBakingAddiction,
    NIHHealthyEating.host(): NIHHealthyEating,
    Panelinha.host(): Panelinha,
    PaniniHappy.host(): PaniniHappy,
    Przepisy.host(): Przepisy,
    RealSimple.host(): RealSimple,
    SeriousEats.host(): SeriousEats,
    SimplyRecipes.host(): SimplyRecipes,
    SouthernLiving.host(): SouthernLiving,
    SteamyKitchen.host(): SteamyKitchen,
    TastesOfLizzyT.host(): TastesOfLizzyT,
    TastyKitchen.host(): TastyKitchen,
    TheHappyFoodie.host(): TheHappyFoodie,
    ThePioneerWoman.host(): ThePioneerWoman,
    TheSpruceEats.host(): TheSpruceEats,
    TheVintageMixer.host(): TheVintageMixer,
    TineNo.host(): TineNo,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    WhatsGabyCooking.host(): WhatsGabyCooking,
    WikiCookbook.host(): WikiCookbook,
    Yummly.host(): Yummly,
    GeniusKitchen.host(): GeniusKitchen,
}


def url_path_to_dict(path):
    pattern = (r'^'
               r'((?P<schema>.+?)://)?'
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
               r'(?P<host>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<query>[?].*?)?'
               r'$'
               )
    regex = re.compile(pattern)
    matches = regex.match(path)
    url_dict = matches.groupdict() if matches is not None else None

    return url_dict


class WebsiteNotImplementedError(NotImplementedError):
    """ Error for when the website is not supported by this library. """
    pass


def scrape_me(url_path):

    host_name = url_path_to_dict(url_path.replace('://www.', '://'))['host']

    try:
        scraper = SCRAPERS[host_name]
    except KeyError:
        raise WebsiteNotImplementedError(
            "Website ({}) is not supported".format(host_name)
        )

    return scraper(url_path)


__all__ = ['scrape_me']
name = "recipe_scrapers"
