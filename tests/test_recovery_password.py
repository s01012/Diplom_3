import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import *
from utils.links import *
from pages.password_recovery_page import PasswordRecoveryPage


class TestRecoveryPassword:

    @allure.title('Проверка перехода на странице с заголовком "Восстановление пароля" по клику на ссылку "Восстановить пароль"')
    def test_click_restore_password_link(self, driver_setup):
        restore_password_page = PasswordRecoveryPage(driver_setup)
        restore_password_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        restore_password_page.click_element(HomePageLocators.LINK_ACCOUNT_BUTTON)
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        restore_password_page.click_restore_password_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(PasswordRecoveryLocators.RECOVERY_FORM_TITLE))
        current_url = restore_password_page.current_url()
        assert current_url == Links.recovery_page

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    def test_set_email_and_click_restore_password_button(self, driver_setup, setup_user):
        restore_password_page = PasswordRecoveryPage(driver_setup)
        restore_password_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        restore_password_page.click_element(HomePageLocators.LINK_ACCOUNT_BUTTON)
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        restore_password_page.click_restore_password_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(
            PasswordRecoveryLocators.RECOVERY_FORM_TITLE))
        email = setup_user.get('email')
        restore_password_page.set_email_for_recovery_password(email)
        restore_password_page.click_restore_button()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(PasswordRecoveryLocators.
                                                                            RESTORE_LABEL_IN_INPUT_CODE))
        current_url = restore_password_page.current_url()
        assert current_url == Links.reset_password_page

    @allure.title('Проверка ввода почты и клик по кнопке "Восстановить"')
    def test_make_active_field_password(self, driver_setup, setup_user):
        restore_password_page = PasswordRecoveryPage(driver_setup)
        restore_password_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        restore_password_page.click_element(HomePageLocators.LINK_ACCOUNT_BUTTON)
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        restore_password_page.click_restore_password_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(
            PasswordRecoveryLocators.RECOVERY_FORM_TITLE))
        email = setup_user.get('email')
        restore_password_page.set_email_for_recovery_password(email)
        restore_password_page.click_restore_button()
        WebDriverWait(driver_setup, 10).until(
            expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")))
        restore_password_page.click_password_visibility_button()
        assert restore_password_page.search_active_field_password()
