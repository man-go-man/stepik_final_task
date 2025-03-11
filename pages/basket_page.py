from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_see_any_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_PRESENCE_ELEMENT), "Items in basket are presented"

    def should_see_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Empty basket text is not presented"