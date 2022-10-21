from bs4 import BeautifulSoup

class OpenGraph:
    def __init__(self, page_data, raw=False):
        if raw:
            self.format = "raw"
            self.data = page_data
        self.format = None
        self.soup = BeautifulSoup(page_data, "html.parser")

    def image(self):
        image = self.soup.find(
            "meta", {"property": "og:image", "content": True}
        )
        return image.get("content")
