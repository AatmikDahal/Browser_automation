from locator.locator import Button 
from selenium.webdriver.common.by import By


class useless_page():
    def __init__(self,browser) -> None:
        self.browser = browser

    @property
    def search(self):
        button =  self.browser.find_element(By.CSS_SELECTOR,Button.search_button)
        button.click()
    
        