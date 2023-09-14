import sys
sys.path.append(sys.path[0]+"/..")

from tests.base_test import BaseTest
from pages.category_pages import Locators , CategoryPage
from selenium.webdriver.common.by import By
from time import sleep 

class WomenCategoryTest(BaseTest):
    """Category tests"""
    def setUp(self):
        super().setUp()
        self.driver.get("https://magento.softwaretestingboard.com/women.html")
        self.category_page = CategoryPage(self.driver)        


    def test_change_displayed_items_amount_on_WomenTopsCategoryPage(self):
        """Test OPEN"""
        self.category_page.open_tops_category()
        sleep(1) #To change
        self.category_page.change_item_amount_on_page_to_36()
        sleep(2) #To change
        #Expected result
        #1. Find all items displayed after changing item amount on page to 36.
        #2. Check lenght of result list of items
        current_items_on_page = self.category_page.amount_of_all_displayed_items_on_page()
        #3. Compere amount of items on page to expected value
        self.assertEqual(current_items_on_page, int("36") )
        
    def test_sort_items_by_price_WomenTopsCategoryPage(self):
        self.category_page.open_tops_category()
        sleep(1) #To change
        self.category_page.sort_items_by_price()
        sleep(1) #To change

        result_items_order_after_sorting = self.category_page.all_products_sorted_by_price()
        properly_items_order_after_sorting = self.category_page.properly_sorted_items_by_price_ascending()

        self.assertEqual(result_items_order_after_sorting , properly_items_order_after_sorting)


