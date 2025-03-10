from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON) # символ * указывает на то, что мы передали кортеж(!) для распаковки
        add_button.click()

    def should_item_name_be_equal_to_item_name_in_basket_msg(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_ITEM_NAME), "Message of adding to basket is not presented"
        assert self.browser.find_element(*ProductPageLocators.ADDED_ITEM_NAME).text == self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def should_see_basket_value_msg(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_ITEM_NAME), "Message of adding to basket is not presented"
        assert self.browser.find_element(*ProductPageLocators.BASKET_VALUE_MSG).text == self.browser.find_element(
            *ProductPageLocators.PRICE).text