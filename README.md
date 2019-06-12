## Recipe scrapers

[![Build Status](https://travis-ci.org/hhursev/recipe-scrapers.svg?branch=master)](https://travis-ci.org/hhursev/recipe-scrapers)
[![Coverage Status](https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=master&service=github)](https://coveralls.io/github/hhursev/recipe-scraper?branch=master)

A simple web scraping tool for recipe sites I use in a project of mine that makes sense to live as
a separate package. **No Python 2 support.**

    pip install git+git://github.com/hhursev/recipe-scrapers.git

then:

    from recipe_scrapers import scrape_me

    # give the url as a string, it can be url from any site listed below
    scraper = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

    scraper.title()
    scraper.total_time()
    scraper.yields()
    scraper.ingredients()
    scraper.instructions()
    scraper.links()

Note: scraper.links() returns a dictionary object containing all of the <a> tag attributes. The attribute names are the dictionary keys.

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
- [http://bbc.com/](http://bbc.com/food/recipes/)
- [http://bbc.co.uk/](http://bbc.co.uk/food/recipes/)
- [http://bbcgoodfood.com/](http://bbcgoodfood.com/)
- [http://bonappetit.com/](http://bonappetit.com/)
- [http://closetcooking.com/](http://closetcooking.com/)
- [http://cookstr.com/](http://cookstr.com/)
- [http://epicurious.com/](http://epicurious.com/)
- [http://finedininglovers.com/](https://www.finedininglovers.com/)
- [http://foodnetwork.com/](http://www.foodnetwork.com)
- [http://foodrepublic.com/](http://foodrepublic.com)
- [https://geniuskitchen.com/](https://geniuskitchen.com/)
- [http://giallozafferano.it/](http://giallozafferano.it)
- [https://healthyeating.nhlbi.nih.gov/](https://healthyeating.nhlbi.nih.gov/)
- [https://www.hellofresh.com/](https://www.hellofresh.com/)
- [https://www.hellofresh.co.uk/](https://www.hellofresh.co.uk/)
- [https://inspiralized.com/](https://inspiralized.com/)
- [http://jamieoliver.com/](http://www.jamieoliver.com/)
- [http://mybakingaddiction.com/](http://mybakingaddiction.com/)
- [http://paninihappy.com/](http://paninihappy.com/)
- [http://realsimple.com/](http://www.realsimple.com/)
- [http://simplyrecipes.com/](http://www.simplyrecipes.com)
- [http://steamykitchen.com/](http://steamykitchen.com/)
- [https://www.tastesoflizzyt.com](https://www.tastesoflizzyt.com/)
- [http://tastykitchen.com/](http://tastykitchen.com/)
- [http://thepioneerwoman.com/](http://thepioneerwoman.com/)
- [http://thehappyfoodie.co.uk/](http://thehappyfoodie.co.uk/)
- [http://thevintagemixer.com/](http://www.thevintagemixer.com/)
- [http://twopeasandtheirpod.com/](http://twopeasandtheirpod.com/)
- [http://whatsgabycooking.com/](http://whatsgabycooking.com/)
- [http://yummly.com/](http://yummly.com/)

### If you want a scraper for a new site added

- Open an [Issue](https://github.com/hhursev/recipe-scraper/issues/new) providing us the site name, as well as a recipe link from it.
- If you are a developer and want to code the scraper on your own, [this is a wonderful example](https://github.com/hhursev/recipe-scraper/pull/29/files) of how to do it.

#### For Devs

Assuming you have `python3` installed, navigate to the directory where you want this project to live in and drop these lines

    git clone git@github.com:hhursev/recipe-scrapers.git &&
    cd recipe-scrapers &&
    python3 -m venv .venv &&
    source .venv/bin/activate &&
    pip install -r requirements.txt &&
    coverage run tests.py &&
    coverage report
