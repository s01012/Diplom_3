import allure
from pages.base_page import BasePage
from utils.locators import *


class PasswordRecoveryPage(BasePage):

    @allure.step('Ввод электронной почты для восстановления пароля')
    def set_email_for_recovery_password(self):
        self.set_text
