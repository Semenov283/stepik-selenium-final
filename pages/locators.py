from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, "login_form")  # Форма логина
    LOGIN_FORM_PASS = (By.ID, "id_login-password") # Форма пароля

class RegistrationPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REG_FORM_MAIL = (By.ID, "id_registration-email") # Форма почты
    REG_FORM_PASS = (By.ID, "id_registration-password1") # Форма пароля
    REG_FORM_REPLAY_PASS = (By.ID, "id_registration-password2") # Форма повтора пароля

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success strong")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, "div.alert-info p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn-default")

class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
