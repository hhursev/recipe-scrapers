from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


class MyRecipes(AbstractScraper):
    
    @classmethod
    def host(self):
        return 'myrecipes.com'

    def title(self):
        return self.soup.find(
            'h1',
            {'class': 'headline heading-content'}
        ).get_text()     


    def total_time(self):
        for item in self.soup.find_all('div', {'class': 'recipe-meta-item-header'}):
            header = normalize_string(item.get_text())
            if header == "Total Time":
                return get_minutes(self.soup.find(
                        'div', 
                        {'class': 'recipe-meta-item-body'}
                    ).get_text()
                
                 
    # TODO: Fix yields
    # def yields(self):
    #     for items in self.soup.find_all('div', {'class': 'recipe-meta-item'}):
    #         item_headers = items.find_all('div', {'class': 'recipe-meta-item-header'})
    #         for item_header in item_headers:
    #             print(item_header)
    #             header = normalize_string(item_header.get_text())
    #             if header == "Yield":
    #                 print(header)
    #                 yields = item_header.next_sibling
    #                 print(yields)
    #                 return get_yields(f"{yields} servings")