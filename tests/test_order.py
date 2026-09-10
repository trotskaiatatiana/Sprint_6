import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls

class TestOrder:

    @pytest.mark.parametrize(
        "button, name, surname, address, metro, phone, date, period, color, comment",
        [
            (
                "top",
                "Анна",
                "Иванова",
                "Москва",
                "Сокольники",
                "89001234567",
                "15.09.2026",
                "сутки",
                "black",
                "Позвонить заранее"
            ),
            (
                "bottom",
                "Ирина",
                "Петрова",
                "Москва",
                "Черкизовская",
                "89998887766",
                "16.09.2026",
                "двое суток",
                "grey",
                "Без комментариев"
            ),
        ]
    )
    
    @allure.title("Успешное оформление заказа")
    def test_successful_order(self, driver, button, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)

        if button == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)

        order_page.fill_first_order_form(name, surname, address, metro, phone)

        order_page.fill_second_order_form(date, period, color, comment)

        order_page.confirm_order()

        assert "Заказ оформлен" in order_page.get_success_message()


class TestLogos:

    @allure.title("Переход на главную по логотипу Самокат")
    def test_scooter_logo_redirects_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        order_page.click_scooter_logo()

        assert order_page.get_current_url() == Urls.BASE_URL

    @allure.title("Переход на Дзен по логотипу Яндекс")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button_top()

        order_page = OrderPage(driver)
        order_page.click_yandex_logo()
        order_page.switch_to_new_window()
        order_page.wait_url(Urls.DZEN_URL)

        assert order_page.get_current_url().startswith(Urls.DZEN_URL)