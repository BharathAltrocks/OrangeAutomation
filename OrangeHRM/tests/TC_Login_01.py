import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.LoginPage import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize(("username", "password"), [
    ("Admin", "admin123")
])
def test_login_with_valid_credentials(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_page("https://opensource-demo.orangehrmlive.com")

    login_page.enter_username(username)

    login_page.enter_password(password)

    login_page.click_login_button()

    if "dashboard" in driver.current_url.lower():
        print(f"The user '{username}' is logged in successfully.")
    else:
        print(f"The user '{username}' failed to login.")

    assert "dashboard" in driver.current_url.lower(), f"Login failed for user '{username}'."
