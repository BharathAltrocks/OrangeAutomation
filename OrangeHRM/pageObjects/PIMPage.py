from selenium.webdriver.common.by import By

from utils.WebUtilities import WebUtilities


class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.web_util = WebUtilities(driver)
        self.PIM_MENU = (By.XPATH, "//span[text()='PIM']")
        self.ADD_BUTTON = (By.XPATH, "//button[@type='button'][contains(.,'Add')]")
        self.FIRST_NAME = (By.XPATH, "//input[@name='firstName']")
        self.MIDDLE_NAME = (By.XPATH, "//input[@name='middleName']")
        self.LAST_NAME = (By.XPATH, "//input[@name='lastName']")
        self.EMPLOYEE_ID = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.SAVE_BUTTON = (By.XPATH, "//button[contains(.,'Save')]")
        self.EMPLOYEE_ID_SEARCH = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.SEARCH_BUTTON = (By.XPATH, "//button[contains(.,'Search')]")
        self.EDIT_ICON = (By.XPATH, "//i[@class='oxd-icon bi-pencil-fill']")
        self.MALE_RADIO_BUTTON = (By.XPATH, "//label[contains(.,'Male')]")
        self.LOADER = (By.CLASS_NAME, "oxd-form-loader")

    def click_pim_side_menu(self):
        self.web_util.click_element(self.PIM_MENU)

    def click_add_button(self):
        self.web_util.click_element(self.ADD_BUTTON)

    def enter_firstname(self, firstname):
        self.web_util.send_keys_to_element(self.FIRST_NAME, firstname)

    def enter_middle_name(self, middlename):
        self.web_util.send_keys_to_element(self.MIDDLE_NAME, middlename)

    def enter_last_name(self, lastname):
        self.web_util.send_keys_to_element(self.LAST_NAME, lastname)

    def enter_employee_id(self, employee_id):
        self.web_util.send_keys_to_element(self.EMPLOYEE_ID, employee_id)

    def click_save_button(self):
        self.web_util.click_element(self.SAVE_BUTTON)

    def get_error_message(self):
        ERROR_MESSAGE = (By.XPATH, "//span[contains(@class, 'error')]")
        return self.web_util.get_text_from_element(ERROR_MESSAGE)

    def enter_employee_id_in_search(self, employee_id):
        self.web_util.send_keys_to_element(self.EMPLOYEE_ID_SEARCH, employee_id)

    def click_search_button(self):
        self.web_util.click_element(self.SEARCH_BUTTON)

    def click_edit_icon(self):
        self.web_util.click_element(self.EDIT_ICON)

    def click_male_radio_button(self):
        self.web_util.wait_for_element_to_be_invisible(*self.LOADER, timeout=20)
        self.web_util.click_element(self.MALE_RADIO_BUTTON)
