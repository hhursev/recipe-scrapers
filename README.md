## Recipe scrapers

[![Build Status](https://travis-ci.org/hhursev/recipe-scraper.svg?branch=master)](https://travis-ci.org/hhursev/recipe-scraper)
[![Coverage Status](https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=master&service=github)](https://coveralls.io/github/hhursev/recipe-scraper?branch=master)

A simple web scraping tool for recipe sites I use in a project of mine that makes sense to live as
a separate package.

    pip install git+git://github.com/hhursev/recipe-scraper.git

then:

    from recipe_scrapers import scrap_me

    # give the url as a string, it can be url from any site listed below
    scrap_me = scrap_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

    scrap_me.title()
    scrap_me.total_time()
    scrap_me.ingredients()
    scrap_me.instructions()


### Contribute

Part of the reason I want this open sourced is because if a site makes a design change, the scraper
for it should be modified.

If you spot a design change (or something else) that makes the scrapers unable to work for the given
site - please fire an issue asap.

If you are programmer a PRs with fixes are warmly welcomed and acknowledged with a virtual beer
 :beer:.


### Scrapers available for:

- [http://allrecipes.com/](http://allrecipes.com/)
- [http://simplyrecipes.com/](http://www.simplyrecipes.com)
- [http://twopeasandtheirpod.com/](http://twopeasandtheirpod.com/)
- [http://tastykitchen.com/](http://tastykitchen.com/)
