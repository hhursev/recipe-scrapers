from ._exceptions import OpenGraphException


class OpenGraph:
    def __init__(self, soup):
        self.soup = soup

    def site_name(self):
        meta = self.soup.find("meta", {"property": "og:site_name"})
        meta = meta or self.soup.find("meta", {"name": "og:site_name"})
        if not meta:
            raise OpenGraphException("Site name not found in OpenGraph metadata.")

        return meta.get("content")

    def image(self):
        image = self.soup.find("meta", {"property": "og:image", "content": True})
        if not image:
            raise OpenGraphException("Image not found in OpenGraph metadata.")

        return image.get("content")
