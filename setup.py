import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='openeats-recipe-scraper',
    url='https://github.com/RyanNoelk/recipe-scraper/',
    version='1.0.2',
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
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
