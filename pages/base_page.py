from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.data import BASE_URL
import time

class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        )
    
    def lose(self, locator):
        return self.wait.until(
            expected_conditions.invisibility_of_element_located(locator)
        )
    def find_clickable(self, locator):
        return self.wait.until(
            expected_conditions.element_to_be_clickable(locator)
        )

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_clickable(locator).click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def loading(self, locator):
        self.find(locator)
        self.lose(locator)
    
    def drag_and_drop_js(self, source, target):
        source_element = self.find(source)
        target_element = self.find(target)
        js_code = (
            "var source = arguments[0], target = arguments[1]; "
            "var dragStartEvent = new DragEvent('dragstart', {bubbles: true, cancelable: true}); "
            "source.dispatchEvent(dragStartEvent); "
            "var dragOverEvent = new DragEvent('dragover', {bubbles: true, cancelable: true}); "
            "target.dispatchEvent(dragOverEvent); "
            "var dropEvent = new DragEvent('drop', {bubbles: true, cancelable: true}); "
            "target.dispatchEvent(dropEvent); "
            "var dragEndEvent = new DragEvent('dragend', {bubbles: true, cancelable: true}); "
            "source.dispatchEvent(dragEndEvent);"
        )
        self.driver.execute_script(js_code, source_element, target_element)
  
    def сollect_states(self, locator, duration, delay):
        i = 0
        result = set()
        while i <= duration:
            result |= ({order.text for order in self.driver.find_elements(*locator)})
            time.sleep(delay)
            i += delay
        return result