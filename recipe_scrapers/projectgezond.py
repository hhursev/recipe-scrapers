from ._abstract import AbstractScraper


class ProjectGezond(AbstractScraper):
    @classmethod
    def host(cls):
        return "projectgezond.nl"

    def author(self):
        return "Project Gezond"

    def ratings(self):
        # Ratings do not exist on this site
        return None

    def cuisine(self):
        # Not listed on site
        return None
    
    def category(self):
        category_script = self.soup.find("script", text=lambda text: text and "var dataLayer_content =" in text)
        if category_script:
            category_text = category_script.string
            start = category_text.find('"pageCategory":[')
            if start != -1:
                start += len('"pageCategory":[')
                end = category_text.find(']', start)
                if end != -1:
                    categories = category_text[start:end].strip('"').split('","')
                    return categories if categories else None
        return None
