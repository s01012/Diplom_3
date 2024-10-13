import allure
from pages.base_page import BasePage
from utils.locators import *


class PasswordRecoveryPage(BasePage):

    @allure.step('Клик по ссылке "Восстановить пароль", для перехода на страницу восстановления пароля')
    def click_restore_password_link(self):
        self.click_element(PasswordRecoveryLocators.RESTORE_PASSWORD_LINK)

    @allure.step('Ввод электронной почты для восстановления пароля')
    def set_email_for_recovery_password(self, email):
        self.set_text(PasswordRecoveryLocators.EMAIL_INPUT_RECOVERY_FORM, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_restore_button(self):
        self.click_element(PasswordRecoveryLocators.RESTORE_PASSWORD_BUTTON)

    @allure.step('Клик по кнопке "Сохранить"')
    def click_save_password_button(self):
        self.click_element(PasswordRecoveryLocators.SAVE_BUTTON_IN_RECOVERY_FORM)

    @allure.step('Клик по кнопке видимости пароля')
    def click_password_visibility_button(self):
        self.click_element(PasswordRecoveryLocators.PASSWORD_VISIBILITY_BUTTON)

    @allure.step('Находим активное поле пароль')
    def search_active_field_password(self):
        return self.find_element(PasswordRecoveryLocators.ACTIVE_PASSWORD_INPUT_RECOVERY_FORM)
