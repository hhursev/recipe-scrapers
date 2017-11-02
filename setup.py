import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='recipe-scrapers',
    url='https://github.com/hhursev/recipe-scrapers/',
    version='2.0.0',
    description='Python package, scraping recipes from all over the internet',
    keywords='python recipes scraper harvest',
    long_description=README,
    install_requires=[
        'beautifulsoup4>=4.4.0',
    ],
    packages=find_packages(),
    package_data={'': ['LICENSE']},
    include_package_data=True,
    classifiers=[
        'Environment :: Python 3+ module',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
