from selenium.webdriver.common.by import By
from base_page import BasePage


class AuthLocators:
    LOCATOR_AUTH_PHONE_TAB = (By.CSS_SELECTOR, "#t-btn-tab-phone")
    LOCATOR_AUTH_MAIL_TAB = (By.CSS_SELECTOR, "#t-btn-tab-mail")
    LOCATOR_AUTH_LOGIN_TAB = (By.CSS_SELECTOR, "#t-btn-tab-login")
    LOCATOR_AUTH_USERNAME_FIELD = (By.ID, "username")
    LOCATOR_AUTH_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_AUTH_CHECKBOX_MEMORY = (By.CLASS_NAME,
                                    "rt-base-icon rt-base-icon--default-color rt-base-icon--fill-path rt-check-small-icon rt-checkbox__check-icon rt-checkbox__check-icon")
    LOCATOR_AUTH_FORGOT_PASSWORD = (By.ID, "forgot_password")
    LOCATOR_AUTH_ENTER_BUTTON = (By.ID, "kc-login")
    LOCATOR_AUTH_BY_GOOGLE = (By.ID, "oidc_google")
    LOCATOR_AUTH_TO_REGPAGE = (By.CSS_SELECTOR, "#kc-register")
    LOCATOR_EXIT_BUTTON = (By.CSS_SELECTOR, "#logout-btn")
    LOCATOR_AUTH_ERROR_TEXT = (By.CSS_SELECTOR, "#form-error-message")


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

    def click_phone_tab(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_PHONE_TAB, time=2).click()

    def click_mail_tab(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_MAIL_TAB, time=2).click()

    def click_login_tab(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_LOGIN_TAB, time=2).click()

    def click_reg_button(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE, time=2).click()

    def click_enter_button(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_ENTER_BUTTON, time=2).click()