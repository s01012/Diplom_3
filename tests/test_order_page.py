import time

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import *
from utils.links import *
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка появления всплывающего окна после клика по заказу')
    def test_visible_popup_order_after_clicking_on_a_ingredient(self, driver_setup):
        order_page = OrderPage(driver_setup)
        order_page.get_to_link(Links.feed_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        order_page.click_order_in_order_dashboard()
        assert order_page.is_title_config_order_visible() == True

    @allure.title('Проверка идентичности отображения заказов на странице истории и ленты заказов')
    def test_identical_order_id(self, driver_setup, setup_user):
        order_page = OrderPage(driver_setup)
        order_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        order_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        email = setup_user.get('email')
        password = setup_user.get('password')
        order_page.set_text(AccountAccessLocators.EMAIL_INPUT_AUTHORIZATION_FORM, email)
        order_page.set_text(AccountAccessLocators.PASSWORD_INPUT_AUTHORIZATION_FORM, password)
        order_page.click_element(AccountAccessLocators.AUTHORIZATION_BUTTON_AUTHORIZATION_FORM)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                CHECKOUT_BUTTON))
        order_page.add_ingredients_to_order_cart()
        order_page.click_to_checkout_button()
        order_page.wait_until_not_9999()
        order_page.click_element(DashboardOrderPageLocators.BUTTON_CLOSE_ORDER)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                ORDER_DASHBOARD_LINK))

        order_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(
            expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
        )
        order_page.click_element(AccountProfileLocators.LINK_TO_HISTORY_ORDER)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(DashboardOrderPageLocators.ALL_ORDER_LIST_IN_DASHBOARD))
        feed_locator = order_page.getting_all_order(DashboardOrderPageLocators.ALL_ORDER_LIST_IN_DASHBOARD)
        history_locator = order_page.getting_all_order(DashboardOrderPageLocators.ALL_ORDER_LIST_IN_PROFILE)
        assert order_page.compare_orders(history_locator, feed_locator) == True

    @allure.title('Проверка увелечения счетчика "за все время" после совершения заказа')
    def test_all_time_counter_value_increases(self, driver_setup, setup_user):
        order_page = OrderPage(driver_setup)
        order_page.get_to_link(Links.feed_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        counter_value = order_page.getting_count_orders(DashboardOrderPageLocators.COUNT_ORDER_ALL_TIME)
        order_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        email = setup_user.get('email')
        password = setup_user.get('password')
        order_page.set_text(AccountAccessLocators.EMAIL_INPUT_AUTHORIZATION_FORM, email)
        order_page.set_text(AccountAccessLocators.PASSWORD_INPUT_AUTHORIZATION_FORM, password)
        order_page.click_element(AccountAccessLocators.AUTHORIZATION_BUTTON_AUTHORIZATION_FORM)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                CHECKOUT_BUTTON))
        order_page.add_ingredients_to_order_cart()
        order_page.click_to_checkout_button()
        order_page.wait_until_not_9999()
        order_page.click_element(DashboardOrderPageLocators.BUTTON_CLOSE_ORDER)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                ORDER_DASHBOARD_LINK))
        order_page.click_element(HomePageLocators.ORDER_DASHBOARD_LINK)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                ORDER_DASHBOARD_LINK))
        current_value = order_page.getting_count_orders(DashboardOrderPageLocators.COUNT_ORDER_ALL_TIME)
        assert current_value > counter_value

    @allure.title('Проверка увелечения счетчика "за все сегодня" после совершения заказа')
    def test_daily_time_counter_value_increases(self, driver_setup, setup_user):
        order_page = OrderPage(driver_setup)
        order_page.get_to_link(Links.feed_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        counter_value = order_page.getting_count_orders(DashboardOrderPageLocators.COUNT_ORDER_DAILY_TIME)
        order_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        email = setup_user.get('email')
        password = setup_user.get('password')
        order_page.set_text(AccountAccessLocators.EMAIL_INPUT_AUTHORIZATION_FORM, email)
        order_page.set_text(AccountAccessLocators.PASSWORD_INPUT_AUTHORIZATION_FORM, password)
        order_page.click_element(AccountAccessLocators.AUTHORIZATION_BUTTON_AUTHORIZATION_FORM)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                CHECKOUT_BUTTON))
        order_page.add_ingredients_to_order_cart()
        order_page.click_to_checkout_button()
        order_page.wait_until_not_9999()
        order_page.click_element(DashboardOrderPageLocators.BUTTON_CLOSE_ORDER)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                ORDER_DASHBOARD_LINK))
        order_page.click_element(HomePageLocators.ORDER_DASHBOARD_LINK)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                ORDER_DASHBOARD_LINK))
        current_value = order_page.getting_count_orders(DashboardOrderPageLocators.COUNT_ORDER_DAILY_TIME)
        assert current_value > counter_value

    @allure.title('Проверка отображения идентификатора заказа в разделе "В работе" после совершения заказа')
    def test_visible_id_in_work_order(self, driver_setup, setup_user):
        order_page = OrderPage(driver_setup)
        order_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        order_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        email = setup_user.get('email')
        password = setup_user.get('password')
        order_page.set_text(AccountAccessLocators.EMAIL_INPUT_AUTHORIZATION_FORM, email)
        order_page.set_text(AccountAccessLocators.PASSWORD_INPUT_AUTHORIZATION_FORM, password)
        order_page.click_element(AccountAccessLocators.AUTHORIZATION_BUTTON_AUTHORIZATION_FORM)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                CHECKOUT_BUTTON))
        order_page.add_ingredients_to_order_cart()
        order_page.click_to_checkout_button()
        order_page.wait_until_not_9999()
        order_id_in_form = order_page.getting_order_id()
        order_page.click_element(DashboardOrderPageLocators.BUTTON_CLOSE_ORDER)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                ORDER_DASHBOARD_LINK))
        order_page.click_element(HomePageLocators.ORDER_DASHBOARD_LINK)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                ORDER_DASHBOARD_LINK))
        number_of_order = order_page.getting_number_order()
        assert f'0{order_id_in_form}' == number_of_order
