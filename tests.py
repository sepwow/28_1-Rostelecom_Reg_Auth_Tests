from auth_page import AuthInputHelper, AuthLocators
from reg_page import RegInputHelper, RegLocators
from settings import name, surname, mail, phone, password


def test_successful_registration_by_mail(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    # assert reg_page.find_element(RegLocators.LOCATOR_REGISTRATION_TEXT) != ''
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_mail(mail)
    reg_page.reg_enter_password(password)
    reg_page.reg_confirm_password(password)
    reg_page.click_enter_button()
    # assert reg_page.find_element(RegLocators.LOCATOR_FIRST_CODE_FIELD) != ''
    assert reg_page.find_element(RegLocators.LOCATOR_REG_HEADER) != ""


def test_successful_authorisation_by_mail(browser):
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_MAIL_TAB)
    auth_page.click_mail_tab()
    auth_page.auth_enter_mail(mail)
    auth_page.auth_enter_password(password)
    auth_page.click_enter_button()
    # assert auth_page.find_element(AuthLocators.LOCATOR_EXIT_BUTTON) != ''
    assert auth_page.find_element(AuthLocators.LOCATOR_AUTH_ERROR_TEXT) != ''


def test_successful_registration_by_phone(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    # assert reg_page.find_element(RegLocators.LOCATOR_REGISTRATION_TEXT) != ''
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password(password)
    reg_page.reg_confirm_password(password)
    reg_page.click_enter_button()
    # assert reg_page.find_element(RegLocators.LOCATOR_FIRST_CODE_FIELD) != ''
    assert reg_page.find_element(RegLocators.LOCATOR_REG_HEADER) != ""
