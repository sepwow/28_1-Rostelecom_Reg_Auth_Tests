from selenium.webdriver.common.by import By
from base_page import BasePage


class RegLocators:
    LOCATOR_REG_NAME_FIELD = (By.NAME, "firstName")
    LOCATOR_REG_SURNAME_FIELD = (By.NAME, "lastName")
    LOCATOR_REG_PHONE_FIELD = (By.ID, "address")
    LOCATOR_REG_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_REG_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    LOCATOR_REG_BUTTON = (By.NAME, "register")
    LOCATOR_REG_HEADER = (By.ID, "app-header")
    LOCATOR_REGISTRATION_TEXT = (By.XPATH, "//h1[contains(text(),'Регистрация')]")
    LOCATOR_FIRST_CODE_FIELD = (By.ID, "rt-code-0")


class RegInputHelper(BasePage):
    def reg_enter_name(self, name):
        name_field = self.find_element(RegLocators.LOCATOR_REG_NAME_FIELD)
        name_field.click()
        name_field.send_keys(name)
        return name_field

    def reg_enter_surname(self, surname):
        surname_field = self.find_element(RegLocators.LOCATOR_REG_SURNAME_FIELD)
        surname_field.click()
        surname_field.send_keys(surname)
        return surname_field

    def reg_enter_phone(self, phone):
        mail_field = self.find_element(RegLocators.LOCATOR_REG_PHONE_FIELD)
        mail_field.click()
        mail_field.send_keys(phone)
        return mail_field

    def reg_enter_mail(self, mail):
        mail_field = self.find_element(RegLocators.LOCATOR_REG_PHONE_FIELD)
        mail_field.click()
        mail_field.send_keys(mail)
        return mail_field

    def reg_enter_password(self, password):
        password_field = self.find_element(RegLocators.LOCATOR_REG_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def reg_confirm_password(self, password):
        password_field = self.find_element(RegLocators.LOCATOR_REG_PASSWORD_CONFIRM)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def click_enter_button(self):
        return self.find_element(RegLocators.LOCATOR_REG_BUTTON, time=2).click()
