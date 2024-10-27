import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.locators import *
from utils.links import *
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Проверка перехода в "Конструктор"')
    def test_of_transition_to_construct_page_after_clicking_on_a_link_in_header(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        home_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        home_page.click_construct_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        current_url = home_page.current_url()
        assert current_url == Links.main_page+f'/'

    @allure.title('Проверка перехода в "Лента заказа"')
    def test_of_transition_to_dashboard_order_page_after_clicking_on_a_link_in_header(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        home_page.click_dashboard_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(DashboardOrderPageLocators.TITLE_ORDER_DASHBOARD))
        current_url = home_page.current_url()
        assert current_url == Links.feed_page

    @allure.title('Проверка появления всплывающего окна после клика по ингредиенту')
    def test_visible_title_popup_ingredient_after_clicking_on_a_ingredient(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        home_page.click_in_ingredient()
        current_text = home_page.is_title_popup_ingredient_visible()
        assert "Детали ингредиента" == current_text

    @allure.title('Проверка закрытия всплывающего окна после клика по крестику')
    def test_visible_title_popup_ingredient_after_clicking_on_a_ingredient(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        home_page.click_in_ingredient()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              invisibility_of_element_located(DashboardOrderPageLocators.TITLE_ORDER_DASHBOARD))
        home_page.close_popup_window()
        assert home_page.is_title_popup_ingredient_invisible() == False

    @allure.title('Проверка увелечения значения счетчика заказа')
    def test_ingredient_total(self, driver_setup):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        current_value = home_page.get_text(HomePageLocators.INGREDIENTS_AMOUNT)
        home_page.add_ingredients_to_order_cart()
        actual_value = home_page.get_text(HomePageLocators.INGREDIENTS_AMOUNT)
        assert int(actual_value) > int(current_value)

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_order_checkout_for_logged_user(self, driver_setup, setup_user):
        home_page = HomePage(driver_setup)
        home_page.get_to_link(Links.main_page)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                LINK_ACCOUNT_BUTTON))
        home_page.click_account_link()
        WebDriverWait(driver_setup, 10).until(expected_conditions.
                                              visibility_of_element_located(AccountAccessLocators.
                                                                            AUTHORIZATION_FORM_TITLE))
        email = setup_user.get('email')
        password = setup_user.get('password')
        home_page.set_text(AccountAccessLocators.EMAIL_INPUT_AUTHORIZATION_FORM, email)
        home_page.set_text(AccountAccessLocators.PASSWORD_INPUT_AUTHORIZATION_FORM, password)
        home_page.click_element(AccountAccessLocators.AUTHORIZATION_BUTTON_AUTHORIZATION_FORM)
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                CHECKOUT_BUTTON))
        home_page.add_ingredients_to_order_cart()
        home_page.click_to_checkout_button()
        WebDriverWait(driver_setup, 10).until(expected_conditions.visibility_of_element_located(HomePageLocators.
                                                                                                TITLE_ID))
        current_text = home_page.is_title_popup_order_visible()
        assert current_text == 'идентификатор заказа'
