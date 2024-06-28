from selenium.webdriver.common.by import By

from utils.WebUtilities import WebUtilities


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.web_util = WebUtilities(driver)
        self.USERNAME_FIELD = (By.XPATH, "//input[@placeholder='Username']")
        self.PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Password']")
        self.LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Login')]")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.web_util.send_keys_to_element(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.web_util.send_keys_to_element(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.web_util.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        ERROR_MESSAGE = (By.XPATH, "//p[contains(.,'Invalid credentials')]")
        return self.web_util.get_text_from_element(ERROR_MESSAGE)
