## Recipe scrapers

[![Build Status](https://travis-ci.org/hhursev/recipe-scraper.svg?branch=master)](https://travis-ci.org/hhursev/recipe-scraper)
[![Coverage Status](https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=master&service=github)](https://coveralls.io/github/hhursev/recipe-scraper?branch=master)

A simple web scraping tool for recipe sites I use in a project of mine that makes sense to live as
a separate package. **No Python 2 support.**

    pip install git+git://github.com/hhursev/recipe-scraper.git

then:

    from recipe_scrapers import scrape_me

    # give the url as a string, it can be url from any site listed below
    scrape_me = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

    scrape_me.title()
    scrape_me.total_time()
    scrape_me.ingredients()
    scrape_me.instructions()


### Contribute

Part of the reason I want this open sourced is because if a site makes a design change, the scraper
for it should be modified.

If you spot a design change (or something else) that makes the scrapers unable to work for the given
site - please fire an issue asap.

If you are programmer PRs with fixes are warmly welcomed and acknowledged with a virtual beer
 :beer:.


### Scrapers available for:

- [http://101cookbooks.com/](http://101cookbooks.com/)
- [http://allrecipes.com/](http://allrecipes.com/)
- [http://bbc.co.uk/](http://bbc.co.uk/food/recipes/)
- [http://bbcgoodfood.com/](http://bbcgoodfood.com/)
- [http://bonappetit.com/](http://bonappetit.com/)
- [http://closetcooking.com/](http://closetcooking.com/)
- [http://cookstr.com/](http://cookstr.com/)
- [http://epicurious.com/](http://epicurious.com/)
- [http://finedininglovers.com/](https://www.finedininglovers.com/)
- [http://foodrepublic.com/](http://foodrepublic.com)
- [http://jamieoliver.com/](http://www.jamieoliver.com/)
- [http://mybakingaddiction.com/](http://mybakingaddiction.com/)
- [http://paninihappy.com/](http://paninihappy.com/)
- [http://realsimple.com/](http://www.realsimple.com/)
- [http://simplyrecipes.com/](http://www.simplyrecipes.com)
- [http://steamykitchen.com/](http://steamykitchen.com/)
- [http://tastykitchen.com/](http://tastykitchen.com/)
- [http://thepioneerwoman.com/](http://thepioneerwoman.com/)
- [http://thevintagemixer.com/](http://www.thevintagemixer.com/)
- [http://twopeasandtheirpod.com/](http://twopeasandtheirpod.com/)
- [http://whatsgabycooking.com/](http://whatsgabycooking.com/)
