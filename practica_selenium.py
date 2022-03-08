import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # неявные ожидания
implicitly_waits = driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody')  # неявные ожидания


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def click():
    pass


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('mia_85@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('qwerty')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    pytest.driver.find_element_by_class_name('navbar-toggler-icon').click()
    pytest.driver.find_element_by_xpath('//*[contains(text(),"Мои питомцы")]').click()
    try:
        explicit_waits = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]')))  # явные ожидания
        assert explicit_waits == '//*[@id="all_my_pets"]'
        print('Есть совпадение')
    except TimeoutException:
        print('Нет совпадений')
    finally:
        driver.quit()

    def test_show_my_pets():
        # Вводим email
        pytest.driver.find_element_by_id('email').send_keys('mia_85@mail.ru')
        # Вводим пароль
        pytest.driver.find_element_by_id('pass').send_keys('qwerty')
        # Нажимаем на кнопку входа в аккаунт
        pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
        pytest.driver.find_element_by_class_name('navbar-toggler-icon').click()
        pytest.driver.find_element_by_xpath('//*[contains(text(),"Мои питомцы")]').click()
        try:
            explicit_waits = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]')))  # явные ожидания
            assert explicit_waits == '//*[@id="all_my_pets"]'
            print('Есть совпадение')
        except TimeoutException:
            print('Нет совпадений')
        finally:
            driver.quit()

animals_names = ['Piter', 'Leo', 'Егонет', 'Симба', 'Джо']
unique = []


def test_get_unique_names():  # У всех питомцев разные имена
    for animals_names in unique:
        if animals_names in unique:
            continue
        else:
            unique.append(animals_names)
        return unique


print(test_get_unique_names())
