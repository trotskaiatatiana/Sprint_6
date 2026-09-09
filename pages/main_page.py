import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на вопрос FAQ")
    def click_question(self, number):
        locator = MainPageLocators.question(number)
        self.scroll_to_element(locator)
        self.click_element_with_wait(locator)

    @allure.step("Получить текст ответа FAQ")
    def get_answer_text(self, number):
        return self.find_element_with_wait(MainPageLocators.answer(number)).text

    def click_order_button_top(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_BOTTOM)