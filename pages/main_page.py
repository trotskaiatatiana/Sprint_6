import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Нажать на вопрос FAQ")
    def click_question(self, number):
        locator = MainPageLocators.question(number)
        self.scroll_to_element(locator)
        self.click_element_with_wait(locator)

    @allure.step("Получить текст ответа FAQ")
    def get_answer_text(self, number):
        return self.find_element_with_wait(MainPageLocators.answer(number)).text

    @allure.step("Нажать верхнюю кнопку Заказать")
    def click_order_button_top(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку Заказать")
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_BOTTOM)