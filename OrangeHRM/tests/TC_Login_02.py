import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.LoginPage import LoginPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password", [("Admin", "Invalid password")])
def test_login_with_invalid_credentials(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open_page("https://opensource-demo.orangehrmlive.com")

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    assert "dashboard" not in driver.current_url.lower(), "Unexpectedly logged in with invalid credentials."
    error_message = login_page.get_error_message()
    assert error_message, "Login failed without an error message."
    print(f"Login failed. Error message: {error_message}")
