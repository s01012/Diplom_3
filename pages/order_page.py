import allure
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from utils.locators import *


class OrderPage(HomePage):

    @allure.step('Клик по заказу на странице "Лента заказов"')
    def click_order_in_order_dashboard(self):
        self.click_element(DashboardOrderPageLocators.LINK_ORDER_CONFIG_IN_LIST)

    @allure.step('Верификация отображения формы с составом заказа')
    def is_title_config_order_visible(self):
        return self.find_element(DashboardOrderPageLocators.TITLE_ORDER_DASHBOARD).is_displayed()

    @allure.step('Получение всех заказов')
    def getting_all_order(self, locator):
        return self.find_elements(locator)

    @allure.step('Сравнение заказов из истории с общей лентой')
    def compare_orders(self, history_locator, feed_locator):
        user_history_orders = history_locator
        global_feed_orders = feed_locator
        history_set = {order.text for order in user_history_orders}
        feed_set = {order.text for order in global_feed_orders}

        if history_set <= feed_set:
            return True
        else:
            return False

    @allure.step('Поиск количества заказов')
    def getting_count_orders(self, locator):
        return self.get_text(locator)

    @allure.step('Получение ID заказа в форме заказа')
    def getting_order_id(self):
        return self.get_text(HomePageLocators.ORDER_ID)

    @allure.step('Получение ID заказа в разделе "В работе"')
    def getting_number_order(self):
        return self.get_text(DashboardOrderPageLocators.NUMBER_OF_ORDER)

    def wait_until_not_9999(self):
        """
        Этот метод ожидает, пока элемент с текстом '9999' не станет невидимым.
        """
        wait = WebDriverWait(self.driver_setup, 10)

        # Ожидание исчезновения элемента с текстом '9999'
        def element_with_text_not_visible(driver):
            element = driver.find_element(*HomePageLocators.ORDER_ID)
            return element.is_displayed() and '9999' not in element.text

        wait.until(element_with_text_not_visible)
