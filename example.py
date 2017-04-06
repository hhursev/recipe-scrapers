#!/usr/bin/env python
# encoding: utf-8

from recipe_scrapers import scrap_me

try:
    scrap_me = scrap_me('https://www.budgetbytes.com/2017/03/lemon-garlic-roasted-chicken')
    print(scrap_me.data())
except KeyError:
    print "Website is not supported."
