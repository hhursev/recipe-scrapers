import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="recipe_scrapers",
    url="https://github.com/hhursev/recipe-scrapers/",
    version="6.0.2",
    author="Hristo Harsev",
    author_email="r+pypi@hharsev.com",
    description="Python package, scraping recipes from all over the internet",
    keywords="python recipes scraper harvest recipe-scraper recipe-scrapers",
    long_description=README,
    install_requires=[
        "beautifulsoup4>=4.6.0",
        "extruct>=0.8.0",
        "requests>=2.19.1",
    ],
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.5'
)
