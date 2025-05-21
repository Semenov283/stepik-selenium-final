from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """Проверяет, что текущая страница является страницей логина:
        - URL содержит 'login'
        - Присутствует форма логина
        - Присутствует форма регистрации
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяет, что текущий URL содержит подстроку 'login'"""
        # Кликаем на ссылку логина для перехода на страницу входа
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

        # Ожидаем появления 'login' в URL в течение 10 секунд
        WebDriverWait(self.browser, 10).until(
            EC.url_contains("login"),
            "Не удалось перейти на страницу логина: URL не содержит 'login'"
        )

        # Дополнительная проверка URL
        current_url = self.browser.current_url
        assert "login" in current_url, (
            f"URL страницы не содержит 'login'. Текущий URL: {current_url}"
        )

    def should_be_login_form(self):
        """Проверяет наличие и видимость формы логина:
        - Основная форма логина
        - Поле для ввода пароля
        """
        try:
            # Проверяем видимость формы логина
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM),
                "Форма логина не отображается на странице"
            )

            # Проверяем видимость поля пароля
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(LoginPageLocators.LOGIN_FORM_PASS),
                "Поле для ввода пароля не отображается в форме логина"
            )

        except Exception as e:
            current_url = self.browser.current_url
            raise AssertionError(
                f"Ошибка при проверке формы логина: {str(e)}\n"
                f"Текущий URL: {current_url}"
            )

    def should_be_register_form(self):
        """Проверяет наличие и видимость формы регистрации:
        - Поле для ввода email
        - Поле для ввода пароля
        - Поле для подтверждения пароля
        """
        try:
            # Проверяем основные поля формы регистрации
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(RegistrationPageLocators.REG_FORM_MAIL),
                "Поле для ввода email не отображается в форме регистрации"
            )

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(RegistrationPageLocators.REG_FORM_PASS),
                "Поле для ввода пароля не отображается в форме регистрации"
            )

            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(RegistrationPageLocators.REG_FORM_REPLAY_PASS),
                "Поле для подтверждения пароля не отображается"
            )

        except Exception as e:
            current_url = self.browser.current_url
            raise AssertionError(
                f"Ошибка при проверке формы регистрации: {str(e)}\n"
                f"Текущий URL: {current_url}"
            )

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
