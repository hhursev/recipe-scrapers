=================
recipe-scrapers
=================

.. image:: https://img.shields.io/github/stars/hhursev/recipe-scrapers?style=social
    :target: https://github.com/hhursev/recipe-scrapers/
    :alt: Github
.. image:: https://img.shields.io/pypi/v/recipe-scrapers.svg?
    :target: https://pypi.org/project/recipe-scrapers/
    :alt: Version
.. image:: https://img.shields.io/pypi/pyversions/recipe-scrapers
    :target: https://pypi.org/project/recipe-scrapers/
    :alt: PyPI - Python Version
.. image:: https://github.com/hhursev/recipe-scrapers/actions/workflows/unittests.yaml/badge.svg?branch=main
    :target: unittests
    :alt: GitHub Actions Unittests
.. image:: https://coveralls.io/repos/hhursev/recipe-scraper/badge.svg?branch=main&service=github
    :target: https://coveralls.io/github/hhursev/recipe-scraper?branch=main
    :alt: Coveralls
.. image:: https://img.shields.io/github/license/hhursev/recipe-scrapers?
    :target: https://github.com/hhursev/recipe-scrapers/blob/main/LICENSE
    :alt: License


Quick Links
-----------
- `Documentation <https://docs.recipe-scrapers.com>`_
- `Supported Sites <https://docs.recipe-scrapers.com/getting-started/supported-sites/>`_
- `Contributing Guide <https://docs.recipe-scrapers.com/contributing/home/>`_
- `Issue Tracker <https://github.com/hhursev/recipe-scrapers/issues>`_
- `Share Project Ideas <https://github.com/hhursev/recipe-scrapers/issues/9>`_


A Python package for extracting recipe data from cooking websites. Parses recipe information from
either standard `HTML <https://developer.mozilla.org/en-US/docs/Web/HTML>`_ structure,
`Schema <https://schema.org/>`_ markup (including JSON-LD, Microdata, and RDFa formats) or
`OpenGraph <https://ogp.me/>`_ metadata.

The package provides a simple and consistent API for retrieving data such as ingredients, instructions,
cooking times, and more.

Compatible with the Python versions listed above. This package does not circumvent or bypass any
bot protection measures implemented by websites.


Installation
------------
.. code:: shell

    pip install recipe-scrapers


Basic Usage
-----------
.. code:: python

    from recipe_scrapers import scrape_me

    scraper = scrape_me("https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/")
    scraper.title()
    scraper.instructions()
    scraper.to_json()
    # for a complete list of methods:
    # help(scraper)


This package is focused **exclusively on HTML parsing**.

For advanced implementations, you'll need to implement your own solution for fetching recipe HTMLs
and managing network requests. The library works best when you provide both the HTML content and
its source domain.

You are encouraged to use our *scrape_html* method:

.. code:: python

    from recipe_scrapers import scrape_html


Supported Sites
---------------
We support a wide range of recipe websites out of the box. Check our
`supported sites list <https://docs.recipe-scrapers.com/getting-started/supported-sites/>`_
for the full list.

You can also get the full list programmatically with:

.. code:: python

    from recipe_scrapers import SCRAPERS

    SCRAPERS.keys()


Contributing
------------
We welcome contributions! Please read our
`contribution guide <https://docs.recipe-scrapers.com/contributing/home/>`_ to get started.


Special Thanks
--------------
To all the `contributors <https://github.com/hhursev/recipe-scrapers/graphs/contributors>`_ who
help make this project better!

.. image:: https://contrib.rocks/image?repo=hhursev/recipe-scrapers
   :target: https://github.com/hhursev/recipe-scrapers/graphs/contributors


Share Your Project
------------------
Have an idea for using recipe-scrapers? Check out
our `project ideas wall <https://github.com/hhursev/recipe-scrapers/issues/9>`_ for inspiration
or to share your own project!
