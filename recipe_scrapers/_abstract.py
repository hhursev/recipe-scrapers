import requests

from bs4 import BeautifulSoup


class AbstractScraper():

    def __init__(self, url, test=False):
        if test:
            # when testing, we simply load a file
            self.soup = BeautifulSoup(url.read(), "html.parser")
        else:
            self.soup = BeautifulSoup(requests.get(url).content, "html.parser")

    def host(self):
        raise NotImplementedError("This should be implemented.")

    def publisher_site(self):
        raise NotImplementedError("This should be implemented.")

    def title(self):
        raise NotImplementedError("This should be implemented.")

    def total_time(self):
        raise NotImplementedError("This should be implemented.")

    def ingredients(self):
        raise NotImplementedError("This should be implemented.")

    def directions(self):
        raise NotImplementedError("This should be implemented.")

    def social_rating(self):
        raise NotImplementedError("This should be implemented.")
