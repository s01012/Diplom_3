import allure
from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):
    @allure.step('Клик по ссылке "Личный кабинет"')
    def click_account_link(self):
        self.click_element(HomePageLocators.LINK_ACCOUNT_BUTTON)
