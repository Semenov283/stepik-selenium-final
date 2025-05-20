from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_added_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == message, f"Expected '{product_name}' in message, got '{message}'"

    def should_be_basket_total_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == message, f"Expected '{product_price}' in message, got '{message}'"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
