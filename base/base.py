import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class Base():
    def __init__(self, driver):
        self.driver = driver

    # locators
    button_close_left_widget = '//button[@class="TutoringEcoTooltip_button__zhTqX"]'
    button_close_widget = '//button[@class="widget__close"]'
    button_cookies = '//button[@class ="CookieInformer_button__hROKN"]'
    button_close_chat = '//jdiv[@class ="closeIcon_e25f"]'
    iframe_path = '//iframe[@id="fl-679776"]'
    iframe_up_path = '//iframe[@id="fl-615140"]'
    iframe_all_window = '//iframe[@id="fl-755090"]'  #Сервис Подели
    iframe_all_window_with_cat = '//iframe[@id="fl-679778"]' #Кошка на шарах

    # Getters
    def get_button_close_left_widget(self):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.button_close_left_widget)))

    # Methods
    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url = ' + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word!")

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        self.driver.save_screenshot('../screen/screenshot_' + str(now_date) + '.png')

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good url!")

    def close_cookies(self):
        try:
            element = self.driver.find_element(By.XPATH, self.button_cookies)
            element.click()
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print('Cant find cookies widget.')

    def close_chat(self):
        try:
            element = self.driver.find_element(By.XPATH, self.button_close_chat)
            element.click()
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print('Cant find chat widget.')

    def close_left_up_widget(self):
        try:
            self.get_button_close_left_widget().click()
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print('Cant find annoying widget with ad (left-up corner).')

    def close_ad_up_bonuses(self):
        try:
            iframe = self.driver.find_element_by_xpath(self.iframe_up_path)
            self.driver.switch_to.frame(iframe)
            element = self.driver.find_element(By.XPATH, self.button_close_widget)
            element.click()
            self.driver.switch_to.default_content()
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print('Cant find annoying widget with ad (up).')

    def close_ad_down_bonuses(self):
        try:
            iframe = self.driver.find_element_by_xpath(self.iframe_path)
            self.driver.switch_to.frame(iframe)
            element = self.driver.find_element(By.XPATH, self.button_close_widget)
            element.click()
            self.driver.switch_to.default_content()
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print('Cant find annoying widget with ad (left-down corner).')

    def close_all_window_widget(self): #закрывает два типа виджета на все окно
        try:
            iframe = self.driver.find_element_by_xpath(self.iframe_all_window)
            self.driver.switch_to.frame(iframe)
            element = self.driver.find_element(By.XPATH, self.button_close_widget)
            element.click()
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print('Cant find annoying all-window widget with ad.')
            self.driver.switch_to.default_content()
        try:
            iframe = self.driver.find_element_by_xpath(self.iframe_all_window_with_cat)
            self.driver.switch_to.frame(iframe)
            element = self.driver.find_element(By.XPATH, self.button_close_widget)
            element.click()
        except (NoSuchElementException, ElementNotInteractableException) as exception:
            print('Cant find annoying all-window widget with ad.')
            self.driver.switch_to.default_content()

