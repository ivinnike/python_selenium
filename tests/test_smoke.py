
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# каждый тест должен начинаться с test_
def test_product_view_sku():
    """
    Test case WERT-1
    """
		# Описываем опции запуска браузера
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"
	
		# устанавливаем webdriver в соответствии с версией используемого браузера
    service = Service(ChromeDriverManager().install())
    # запускаем браузер с указанными выше настройками
    driver = webdriver.Chrome(service=service, options=chrome_options)
		# определяем адрес страницы для теста и переходим на неё
    url = "https://www.vprok.ru/"
    driver.get(url=url)
		# ищем по селектору элемент меню "Детские товары" и кликаем по нему
    element = driver.find_element(by=By.XPATH, value="//a[normalize-space(.)='Детские товары']")
    element.click()
    # чтобы просмотреть детали
    element = driver.find_element(by=By.XPATH, value='//a[normalize-space(.)="Творог детский Агуша Черника 3.9% 100г"]')
    element.click()
		# ищем по имени класса артикул для "Творог детский Агуша Черника 3.9% 100г"
    sku = driver.find_element(By.CLASS_NAME, value="Title_articul__fJ5GI")
		# проверяем соответствие
    assert sku.text == '307002', "Unexpected sku"