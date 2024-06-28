from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class WebUtilities:
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_strategy, locator_value, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator_strategy, locator_value))
            )
        except TimeoutException:
            raise TimeoutException(f"Timed out waiting for element {locator_value}.")

    def wait_for_element_to_be_clickable(self, locator_strategy, locator_value, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((locator_strategy, locator_value))
            )
        except TimeoutException:
            raise TimeoutException(f"Timed out waiting for element {locator_value} to be clickable.")

    def send_keys_to_element(self, element_locator, keys, timeout=None):
        element = self.wait_for_element(*element_locator, timeout)
        element.send_keys(keys)

    def click_element(self, element_locator, timeout=None):
        element = self.wait_for_element_to_be_clickable(*element_locator, timeout)
        element.click()

    def get_text_from_element(self, element_locator, timeout=None):

        element = self.wait_for_element(*element_locator, timeout)
        return element.text

    def wait_for_element_to_be_invisible(self, locator_strategy, locator_value, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element((locator_strategy, locator_value))
            )
        except TimeoutException:
            raise TimeoutException(f"Timed out waiting for element {locator_value} to be invisible.")

    def wait_for_element_to_be_not_present(self, locator_strategy, locator_value, timeout=None):
        timeout = timeout or self.DEFAULT_TIMEOUT
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.staleness_of(self.driver.find_element(locator_strategy, locator_value))
            )
        except TimeoutException:
            raise TimeoutException(f"Timed out waiting for element {locator_value} to be not present.")
