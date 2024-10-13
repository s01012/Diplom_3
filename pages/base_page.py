import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver_setup = driver

    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return WebDriverWait(self.driver_setup, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        WebDriverWait(self.driver_setup, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        ).click()

    @allure.step("Переход по ссылке")
    def get_to_link(self, links: str):
        self.driver_setup.get(links)

    @allure.step("Получение текущего url")
    def current_url(self):
        return self.driver_setup.current_url

    @allure.step("Скроллинг к элементу")
    def scroll_to_element(self, locator):
        scroll_to_element = WebDriverWait(self.driver_setup, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        self.driver_setup.execute_script(
            "arguments[0].scrollIntoView(true);", scroll_to_element
        )

    @allure.step("Ввод текста")
    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

