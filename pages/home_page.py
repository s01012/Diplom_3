import allure
from pages.base_page import BasePage
from utils.locators import *


class HomePage(BasePage):

    @allure.step('Клик по ссылке "Личный кабинет"')
    def click_account_link(self):
        self.click_element(HomePageLocators.LINK_ACCOUNT_BUTTON)

    @allure.step('Клик по ссылке "Конструктор"')
    def click_construct_link(self):
        self.click_element(HomePageLocators.LINK_CONSTRUCT)

    @allure.step('Клик по ссылке "Лента заказа"')
    def click_dashboard_link(self):
        self.click_element(HomePageLocators.ORDER_DASHBOARD_LINK)

    @allure.step('Клик по ингредиенту')
    def click_in_ingredient(self):
        self.click_element(HomePageLocators.BUN_INGREDIENT)

    @allure.step('Проверка открытия окна с деталями заказа')
    def is_title_popup_ingredient_visible(self):
        return self.get_text(HomePageLocators.TITLE_POPUP_INGREDIENT)

    @allure.step('Закрытие попап окна "Детали заказа"')
    def close_popup_window(self):
        self.click_element(HomePageLocators.CLOSE_BUTTON)

    @allure.step('Проверка закрытия попап окна с деталями ингредиентов')
    def is_title_popup_ingredient_invisible(self):
        return self.is_element_invisible(HomePageLocators.TITLE_POPUP_INGREDIENT).is_displayed()

    @allure.step('Получаем значение кол-ва выбранного ингредиента')
    def extract_ingredients_amount(self):
        return self.get_text(HomePageLocators.INGREDIENTS_AMOUNT)

    @allure.step('Добавить ингредиенты')
    def add_ingredients_to_order_cart(self):
        self.perform_drag_and_drop(HomePageLocators.BUN_INGREDIENT, HomePageLocators.ORDER_CART)

    @allure.step('Нажать по кнопке оформить заказ')
    def click_to_checkout_button(self):
        return self.click_element(HomePageLocators.CHECKOUT_BUTTON)

    @allure.step('Проверка открытия окна с id заказа')
    def is_title_popup_order_visible(self):
        return self.get_text(HomePageLocators.TITLE_ID)

    @allure.step('Дождаться загрузки "Ссылки на личный кабинет"')
    def wait_link_account_visibility(self):
        return self.find_element(HomePageLocators.LINK_ACCOUNT_BUTTON)

    @allure.step('Дождаться загрузки кнопки "Оформить заказ"')
    def wait_checkout_button_visibility(self):
        return self.find_element(HomePageLocators.CHECKOUT_BUTTON)

    @allure.step('Дождаться загрузки "Лента заказов"')
    def wait_dashboard_link_visibility(self):
        return self.find_element(HomePageLocators.ORDER_DASHBOARD_LINK)

    @allure.step('Дождаться загрузки "Заголовка ID"')
    def wait_title_id_visibility(self):
        return self.find_element(HomePageLocators.TITLE_ID)
