import allure
from pages.home_page import HomePage
from utils.locators import *


class OrderPage(HomePage):

    @allure.step('Клик по заказу на странице "Лента заказов"')
    def click_order_in_order_dashboard(self):
        self.click_element(DashboardOrderPageLocators.LINK_ORDER_CONFIG_IN_LIST)

    @allure.step('Получение всех заказов ВСЕГО сервиса')
    def getting_all_order_service(self):
        return self.find_elements(DashboardOrderPageLocators.ALL_ORDER_LIST_IN_DASHBOARD)

    @allure.step('Получение всех заказов пользователя')
    def getting_all_order_user(self):
        return self.find_elements(DashboardOrderPageLocators.ALL_ORDER_LIST_IN_PROFILE)

    @allure.step('Ввод значения в поле e-mail')
    def set_email(self, email):
        self.set_text(AccountAccessLocators.EMAIL_INPUT_AUTHORIZATION_FORM, email)

    @allure.step('Ввод значения в поле password')
    def set_password(self, password):
        self.set_text(AccountAccessLocators.PASSWORD_INPUT_AUTHORIZATION_FORM, password)

    @allure.step('Верификация отображения формы с составом заказа')
    def is_title_config_order_visible(self):
        return self.find_element(DashboardOrderPageLocators.TITLE_ORDER_DASHBOARD).is_displayed()

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

    @allure.step('Поиск количества заказов за все время')
    def getting_count_orders(self):
        return self.get_text(DashboardOrderPageLocators.COUNT_ORDER_ALL_TIME)

    @allure.step('Поиск количества заказов за день')
    def getting_daily_count_orders(self):
        return self.get_text(DashboardOrderPageLocators.COUNT_ORDER_DAILY_TIME)

    @allure.step('Получение ID заказа в форме заказа')
    def getting_order_id(self):
        return self.get_text(HomePageLocators.ORDER_ID)

    @allure.step('Получение ID заказа в разделе "В работе"')
    def getting_number_order(self):
        return self.get_text(DashboardOrderPageLocators.NUMBER_OF_ORDER)

    def wait_until_not_9999(self):
        self.wait_for_text_change(HomePageLocators.ORDER_ID, original_text='9999')

    @allure.step('Ожидание кликабельности идентификатора заказа в попап окне')
    def wait_clickable_id_order(self):
        self.wait_for_element_to_be_clickable(HomePageLocators.ORDER_ID)

    @allure.step('Дождаться загрузки "Всех заказов"')
    def wait_all_order_list_in_dashboard_visibility(self):
        return self.wait_element_visibility(DashboardOrderPageLocators.ALL_ORDER_LIST_IN_DASHBOARD)

    @allure.step('Дождаться загрузки "Лента заказов"')
    def wait_title_order_dashboard_visibility(self):
        return self.wait_element_visibility(DashboardOrderPageLocators.TITLE_ORDER_DASHBOARD)

    @allure.step('Закрытие попап окна по крестику')
    def click_to_cross(self):
        self.click_element(DashboardOrderPageLocators.BUTTON_CLOSE_ORDER)


