from selenium.webdriver.common.by import By

class HomePageLocators:
    """Локаторы для работы с домашней страницей"""

    LINK_ACCOUNT_BUTTON = [By.XPATH, '//p[text()="Личный Кабинет"]/parent::a']  # Ссылка на личный кабинет

    CHECKOUT_BUTTON = [By.XPATH, '//div/button[text()="Оформить заказ"]']  # Кнопка оформить заказ

    LINK_ENTER = [By.XPATH, './/div/button[text()="Войти в аккаунт"]']  # Ссылка на форму Войти в аккаунт

    ORDER_DASHBOARD_LINK = [By.XPATH, '//p[text()="Лента Заказов"]//parent::a'] # Ссылка на Ленту Заказов

    BUN_INGREDIENT = [By.XPATH, '//p[text()="Краторная булка N-200i"]'] # Заголовок элемента булочки

    TITLE_POPUP_INGREDIENT = [By.XPATH, '//h2[text()="Детали ингредиента"]'] # Заголовок всплывающего окна с деталями

    CLOSE_BUTTON = [By.XPATH, '//button[contains(@class, "close")]'] # Кнопка закрытия попап окна

    INGREDIENTS_AMOUNT = [By.XPATH, '//ul[1]/a[2]//p[contains(@class, "num")]'] # Счетчик ингредиента (булочки)

    ORDER_CART = [By.XPATH, '//span[@class="constructor-element__text" and text()="Перетяните булочку сюда (верх)"]']

    TITLE_ID = [By.XPATH, '//p[text()="идентификатор заказа"]'] # Заголовок попап окна с id

    LINK_CONSTRUCT = [By.XPATH, '//p[text()="Конструктор"]/parent::a'] # Линк конструктора


class AccountAccessLocators:

    """Локаторы для работы с авторизацией пользователей и учетной записью"""
    AUTHORIZATION_FORM_TITLE = [By.XPATH, '//h2[text()="Вход"]'] # Заголовок формы авторизации

    EMAIL_INPUT_AUTHORIZATION_FORM = [By.XPATH, '//div[h2[text()="Вход"]]/descendant::label[text('
                                                ')="Email"]/following-sibling::input']  # Поле ввода эл.почты в форме
    # авторизации

    PASSWORD_INPUT_AUTHORIZATION_FORM = [By.XPATH,'//div[h2[text()="Вход"]]/descendant::label[text('
                                                  ')="Пароль"]/following-sibling::input']  # Поле ввода пароля в
    # форме авторизации

    AUTHORIZATION_BUTTON_AUTHORIZATION_FORM = [By.XPATH, './/form[@class="Auth_form__3qKeq mb-20"]/button[text('
                                                         ')="Войти"]']  # Кнопка войти в форме авторизации

    LINK_TO_HISTORY_ORDER = [By.XPATH, '//a[text()="История заказов"]']

    BUTTON_TO_EXIT = [By.XPATH, '//button[text()="Выход"]']

    TEXT_IN_ACCOUNT_PROFILE = [By.XPATH, '//p[text()="В этом разделе вы можете изменить свои персональные данные"]']

    OVERLAY = [By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"]


class PasswordRecoveryLocators:

    """Локаторы для работы с функционалом по восстановлению пароля"""
    RECOVERY_FORM_TITLE = [By.XPATH, '//h2[text()="Восстановление пароля"]'] # Заголовок формы восстановления пароля
    EMAIL_INPUT_RECOVERY_FORM = [By.XPATH, '//div[h2[text()="Восстановление пароля"]]//descendant::label[text('
                                           ')="Email"]/following-sibling::input'] #  Поле ввода эл.почты в форме
    # восстановления пароля

    RESTORE_PASSWORD_BUTTON = [By.XPATH, '//button[text()="Восстановить"]']
    # Кнопка "Восстановить" в форме восстановления пароля

    PASSWORD_VISIBILITY_BUTTON = [By.XPATH, '//div[contains(@class, "icon-action")]'] # Кнопка вкл видимости
    # пароля в форме восстановления пароля

    SAVE_BUTTON_IN_RECOVERY_FORM = [By.XPATH, '//button[text()="Сохранить"]'] # Кнопка "Сохраниить" в форме
    # восстановления пароля

    ACTIVE_PASSWORD_INPUT_RECOVERY_FORM = [By.CSS_SELECTOR, '.input.input_status_active'] # Состояние активного поля
    # пароль

    RESTORE_PASSWORD_LINK = [By.XPATH, '//p[text()="Забыли пароль?"]/a[text()="Восстановить пароль"]']
    # Ссылка на форму восстановления пароля

    RESTORE_LABEL_IN_INPUT_CODE = [By.XPATH, '//label[text()="Введите код из письма"]']


class DashboardOrderPageLocators:

    """Локаторы для работы с заказами"""
    TITLE_ORDER_DASHBOARD = [By.XPATH, '//h1[text()="Лента заказов"]'] # Заголовок на странице заказов

    LINK_ORDER_CONFIG_IN_LIST = [By.XPATH, '//*[contains(@class, "OrderHistory_link")]'] # Ссылка на форму с составом

    TITLE_ORDER_CONFIG = [By.XPATH, '//p[text()= "Состав"]'] # Состав

    ALL_ORDER_LIST_IN_DASHBOARD = [By.XPATH, '//div[contains(@class, "OrderHistory_textBox__3lgbs") and contains('
                                             '@class, "mb-6")]//p[contains(@class, "text_type_digits-default")]']
    # Все заказы в "Ленте заказов"

    ALL_ORDER_LIST_IN_PROFILE = [By.XPATH, '//div[contains(@class, "OrderHistory_textBox__3lgbs")]//p[contains('
                                           '@class, "text_type_digits-default") and not(ancestor::div[contains('
                                           '@class, "hidden")])]']

    COUNT_ORDER_ALL_TIME = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p']

    COUNT_ORDER_DAILY_TIME = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p']

    NUMBER_OF_ORDER = [By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]//li['
                                 'contains(@class, "text") and contains(@class, "text_type_digits-default") and '
                                 'contains(@class, "mb-2")]'] # Номер заказа

    BUTTON_CLOSE_ORDER = [By.XPATH, '//button[contains(@class, "Modal_modal__close")][1]']

    ORDER_ID = [By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow__3ikwq")]']  # Идентификатор заказа
