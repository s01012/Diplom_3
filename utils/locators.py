from selenium.webdriver.common.by import By

class HomePageLocators:
    """Локаторы для работы с домашней страницей"""

    LINK_ACCOUNT_BUTTON = [By.XPATH, '//p[text()="Личный Кабинет"]/parent::a']  # Ссылка на личный кабинет

    CHECKOUT_BUTTON= [By.XPATH, '//div/button[text()="Оформить заказ"]']  # Кнопка оформить заказ

    LINK_ENTER = './/div/button[text()="Войти в аккаунт"]'  # Ссылка на форму Войти в аккаунт

class AccountProfileLocators:

    LINK_TO_PROFILE = [By.XPATH, '//a[text()="Профиль"]'] #Ссылка на раздел профиля в ЛК

    LINK_TO_HISTORY_ORDER = [By.XPATH, '//a[text()="История заказов"]']

    BUTTON_TO_EXIT = [By.XPATH, '//button[text()="Выход"]']

    TEXT_IN_ACCOUNT_PROFILE = [By.XPATH, '//p[text()="В этом разделе вы можете изменить свои персональные данные"]']


class AccountAccessLocators:

    AUTHORIZATION_FORM_TITLE = [By.XPATH, '//h2[text()="Вход"]'] # Заголовок формы авторизации

    EMAIL_INPUT_AUTHORIZATION_FORM = [By.XPATH, '//div[h2[text()="Вход"]]/descendant::label[text('
                                                ')="Email"]/following-sibling::input']  # Поле ввода эл.почты в форме
    # авторизации

    PASSWORD_INPUT_AUTHORIZATION_FORM = [By.XPATH,'//div[h2[text()="Вход"]]/descendant::label[text('
                                                  ')="Пароль"]/following-sibling::input']  # Поле ввода пароля в
    # форме авторизации

    AUTHORIZATION_BUTTON_AUTHORIZATION_FORM = [By.XPATH, './/form[@class="Auth_form__3qKeq mb-20"]/button[text('
                                                         ')="Войти"]']  # Кнопка войти в форме авторизации




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



