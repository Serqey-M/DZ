import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    # Поле ввода username страницы авторизации
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    # Поле ввода password страницы авторизации
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    # Блок ошибки страницы авторизации
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    # Ссылка на профиль пользователя с выпадающим меню на главной странице
    LOCATOR_USER_PROFILE_LINK = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    # Поле ввода Title формы создания поста
    LOCATOR_FORM_POST_TITLE = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[1]/div/label/input')
    # Поле ввода Description формы создания поста
    LOCATOR_FORM_POST_DESCRIPTION = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea')
    # Поле ввода Content формы создания поста
    LOCATOR_FORM_POST_CONTENT = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea')
    # Название поста на странице поста сразу после его создания
    LOCATOR_POST_NAME = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    # Кнопка Login страницы авторизации
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    # Кнопка создания поста на главной странице
    LOCATOR_CREATE_POST_BTN = (By.CSS_SELECTOR, '#create-btn')
    # Кнопка сохранения поста SAVE формы создания поста
    LOCATOR_SAVE_POST_BTN = (By.CSS_SELECTOR, '.button')
    # Ссылка Contact
    LOCATOR_CONTACT = (By.XPATH, '/html/body/div[1]/main/nav/ul/li[2]/a')
    LOCATOR_CONTACT_NAME = (By.XPATH, '/html/body/div[1]/main/div/div/form/div[1]/label/input')
    LOCATOR_CONTACT_EMAIL = (By.XPATH, '/html/body/div[1]/main/div/div/form/div[2]/label/input')
    LOCATOR_CONTACT_CONTENT = (By.XPATH, '/html/body/div[1]/main/div/div/form/div[3]/label/span/textarea')
    LOCATOR_CONTACT_BTN = (By.CSS_SELECTOR, '.button')



class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f"Found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text
    
    def get_login_text(self):
        element_successful_login = self.find_element(TestSearchLocators.LOCATOR_USER_PROFILE_LINK)
        text = element_successful_login.text
        logging.info(f"Found text {text} in error field {TestSearchLocators.LOCATOR_USER_PROFILE_LINK[1]}")
        return text

    def click_create_post_button(self):
        logging.info("Click create new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    
    def enter_post_titl(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FORM_POST_TITLE[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_TITLE)
        login_field.clear()
        login_field.send_keys(word)

    def enter_post_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FORM_POST_DESCRIPTION[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_DESCRIPTION)
        login_field.clear()
        login_field.send_keys(word)
    
    
    def enter_post_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_FORM_POST_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_CONTENT)
        login_field.clear()
        login_field.send_keys(word)


    def click_save_button(self):
        logging.info("Click save button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()


    def get_added_post_titl(self):
        element_successful_login = self.find_element(TestSearchLocators.LOCATOR_POST_NAME)
        text = element_successful_login.text
        logging.info(f"Found text {text} in field {TestSearchLocators.LOCATOR_POST_NAME[1]}")
        return text


    def click_сontact(self):
        logging.info("Click Contact")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT).click()


    def enter_сontact_name(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME)
        login_field.clear()
        login_field.send_keys(word)


    def enter_сontact_email(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL)
        login_field.clear()
        login_field.send_keys(word)


    def enter_сontact_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT)
        login_field.clear()
        login_field.send_keys(word)


    def click_сontact_btn(self):
        logging.info("Click Contact btn")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()


    def alert(self):
        alert = self.find_alert()
        logging.info(alert.text)
        return alert.text