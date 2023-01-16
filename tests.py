from auth_page import AuthInputHelper, AuthLocators
from reg_page import RegInputHelper, RegLocators
from settings import name, surname, mail, phone, password


""" 4 автотеста smoke """
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


def test_successful_authorisation_by_phone(browser):
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_PHONE_TAB)
    auth_page.click_phone_tab()
    auth_page.auth_enter_phone(phone)
    auth_page.auth_enter_password(password)
    auth_page.click_enter_button()
    assert auth_page.find_element(AuthLocators.LOCATOR_EXIT_BUTTON) != ''
    # assert auth_page.find_element(AuthLocators.LOCATOR_AUTH_ERROR_TEXT) != ''


""" Далее - важные позитивные тесты """
def test_successful_authorisation_by_login(browser):
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_LOGIN_TAB)
    auth_page.click_login_tab()
    auth_page.auth_enter_phone(phone)
    auth_page.auth_enter_password(password)
    auth_page.click_enter_button()
    assert auth_page.find_element(AuthLocators.LOCATOR_EXIT_BUTTON) != ''
    # assert auth_page.find_element(AuthLocators.LOCATOR_AUTH_ERROR_TEXT) != ''

    
""" Восстановление пароля """
def test_password_recovery_by_mail(browser):
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_FORGOT_PASSWORD)
    auth_page.click_forgot_password()
    auth_page.find_element(AuthLocators.LOCATOR_USERNAME_FIELD_RECOVERY)
    auth_page.recovery_enter_username(mail)
    # auth_page.find_element(AuthLocators.LOCATOR_CAPTCHA)
    auth_page.click_continue_button()
    # assert auth_page.find_element(AuthLocators.LOCATOR_AUTH_TEXT) != ''
    assert auth_page.find_element(AuthLocators.LOCATOR_WRONG_CAPTCHA_TEXT) != ''


def test_password_recovery_by_phone(browser):
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_FORGOT_PASSWORD)
    auth_page.click_forgot_password()
    auth_page.find_element(AuthLocators.LOCATOR_USERNAME_FIELD_RECOVERY)
    auth_page.recovery_enter_username(phone)
    # auth_page.find_element(AuthLocators.LOCATOR_CAPTCHA)
    auth_page.click_continue_button()
    # assert auth_page.find_element(AuthLocators.LOCATOR_AUTH_TEXT) != ''
    assert auth_page.find_element(AuthLocators.LOCATOR_WRONG_CAPTCHA_TEXT) != ''


""" Авторизация через Google """
def test_authorization_by_google(browser):
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_BY_GOOGLE, time=5).click()
    assert auth_page.find_element(AuthLocators.LOCATOR_GOOGLE_TEXT) != ''


""" UI - тест на проверку активации кнопок """
def test_tab_change(browser):
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_MAIL_TAB)
    auth_page.click_mail_tab()
    auth_page.auth_enter_mail(phone)
    auth_page.click_empty_space()
    auth_page.find_element(AuthLocators.LOCATOR_ACTIVE_TAB)


""" Проверка на предмет "запоминания" введённых пользователем данных при последующей авторизации """
def test_check_box(browser):
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_CHECKBOX_MEMORY)
    auth_page.click_checkbox()
    auth_page.click_checkbox()
    auth_page.click_mail_tab()
    auth_page.auth_enter_mail(mail)
    auth_page.auth_enter_password(password)
    auth_page.click_enter_button()
    auth_page.find_element(AuthLocators.LOCATOR_EXIT_BUTTON)
    auth_page.click_exit_button()
    # auth_page.refresh()
    assert auth_page.find_element(AuthLocators.LOCATOR_TEXT_IN_FIELD).get_attribute("value") == mail


""" Пароль = 9 знаков """
def test_successful_registration_9_password(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    # assert reg_page.find_element(RegLocators.LOCATOR_REGISTRATION_TEXT) != ''
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password("!QAZ\"WSx@")
    reg_page.reg_confirm_password("!QAZ\"WSx@")
    reg_page.click_enter_button()
    # assert reg_page.find_element(RegLocators.LOCATOR_FIRST_CODE_FIELD) != ''
    assert reg_page.find_element(RegLocators.LOCATOR_REG_HEADER) != ""


""" Поле автоматически добавляет "+7" при вводе (920)***-**-** """
def test_auto_7_by_phone(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    # assert reg_page.find_element(RegLocators.LOCATOR_REGISTRATION_TEXT) != ''
    reg_page.reg_enter_phone("9209999999")
    auth_page.click_empty_space()
    assert auth_page.find_element(RegLocators.LOCATOR_REG_PHONE_FIELD).get_attribute("value") == phone


"""NEGATIVE"""


""" "0" (ноль) в имени при регистрации """
def test_name_zero_registration(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    reg_page.reg_enter_name("0")
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password(password)
    reg_page.reg_confirm_password(password)
    reg_page.click_enter_button()
    assert reg_page.find_element(RegLocators.LOCATOR_ERROR_NAME) != ''


""" Имя латиницей """
def test_name_latin_registration(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    reg_page.reg_enter_name("Maxim")
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password(password)
    reg_page.reg_confirm_password(password)
    reg_page.click_enter_button()
    assert reg_page.find_element(RegLocators.LOCATOR_ERROR_NAME) != ''


""" Пустое поле "Фамилия" """
def test_surname_empty_registration(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname("")
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password(password)
    reg_page.reg_confirm_password(password)
    reg_page.click_enter_button()
    assert reg_page.find_element(RegLocators.LOCATOR_ERROR_NAME) != ''


""" Пробел в поле "Фамилия" """
def test_surname_space_registration(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname(" ")
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password(password)
    reg_page.reg_confirm_password(password)
    reg_page.click_enter_button()
    assert reg_page.find_element(RegLocators.LOCATOR_ERROR_NAME) != ''


""" Пустое поле "Телефон" """
def test_phone_empty_registration(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_phone("")
    reg_page.reg_enter_password(password)
    reg_page.reg_confirm_password(password)
    reg_page.click_enter_button()
    assert reg_page.find_element(RegLocators.LOCATOR_ERROR_PHONE) != ''


""" Пароль = 7 знаков """    
def test_7_password_registration(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password("!QAZ\"Wx")
    reg_page.reg_confirm_password("!QAZ\"Wx")
    reg_page.click_enter_button()
    assert reg_page.find_element(RegLocators.LOCATOR_ERROR_PASSWORD) != ''

    
""" Пароль кириллицей """    
def test_russ_password_registration(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password("!ЙФЯ\"ЦЫч")
    reg_page.reg_confirm_password("!ЙФЯ\"ЦЫч")
    reg_page.click_enter_button()
    assert reg_page.find_element(RegLocators.LOCATOR_ERROR_PASSWORD) != ''


""" Пароль строчными """
def test_small_password_registration(browser):
    reg_page = RegInputHelper(browser)
    auth_page = AuthInputHelper(browser)
    auth_page.go_to_site()
    auth_page.find_element(AuthLocators.LOCATOR_AUTH_TO_REGPAGE)
    auth_page.click_reg_button()
    reg_page.reg_enter_name(name)
    reg_page.reg_enter_surname(surname)
    reg_page.reg_enter_phone(phone)
    reg_page.reg_enter_password("!qaz\"wsx")
    reg_page.reg_confirm_password("!qaz\"wsx")
    reg_page.click_enter_button()
    assert reg_page.find_element(RegLocators.LOCATOR_ERROR_PASSWORD) != ''
