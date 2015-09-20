import re

from .allrecipes import AllRecipes
from .bbcfood import BBCFood
from .bbcgoodfood import BBCGoodFood
from .bonappetit import BonAppetit
from .finedininglovers import FineDiningLovers
from .jamieoliver import JamieOliver
from .realsimple import RealSimple
from .simplyrecipes import SimplyRecipes
from .steamykitchen import SteamyKitchen
from .tastykitchen import TastyKitchen
from .thepioneerwoman import ThePioneerWoman
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .whatsgabycooking import WhatsGabyCooking


SCRAPERS = {
    AllRecipes.host(): AllRecipes,
    BBCFood.host(): BBCFood,
    BBCGoodFood.host(): BBCGoodFood,
    BonAppetit.host(): BonAppetit,
    FineDiningLovers.host(): FineDiningLovers,
    JamieOliver.host(): JamieOliver,
    RealSimple.host(): RealSimple,
    SimplyRecipes.host(): SimplyRecipes,
    SteamyKitchen.host(): SteamyKitchen,
    TastyKitchen.host(): TastyKitchen,
    ThePioneerWoman.host(): ThePioneerWoman,
    TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    WhatsGabyCooking.host(): WhatsGabyCooking,
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


def scrap_me(url_path):
    url_path = url_path.replace('://www.', '://')
    return SCRAPERS[url_path_to_dict(url_path)['host']](url_path)


__all__ = ['scrap_me']
