import re

from .allrecipes import AllRecipes
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bonappetit import BonAppetit
from .closetcooking import ClosetCooking
from .cookstr import Cookstr
from .epicurious import Epicurious
from .finedininglovers import FineDiningLovers
from .foodnetwork import FoodNetwork
from .foodrepublic import FoodRepublic
from .giallozafferano import GialloZafferano
from .hellofresh import HelloFresh
from .hundredandonecookbooks import HundredAndOneCookbooks
from .inspiralized import Inspiralized
from .jamieoliver import JamieOliver
from .mybakingaddiction import MyBakingAddiction
from .nihhealthyeating import NIHHealthyEating
from .paninihappy import PaniniHappy
from .realsimple import RealSimple
from .simplyrecipes import SimplyRecipes
from .steamykitchen import SteamyKitchen
from .tastesoflizzyt import TastesOfLizzyT
from .tastykitchen import TastyKitchen
from .thehappyfoodie import TheHappyFoodie
from .thepioneerwoman import ThePioneerWoman
from .thevintagemixer import TheVintageMixer
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .whatsgabycooking import WhatsGabyCooking
from .yummly import Yummly
from .geniuskitchen import GeniusKitchen

SCRAPERS = {
    AllRecipes.host(): AllRecipes,
    BBCFood.host(): BBCFood,
    BBCFood.host(domain='co.uk'): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BonAppetit.host(): BonAppetit,
    ClosetCooking.host(): ClosetCooking,
    Cookstr.host(): Cookstr,
    Epicurious.host(): Epicurious,
    FineDiningLovers.host(): FineDiningLovers,
    FoodNetwork.host(): FoodNetwork,
    FoodRepublic.host(): FoodRepublic,
    GialloZafferano.host(): GialloZafferano,
    HelloFresh.host(): HelloFresh,
    HelloFresh.host(domain='co.uk'): HelloFresh,
    HundredAndOneCookbooks.host(): HundredAndOneCookbooks,
    Inspiralized.host(): Inspiralized,
    JamieOliver.host(): JamieOliver,
    MyBakingAddiction.host(): MyBakingAddiction,
    NIHHealthyEating.host(): NIHHealthyEating,
    PaniniHappy.host(): PaniniHappy,
    RealSimple.host(): RealSimple,
    SimplyRecipes.host(): SimplyRecipes,
    SteamyKitchen.host(): SteamyKitchen,
    TastesOfLizzyT.host(): TastesOfLizzyT,
    TastyKitchen.host(): TastyKitchen,
    TheHappyFoodie.host(): TheHappyFoodie,
    ThePioneerWoman.host(): ThePioneerWoman,
    TheVintageMixer.host(): TheVintageMixer,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    WhatsGabyCooking.host(): WhatsGabyCooking,
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
    '''Error for when the website is not supported by this library.'''
    pass


def scrape_me(url_path):
    host_name = url_path_to_dict(url_path.replace('://www.', '://'))['host']

    try:
        scraper = SCRAPERS[host_name]
    except KeyError:
        raise WebsiteNotImplementedError(
            "Website ({}) is not supported".format(host_name))

    return scraper(url_path)


__all__ = ['scrape_me']
