import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Добавление параметра командной строки для выбора языка браузера.

    Аргументы:
        parser: Парсер аргументов pytest.
    """
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Выбор языка браузера: en, ru, fr и т.д."
    )


@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для инициализации Chrome браузера с указанным языком.

    Аргументы:
        request: Объект request pytest для доступа к конфигурации.

    Возвращает:
        WebDriver: Настроенный экземпляр браузера Chrome.
    """
    # Получаем язык из параметров командной строки
    user_language = request.config.getoption("language")

    print(f"\nЗапуск Chrome с языком '{user_language}'...")

    # Настройка опций Chrome
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )

    # Инициализация браузера
    browser = webdriver.Chrome(options=options)
    yield browser

    # Завершающие действия
    print("\nЗакрытие браузера...")
    browser.quit()
