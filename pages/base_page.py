import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент с ожиданием")
    def click_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Нажать на логотип Самокат")
    def click_scooter_logo(self):
        self.click_element_with_wait(BasePageLocators.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекс")
    def click_yandex_logo(self):
        self.click_element_with_wait(BasePageLocators.YANDEX_LOGO)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Дождаться перехода по URL")
    def wait_url(self, url):
        WebDriverWait(self.driver, 10).until(lambda driver: driver.current_url.startswith(url))