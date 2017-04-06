#!/usr/bin/env python
# encoding: utf-8

from pprint import pprint
from recipe_scrapers import scrap_me

try:
    scrap_me = scrap_me('http://allrecipes.com/recipe/213742/meatball-nirvana/?internalSource=staff%20pick&referringId=80&referringContentType=recipe%20hub&clickId=cardslot%205')
    pprint(scrap_me.data())
except KeyError:
    print "Website is not supported."
