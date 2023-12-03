from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ._abstract import AbstractScraper


class Argiro(AbstractScraper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def host(cls):
        return "argiro.gr"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def equipment(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

        # Start Chrome browser
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Load the page
            driver.get(AbstractScraper.canonical_url(self))

            # Wait for the page to fully load (adjust the timeout as needed)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "equipment-title")))

            # Get the page source after JavaScript execution
            html_content = driver.page_source

            # Parse the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')

            # Find the equipment list using the class name 'equipment-title'
            equipment_list = soup.find_all('div', class_='equipment-title')

            # Convert the list to a set to remove duplicates
            unique_equipment_set = set(item.text.strip() for item in equipment_list)

            return list(unique_equipment_set)

        finally:
            # Close the browser
            driver.quit()
            pass

    def instructions(self):
        return self.schema.instructions()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
