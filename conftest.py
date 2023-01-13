import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path=r"C:\Users\galan\PycharmProjects\chromedriver.exe",
                              options=chrome_options)
    yield driver
    driver.quit()
