import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import *
from utils.links import *
from pages.password_recovery_page import PasswordRecoveryPage
from pages.home_page import HomePage
from pages.account_access_page import AccountAccessPage


class TestRecoveryPassword:

    @allure.title('Проверка перехода на странице с заголовком "Восстановление пароля" по клику на ссылку "Восстановить пароль"')
    def test_click_restore_password_link(self, driver_setup):
        restore_password_page = PasswordRecoveryPage(driver_setup)
        home_page = HomePage(driver_setup)
        account_access_page = AccountAccessPage(driver_setup)
        restore_password_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        home_page.click_account_link()
        account_access_page.wait_authorization_form_title_visibility()
        restore_password_page.click_restore_password_link()
        restore_password_page.wait_recovery_form_title_visibility()
        current_url = restore_password_page.current_url()
        assert current_url == Links.recovery_page

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    def test_set_email_and_click_restore_password_button(self, driver_setup, setup_user):
        restore_password_page = PasswordRecoveryPage(driver_setup)
        home_page = HomePage(driver_setup)
        account_access_page = AccountAccessPage(driver_setup)
        restore_password_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        home_page.click_account_link()
        account_access_page.wait_authorization_form_title_visibility()
        restore_password_page.click_restore_password_link()
        restore_password_page.wait_recovery_form_title_visibility()
        email = setup_user.get('email')
        restore_password_page.set_email_for_recovery_password(email)
        restore_password_page.click_restore_button()
        restore_password_page.wait_restore_label_in_input_code_visibility()
        current_url = restore_password_page.current_url()
        assert current_url == Links.reset_password_page

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    def test_make_active_field_password(self, driver_setup, setup_user):
        restore_password_page = PasswordRecoveryPage(driver_setup)
        home_page = HomePage(driver_setup)
        account_access_page = AccountAccessPage(driver_setup)
        restore_password_page.get_to_link(Links.main_page)
        home_page.wait_link_account_visibility()
        home_page.click_account_link()
        account_access_page.wait_authorization_form_title_visibility()
        restore_password_page.click_restore_password_link()
        restore_password_page.wait_recovery_form_title_visibility()
        email = setup_user.get('email')
        restore_password_page.set_email_for_recovery_password(email)
        restore_password_page.click_restore_button()
        home_page.wait_for_overlay_to_disappear()
        restore_password_page.click_password_visibility_button()
        assert restore_password_page.search_active_field_password()
