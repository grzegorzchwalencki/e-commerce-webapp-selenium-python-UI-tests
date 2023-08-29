from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    PAGE_HEADER = (By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    TOPS_CATEGORY = (By.XPATH, '//a[text()="Tops"]/@href') #
    BOTTOMS_CATEGORY = (By.XPATH, '//a[text()="Bottoms"]/@href')
    JACKETS_CATEGORY = (By.XPATH, '//a[text()="Jackets"]/@href')
    LIMITER_ITEMS_ON_PAGE = (By.XPATH, '//select[@id="limiter"]')


class CategoryPage(BasePage):
    def _verify_page(self):
        wait = WebDriverWait(self.driver, 3)
        wait.until(EC.visibility_of_element_located(Locators.TOPS_CATEGORY))
        wait.until(EC.visibility_of_element_located(Locators.BOTTOMS_CATEGORY))

    def open_tops_category(self):
        """Open Tops category page"""
        el_tops = self.driver.find_element(*Locators.TOPS_CATEGORY)
        el_tops.click()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def open_bottoms_category(self):
        el_bottoms = self.driver.find_element(*Locators.BOTTOMS_CATEGORY)
        el_bottoms.click()

    def open_jackets_category(self):
        el_jackets = self.driver.find_element(*Locators.JACKETS_CATEGORY)
        el_jackets.click()   

    def change_item_amount_on_page(self):
        els_item_amount = self.driver.find_elements(*Locators.LIMITER_ITEMS_ON_PAGE)
        el_item_amount = [i for i in els_item_amount if i.is_displayed()]
        el_item_amount[0].click()


    # Sort items
