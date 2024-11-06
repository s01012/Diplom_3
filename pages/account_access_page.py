import allure
from pages.base_page import BasePage
from pages.home_page import HomePage
from utils.locators import *


class AccountAccessPage(HomePage):

    @allure.step('Ввод почты на странице авторизации')
    def set_email(self, email):
        self.set_text(AccountAccessLocators.EMAIL_INPUT_AUTHORIZATION_FORM, email)

    @allure.step('Ввод пароля на странице авторизации')
    def set_password(self, password):
        self.set_text(AccountAccessLocators.PASSWORD_INPUT_AUTHORIZATION_FORM, password)

    @allure.step('Клик на кнопку "Войти" на странице авторизации')
    def click_authorization_button(self):
        self.click_element(AccountAccessLocators.AUTHORIZATION_BUTTON_AUTHORIZATION_FORM)

    @allure.step('Клик на ссылку раздела "История заказа" на странице профиля')
    def click_link_order_history(self):
        self.click_element(AccountProfileLocators.LINK_TO_HISTORY_ORDER)

    @allure.step('Клик на кнопку "Выйти" в личном кабинете')
    def click_to_exit_button(self):
        self.click_element(AccountProfileLocators.BUTTON_TO_EXIT)

    @allure.step('Дождаться загрузки "Ссылки на личный кабинет"')
    def wait_authorization_form_title_visibility(self):
        return self.wait_element_visibility(AccountAccessLocators.AUTHORIZATION_FORM_TITLE)

    @allure.step('Дождаться загрузки раздела "Смены персональных данных"')
    def wait_text_in_account_profile_visibility(self):
        return self.wait_element_visibility(AccountProfileLocators.TEXT_IN_ACCOUNT_PROFILE)

    @allure.step('Дождаться невидимости оверлей"')
    def wait_overlay_invisibility(self):
        return self.wait_invisibility(AccountProfileLocators.OVERLAY)