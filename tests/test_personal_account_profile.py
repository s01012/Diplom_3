import time

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import *
from utils.links import *
from pages.account_access_page import AccountAccessPage


class TestPersonalAccountProfile:

    def test_of_transition_to_login_page_after_clicking_on_a_link_in_header(self, driver_setup):
        account_access_page = AccountAccessPage(driver_setup)
        account_access_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        account_access_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        current_url = account_access_page.current_url()
        assert current_url == Links.login_page

    def test_of_transition_to_order_history_section_after_clicking_on_a_link(self, driver_setup, setup_user):
        account_access_page = AccountAccessPage(driver_setup)
        account_access_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        account_access_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        email = setup_user.get('email')
        password = setup_user.get('password')
        account_access_page.set_email(email)
        account_access_page.set_password(password)
        account_access_page.click_authorization_button()
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                CHECKOUT_BUTTON))
        WebDriverWait(driver_setup, 30).until(
            expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")))

        account_access_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountProfileLocators.
                                                                            TEXT_IN_ACCOUNT_PROFILE))
        account_access_page.click_link_order_history()
        current_url = account_access_page.current_url()
        assert current_url == Links.profile_order_history_page

    def test_successful_logout_after__clicking_on_a_button(self, driver_setup, setup_user):
        account_access_page = AccountAccessPage(driver_setup)
        account_access_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        account_access_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        email = setup_user.get('email')
        password = setup_user.get('password')
        account_access_page.set_email(email)
        account_access_page.set_password(password)
        account_access_page.click_authorization_button()
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                CHECKOUT_BUTTON))
        account_access_page.click_account_link()
        WebDriverWait(driver_setup, 30).until(
            expected_conditions.invisibility_of_element_located(AccountProfileLocators.OVERLAY)
        )
        account_access_page.click_to_exit_button()
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located
                                              (AccountAccessLocators.AUTHORIZATION_FORM_TITLE))
        current_url = account_access_page.current_url()
        assert current_url == Links.login_page

