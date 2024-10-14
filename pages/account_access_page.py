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

    # @allure.step('Клик на кнопку "Выйти" в личном кабинете')
    # def set_email(self):
    #     self.set_text(AccountProfileLocators.BUTTON_TO_EXIT)