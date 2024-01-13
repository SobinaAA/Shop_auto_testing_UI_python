import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base import Base


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    phone_field = '//input[@name="root_phone"]'
    button_msg = '//button[@type="submit"]'
    code_field = '//input[@data-testid="TextInput__input-empty"]'
    date_button = '(//div[@role="button"])[1]'
    button_payment_method = '(//div[@class="select-with-group_element SelectWithGroup_element__TjyzG SelectWithGroup_tile__uIv1s"])[7]'
    final_button = '(//span[@class="Button_button_content__Jhwto"])[2]'
    email_button = '//div[@class="OrderAuthorization_link_wrapper__c9sQk"]/button'
    email_field = '//input[@name="root_login"]'
    email_label = '(//label[@data-testid="TextInput__label"])[4]' #проба пера
    pass_label = '(//label[@data-testid="TextInput__label"])[5]'#проба пера
    pass_field = '//input[@name="root_password"]'
    enter_button = '(//button[@type="submit"])[2]'

    # Getters
    def get_phone_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_button_msg(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_msg)))

    def get_code_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.code_field)))

    def get_date_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.date_button)))

    def get_final_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.final_button)))

    def get_button_payment_method(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_payment_method)))

    def get_email_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_button)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_pass_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pass_field)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_email_label(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_label)))

    def get_pass_label(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pass_label)))

    # Actions
    def enter_phone(self, number):
        self.get_phone_field().send_keys(number)
        print('Enter phone number.')

    def click_button_enter_msg(self):
        self.get_button_msg().click()
        print('Click button to receive msg.')

    def click_date_button(self):
        self.get_date_button().click()
        print('Select date for order.')

    def click_button_payment_method(self):
        self.get_button_payment_method().click()
        print('Select payment method.')

    def click_email_label(self):
        self.get_email_label().click()
        print('-')

    def click_pass_label(self):
        self.get_pass_label().click()
        print('-')

    def click_final_button(self):
        self.get_final_button().click()
        print('Finish my order.')

    def click_email_button(self):
        self.get_email_button().click()
        print('Enter with email.')

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Entered with email.')

    def enter_code(self, code):
        self.get_code_field().send_keys(code)
        print('Enter code.')

    def enter_email(self):
        self.get_email_field().send_keys('******')
        print('Enter email.')

    def enter_pass(self):
        self.get_pass_field().send_keys('******')
        print('Enter password.')
        time.sleep(10)

    # Methods
    # def enter_with_email(self):   #Good method, but doesnt work
    #     self.click_email_button()
    #     time.sleep(5)
    #     self.enter_email()
    #     self.enter_pass()
    #     time.sleep(5)
    #     self.click_enter_button()

    def enter_with_email(self):
        self.click_email_button()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//input[@name="root_login"]').send_keys('makkuropip@gmail.com') #Too simple method, but works
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//input[@name="root_password"]').send_keys('gAmruv-7fyrfa-tugber') #Too simple method, but works
        time.sleep(5)
        self.click_enter_button()

    def finish_order(self):
        self.click_date_button()
        time.sleep(10)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_button_payment_method()).click().perform()
        self.click_button_payment_method()
        self.assert_word(self.get_final_button(), 'Оформить заказ')
        #self.click_final_button() # We will not make the order
        print('We found an order button on the page, it is clickable. The text from it was checked. We will not make the order!')







