from selenium.webdriver.common.by import By


class MainPageLocators:

    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]/button")

# Вопросы о важном
    @staticmethod
    def question(number):
        return (By.ID, f"accordion__heading-{number}")

    @staticmethod
    def answer(number):
        return (By.ID, f"accordion__panel-{number}")