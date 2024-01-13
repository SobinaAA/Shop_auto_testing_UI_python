import time
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base import Base

class CatDryFeedPageAll(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    price_filter = '//div[@class="CatalogFiltersBlock_content__5SFm9"]/div[6]'
    weight_filter = '//div[@class="CatalogFiltersBlock_content__5SFm9"]/div[7]'
    age_filter = '//div[@class="CatalogFiltersBlock_content__5SFm9"]/div[2]'
    min_price_slider = '(//span[@data-index="0"])[1]'
    max_price_slider = '(//span[@data-index="1"])[1]'
    min_weight_slider = '(//span[@data-index="0"])[2]'
    max_weight_slider = '(//span[@data-index="1"])[2]'
    adult_value_filter = '(//div[@class="CheckboxGroupFilter_container__I+CQW"])[2]/label[1]'
    my_item_cart = '(//button[@data-testid="button"])[2]'
    cart_link = '//a[@title="Корзина"]'

    # Getters
    def get_price_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_weight_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.weight_filter)))

    def get_age_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.age_filter)))

    def get_min_price_slider(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.min_price_slider)))

    def get_max_price_slider(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.max_price_slider)))

    def get_min_weight_slider(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.min_weight_slider)))

    def get_max_weight_slider(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.max_weight_slider)))

    def get_adult_value_filter(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.adult_value_filter)))

    def get_my_item_cart(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.my_item_cart)))

    def get_cart_link(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.cart_link)))


    # Actions
    def click_cart_link(self):
        self.get_cart_link().click()
        print('Click cart link.')

    def click_price_filter(self):
        self.get_price_filter().click()
        print('Click price filter.')

    def click_weight_filter(self):
        self.get_weight_filter().click()
        print('Click weight filter.')

    def click_age_filter(self):
        self.get_age_filter().click()
        print('Click age filter.')

    def click_adult_value_filter(self):
        self.get_adult_value_filter().click()
        print('Click adult age.')

    def click_my_item_cart(self):
        self.get_my_item_cart().click()
        print('Click Royal Canin.')

    def increase_min_price(self, value_min):
        self.close_ad_down_bonuses()
        action_0 = ActionChains(self.driver)
        action_0.click_and_hold(self.get_min_price_slider()).move_by_offset(value_min,
                                                                            0).release().perform()  # зажали и тянем, двигаем,

    def decrease_max_price(self, value_max):
        action_1 = ActionChains(self.driver)
        action_1.click_and_hold(self.get_max_price_slider()).move_by_offset(value_max,
                                                                            0).release().perform()  # зажали и тянем, двигаем,

    def increase_min_weight(self, value_min):
        action_0 = ActionChains(self.driver)
        action_0.click_and_hold(self.get_min_weight_slider()).move_by_offset(value_min,
                                                                             0).release().perform()  # зажали и тянем, двигаем,

    def decrease_max_weight(self, value_max):
        action_1 = ActionChains(self.driver)
        action_1.click_and_hold(self.get_max_weight_slider()).move_by_offset(value_max,
                                                                             0).release().perform()  # зажали и тянем, двигаем,

    # Methods
    def appoint_price(self, value_min, value_max):
        self.close_all_window_widget()
        self.close_ad_down_bonuses()
        try:
            self.click_price_filter()
        except TimeoutException as exception:
            self.driver.refresh()
            time.sleep(3)
            self.close_ad_down_bonuses()
            self.close_all_window_widget()
            self.click_price_filter()
        time.sleep(10)
        self.increase_min_price(value_min)
        time.sleep(10)
        self.decrease_max_price(value_max)

    def appoint_weight(self, value_min, value_max):
        try:
            self.click_weight_filter()
        except TimeoutException as exception:
            self.close_all_window_widget()
            self.close_ad_down_bonuses()
            self.click_weight_filter()
        time.sleep(10)
        self.increase_min_weight(value_min)
        time.sleep(10)
        self.decrease_max_weight(value_max)
        time.sleep(10)

    def appoint_age(self):
        try:
            self.click_age_filter()
        except (TimeoutException, ElementClickInterceptedException) as exception:
            self.driver.refresh()
            self.close_all_window_widget()
            actions = ActionChains(self.driver)
            actions.move_to_element(self.get_age_filter()).click().perform()
            self.click_age_filter()
        time.sleep(10)
        self.click_adult_value_filter()

    def choose_feed(self):
        try:
            self.click_my_item_cart()
        except (TimeoutException, ElementClickInterceptedException) as exception:
            self.driver.refresh()
            self.close_all_window_widget()
            actions = ActionChains(self.driver)
            actions.move_to_element(self.get_my_item_cart()).click().perform()
            self.click_my_item_cart()
        time.sleep(10)

    def to_write_filters_values(self):
        values = [108, 12644, 0.2, 18]
        values[0] = float(self.get_min_price_slider().get_attribute('aria-valuenow'))
        values[1] = float(self.get_max_price_slider().get_attribute('aria-valuenow'))
        values[2] = float(self.get_min_weight_slider().get_attribute('aria-valuenow'))/1000
        values[3] = float(self.get_max_weight_slider().get_attribute('aria-valuenow'))/1000
        return values

    def go_to_cart(self):
        self.click_cart_link()
