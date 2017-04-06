#!/usr/bin/env python
# encoding: utf-8
import re

from .allrecipes import AllRecipes
from .bonappetit import BonAppetit
from .budgetbytes import BudgetBytes
from .cookstr import Cookstr
from .epicurious import Epicurious
from .finedininglovers import FineDiningLovers
from .foodrepublic import FoodRepublic
from .jamieoliver import JamieOliver
from .mybakingaddiction import MyBakingAddiction
from .simplyrecipes import SimplyRecipes
from .steamykitchen import SteamyKitchen
from .tastykitchen import TastyKitchen
from .thevintagemixer import TheVintageMixer
from .twopeasandtheirpod import TwoPeasAndTheirPod
from .whatsgabycooking import WhatsGabyCooking


SCRAPERS = {
    AllRecipes.host(): AllRecipes,
    # BonAppetit.host(): BonAppetit,
    BudgetBytes.host(): BudgetBytes,
    # Cookstr.host(): Cookstr,
    # Epicurious.host(): Epicurious,
    # FineDiningLovers.host(): FineDiningLovers,
    # FoodRepublic.host(): FoodRepublic,
    # JamieOliver.host(): JamieOliver,
    # MyBakingAddiction.host(): MyBakingAddiction,
    # SimplyRecipes.host(): SimplyRecipes,
    # SteamyKitchen.host(): SteamyKitchen,
    # TastyKitchen.host(): TastyKitchen,
    # TheVintageMixer.host(): TheVintageMixer,
    # TwoPeasAndTheirPod.host(): TwoPeasAndTheirPod,
    # WhatsGabyCooking.host(): WhatsGabyCooking,
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
