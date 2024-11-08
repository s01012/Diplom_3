import allure
from utils.links import *
from pages.home_page import HomePage
from pages.account_access_page import AccountAccessPage
from pages.order_page import OrderPage


class TestHomePage:

    @allure.title('Проверка перехода в "Конструктор"')
    def test_of_transition_to_construct_page_after_clicking_on_a_link_in_header(self, driver_setup):
        home_page = HomePage(driver_setup)
        account_access_page = AccountAccessPage(driver_setup)
        home_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        home_page.click_account_link()
        account_access_page.wait_authorization_form_title_visibility()
        home_page.click_construct_link()
        home_page.wait_link_account_visibility()
        current_url = home_page.current_url()
        assert current_url == Links.main_page+f'/'

    @allure.title('Проверка перехода в "Лента заказа"')
    def test_of_transition_to_dashboard_order_page_after_clicking_on_a_link_in_header(self, driver_setup):
        home_page = HomePage(driver_setup)
        order_page = OrderPage(driver_setup)
        home_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        home_page.click_dashboard_link()
        order_page.wait_title_order_dashboard_visibility()
        current_url = home_page.current_url()
        assert current_url == Links.feed_page

    @allure.title('Проверка появления всплывающего окна после клика по ингредиенту')
    def test_visible_title_popup_ingredient_after_clicking_on_a_ingredient(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        home_page.click_in_ingredient()
        current_text = home_page.is_title_popup_ingredient_visible()
        assert "Детали ингредиента" == current_text

    @allure.title('Проверка закрытия всплывающего окна после клика по крестику')
    def test_popup_ingredient_closes_after_clicking_cross_button(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        home_page.click_in_ingredient()
        home_page.close_popup_window()
        assert home_page.is_title_popup_ingredient_invisible() == False

    @allure.title('Проверка увелечения значения счетчика заказа')
    def test_ingredient_total(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        current_value = home_page.extract_ingredients_amount()
        home_page.add_ingredients_to_order_cart()
        actual_value = home_page.extract_ingredients_amount()
        assert int(actual_value) > int(current_value)

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_order_checkout_for_logged_user(self, driver_setup, setup_user):
        home_page = HomePage(driver_setup)
        account_access_page = AccountAccessPage(driver_setup)
        order_page = OrderPage(driver_setup)
        home_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        home_page.click_account_link()
        account_access_page.wait_authorization_form_title_visibility()
        email = setup_user.get('email')
        password = setup_user.get('password')
        account_access_page.set_email(email)
        account_access_page.set_password(password)
        account_access_page.click_authorization_button()
        order_page.wait_checkout_button_visibility()
        home_page.add_ingredients_to_order_cart()
        home_page.click_to_checkout_button()
        home_page.wait_title_id_visibility()
        current_text = home_page.is_title_popup_order_visible()
        assert current_text == 'идентификатор заказа'
