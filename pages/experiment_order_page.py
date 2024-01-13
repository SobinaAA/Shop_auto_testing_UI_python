import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base import Base


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://www.petshop.ru/catalog/cats/syxkor/kotyata_do_1_goda_beremennye_koshki/dlya_kotyat_s_momenta_operacii_do_12_mes_kitten_sterilized_16789/?oid=505113'

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
    enter_button = '//button[@type="submit"]'

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
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email_label)))

    def get_email_label(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pass_field)))

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
        self.get_code_field().send_keys('makkuropip@gmail.com')
        print('Enter email.')

    def enter_pass(self):
        self.get_pass_field().send_keys('zxc666666')
        print('Enter password.')
        time.sleep(10)

    # Methods
    # def confirm_phone_number(self):
    #     self.get_current_url()
    #     self.enter_phone('9030806479')
    #     time.sleep(5)
    #     self.click_button_enter_msg()
    #     time.sleep(15)
    #     code = input('Введите код:')
    #     time.sleep(15)
    #     self.enter_code(code)
    #     time.sleep(20)

    def enter_with_email(self):
        self.click_email_button()
        time.sleep(5)
        self.click_email_label()
        time.sleep(10)
        self.enter_email()
        self.click_pass_label()
        time.sleep(10)
        self.enter_pass()
        time.sleep(5)
        self.click_enter_button()

    def finish_order(self):
        self.click_date_button()
        time.sleep(10)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_button_payment_method()).click().perform()
        self.click_button_payment_method()
        #self.click_final_button() #В проекте не будем заказывать по-настоящему
        print('Кнопочку для заказа нашли, но нажимать не станем: ' + self.get_final_button().text)

    def test_experiment(self):
        self.click_email_button()
        time.sleep(5)
        self.click_email_label()
        self.enter_email()
        self.click_pass_label()
        self.enter_pass()
        time.sleep(5)
        self.click_enter_button()
        self.click_date_button()
        time.sleep(10)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_button_payment_method()).click().perform()
        self.click_button_payment_method()
        # self.click_final_button() #В проекте не будем заказывать по-настоящему
        print('Кнопочку для заказа нашли, но нажимать не станем: ' + self.get_final_button().text)








