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
