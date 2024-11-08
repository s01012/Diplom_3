import allure
from utils.links import *
from pages.account_access_page import AccountAccessPage
from pages.home_page import HomePage
from pages.order_page import OrderPage



class TestPersonalAccountProfile:

    @allure.title('Проверка перехода в личный кабинет по клику на "Личный кабинет"')
    def test_of_transition_to_login_page_after_clicking_on_a_link_in_header(self, driver_setup):
        account_access_page = AccountAccessPage(driver_setup)
        home_page = HomePage(driver_setup)
        account_access_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        account_access_page.click_account_link()
        account_access_page.wait_authorization_form_title_visibility()
        current_url = account_access_page.current_url()
        assert current_url == Links.login_page

    @allure.title('Проверка перехода в раздел история заказа по клику "История заказа"')
    def test_of_transition_to_order_history_section_after_clicking_on_a_link(self, driver_setup, setup_user):
        account_access_page = AccountAccessPage(driver_setup)
        home_page = HomePage(driver_setup)
        order_page = OrderPage(driver_setup)
        account_access_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        account_access_page.click_account_link()
        account_access_page.wait_authorization_form_title_visibility()
        email = setup_user.get('email')
        password = setup_user.get('password')
        account_access_page.set_email(email)
        account_access_page.set_password(password)
        account_access_page.click_authorization_button()
        order_page.wait_checkout_button_visibility()
        order_page.wait_for_overlay_to_disappear()
        account_access_page.click_account_link()
        account_access_page.wait_text_in_account_profile_visibility()
        account_access_page.click_link_order_history()
        current_url = account_access_page.current_url()
        assert current_url == Links.profile_order_history_page

    @allure.title('Проверка деавторизации и перехода на страницу авторизации после клика по кнопке "Выход"')
    def test_successful_logout_after__clicking_on_a_button(self, driver_setup, setup_user):
        account_access_page = AccountAccessPage(driver_setup)
        home_page = HomePage(driver_setup)
        order_page = OrderPage(driver_setup)
        account_access_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        account_access_page.click_account_link()
        account_access_page.wait_authorization_form_title_visibility()
        email = setup_user.get('email')
        password = setup_user.get('password')
        account_access_page.set_email(email)
        account_access_page.set_password(password)
        account_access_page.click_authorization_button()
        order_page.wait_checkout_button_visibility()
        account_access_page.click_account_link()
        account_access_page.wait_overlay_invisibility()
        account_access_page.click_to_exit_button()
        account_access_page.wait_authorization_form_title_visibility()
        current_url = account_access_page.current_url()
        assert current_url == Links.login_page
