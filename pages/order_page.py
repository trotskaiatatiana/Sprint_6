import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):

    @allure.step("Заполнить первую часть формы заказа")
    def fill_first_order_form(self, name, surname, address, metro, phone):
        self.find_element_with_wait(OrderPageLocators.NAME_INPUT).send_keys(name)
        self.find_element_with_wait(OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.find_element_with_wait(OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.find_element_with_wait(OrderPageLocators.METRO_INPUT).click()
        self.click_element_with_wait(OrderPageLocators.metro_station(metro))
        self.find_element_with_wait(OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.click_element_with_wait(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую часть формы заказа")
    def fill_second_order_form(self, date, period, color, comment):
        date_input = self.find_element_with_wait(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        self.click_element_with_wait(OrderPageLocators.RENTAL_PERIOD)
        self.click_element_with_wait(OrderPageLocators.rental_period(period))

        if color == "black":
            self.click_element_with_wait(OrderPageLocators.BLACK_COLOR)
        elif color == "grey":
            self.click_element_with_wait(OrderPageLocators.GREY_COLOR)

        self.find_element_with_wait(OrderPageLocators.COMMENT_INPUT).send_keys(comment)

        self.click_element_with_wait(OrderPageLocators.ORDER_BUTTON)

    
    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element_with_wait(OrderPageLocators.YES_BUTTON)

    @allure.step("Получить сообщение об успешном оформлении заказа")
    def get_success_message(self):
        return self.find_element_with_wait(OrderPageLocators.SUCCESS_MODAL).text