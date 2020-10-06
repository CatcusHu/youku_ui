import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


class Base:
    
    MAX_WAIT = 10

    def __init__(self, driver, timeout=10, timesleep=0.5):
        self.driver = driver
        self.timeout = timeout
        self.timesleep = timesleep

    def find_element(self, locator):
        if not isinstance(locator, tuple):
            print("需要传入元组类型")
        else:
            element = WebDriverWait(self.driver, self.timeout, self.timesleep).until(
                EC.presence_of_element_located(locator))
            return element

    def find_elements(self, locator):
        if not isinstance(locator, tuple):
            print("需要传入元组类型")
        else:
            try:
                elements = WebDriverWait(self.driver, self.timeout, self.timesleep).until(
                    EC.presence_of_all_elements_located(locator))
                return elements
            except:
                return []

    def send_words(self, locator, text=""):
        return self.find_element(locator).send_keys(text)

    def click(self, locator):
        return self.find_element(locator).click()

    def wait(self, fn):
        """等待时间"""
        start_time = time.time()
        while True:
            try:
                return fn()
            except (WebDriverException, AssertionError) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)

# if __name__ == "__main__":
#     driver = webdriver.Firefox()
#     driver.get("https://www.mgtv.com/")
#     base = Base(driver)
