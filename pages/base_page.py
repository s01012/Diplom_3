import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from utils.locators import *


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

    @allure.step("Получение текста")
    def get_text(self, locator):
        text_element = self.find_element(locator).text
        return text_element

    @allure.step('Проверка закрытия окна')
    def is_element_invisible(self, locator):
        return WebDriverWait(self.driver_setup, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Перетаскивание элемента')
    def perform_drag_and_drop(self, drag_element_locator, drop_element_locator):
        element_to_move = self.find_element(drag_element_locator)
        destination_element = self.find_element(drop_element_locator)

        js_script = """
            function triggerDragAndDrop(dragElement, dropElement) {
                const dragStartEvent = new Event('dragstart', { bubbles: true });
                const dropEvent = new Event('drop', { bubbles: true });
                const dragEndEvent = new Event('dragend', { bubbles: true });

                dragElement.dispatchEvent(dragStartEvent);
                dropElement.dispatchEvent(dropEvent);
                dragElement.dispatchEvent(dragEndEvent);
            }

            const dragElement = arguments[0];
            const dropElement = arguments[1];
            triggerDragAndDrop(dragElement, dropElement);
        """

        self.driver_setup.execute_script(js_script, element_to_move, destination_element)

    @allure.step('Поиск нескольких элементов')
    def find_elements(self, locator):
        return WebDriverWait(self.driver_setup, 10).until(expected_conditions.
                                                          presence_of_all_elements_located(locator))

    @allure.step('Клик вне области попап')
    def click_outside_popup(self):
        body = self.driver_setup.find_element(By.TAG_NAME, 'body')
        x = body.size['width'] / 2
        y = body.size['height'] / 2
        ActionChains(self.driver_setup).move_by_offset(x, y).click().perform()