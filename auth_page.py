from selenium.webdriver.common.by import By
from base_page import BasePage
from settings import *


class AuthLocators:
    LOCATOR_AUTH_TEXT = (By.XPATH, "//h1[contains(text(),'Авторизация')]")
    LOCATOR_AUTH_PHONE_TAB = (By.CSS_SELECTOR, "#t-btn-tab-phone")
    LOCATOR_AUTH_MAIL_TAB = (By.CSS_SELECTOR, "#t-btn-tab-mail")
    LOCATOR_AUTH_LOGIN_TAB = (By.CSS_SELECTOR, "#t-btn-tab-login")
    LOCATOR_AUTH_USERNAME_FIELD = (By.ID, "username")
    LOCATOR_TEXT_IN_FIELD = (By.XPATH, f'//*[contains(text(), {mail})]')
    LOCATOR_AUTH_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_AUTH_CHECKBOX_MEMORY = (By.CLASS_NAME,
                                    "rt-checkbox__label")
    LOCATOR_AUTH_FORGOT_PASSWORD = (By.ID, "forgot_password")
    LOCATOR_AUTH_ENTER_BUTTON = (By.ID, "kc-login")
    LOCATOR_AUTH_BY_GOOGLE = (By.XPATH, "//a[@id='oidc_google']")
    LOCATOR_AUTH_TO_REGPAGE = (By.CSS_SELECTOR, "#kc-register")
    LOCATOR_EXIT_BUTTON = (By.CSS_SELECTOR, "#logout-btn")
    LOCATOR_AUTH_ERROR_TEXT = (By.CSS_SELECTOR, "#form-error-message")
    LOCATOR_USERNAME_FIELD_RECOVERY = (By.XPATH, "//input[@id='username']")
    LOCATOR_CAPTCHA = (By.CSS_SELECTOR, "#captcha")
    LOCATOR_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#reset")
    LOCATOR_WRONG_CAPTCHA_TEXT = (By.CSS_SELECTOR, "#form-error-message")
    LOCATOR_GOOGLE_TEXT = (By.XPATH, "//div[contains(text(),'Войдите в аккаунт')]")
    LOCATOR_ACTIVE_TAB = (By.CLASS_NAME, "rt-tab--active")
    LOCATOR_EMPTY_SPACE = (By.XPATH, "//html")


class AuthInputHelper(BasePage):
    def auth_enter_mail(self, mail):
        mail_field = self.find_element(AuthLocators.LOCATOR_AUTH_USERNAME_FIELD)
        mail_field.click()
        mail_field.clear()
        mail_field.send_keys(mail)
        return mail_field

    def auth_enter_phone(self, phone):
        mail_field = self.find_element(AuthLocators.LOCATOR_AUTH_USERNAME_FIELD)
        mail_field.click()
        mail_field.clear()
        mail_field.send_keys(phone)
        return mail_field

    def auth_enter_password(self, password):
        password_field = self.find_element(AuthLocators.LOCATOR_AUTH_PASSWORD_FIELD)
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)
        return password_field

    def recovery_enter_username(self, mail):
        mail_field = self.find_element(AuthLocators.LOCATOR_USERNAME_FIELD_RECOVERY)
        mail_field.click()
        mail_field.send_keys(mail)
        return mail_field

    def click_phone_tab(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_PHONE_TAB, time=2).click()

    def click_mail_tab(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_MAIL_TAB, time=2).click()

    def click_login_tab(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_LOGIN_TAB, time=2).click()

    def click_forgot_password(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_FORGOT_PASSWORD, time=2).click()

    def click_reg_button(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE, time=2).click()

    def click_checkbox(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_CHECKBOX_MEMORY, time=2).click()

    def click_enter_button(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_ENTER_BUTTON, time=2).click()

    def click_exit_button(self):
        return self.find_element(AuthLocators.LOCATOR_EXIT_BUTTON, time=2).click()

    def click_continue_button(self):
        return self.find_element(AuthLocators.LOCATOR_CONTINUE_BUTTON, time=2).click()

    def click_empty_space(self):
        return self.find_element(AuthLocators.LOCATOR_EMPTY_SPACE, time=2).click()