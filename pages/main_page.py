import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base import Base


class MainPage(Base):
    url = 'https://www.petshop.ru/'

    # Locators
    dry_cat_category = '(//ul[@class="left-list left-list_column-three"])[2]/li[2]/a'
    button_change_location = '//button[@class="City_city__ykrSq undefined action-header-city"]'
    ekb_city = '(//span[text()="Екатеринбург"])[2]'

    # Getters
    def get_dry_cat_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dry_cat_category)))

    def get_button_change_location(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_change_location)))

    def get_ekb_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ekb_city)))

    # Actions
    def click_dry_cat_category(self):
        self.get_dry_cat_category().click()
        print('Click dry feed category for cats in the left menu.')

    def click_button_change_location(self):
        self.get_button_change_location().click()
        print('Click to change my location.')

    def click_ekb_city(self):
        self.get_ekb_city().click()
        print('Click to select Ekb.')

    def click_button_close_widget(self):
        self.get_ekb_city().click()
        print('Click to close widget.')

    # Methods
    def change_location(self): #Кликаем по окну для смены локации на Екб
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.close_left_up_widget()
        self.click_button_change_location()
        self.click_ekb_city()
        time.sleep(3)
        self.close_cookies()

    def select_category_dry_cat(self): #ВЫбор категории сухого корма
        self.close_ad_up_bonuses()
        time.sleep(5)
        self.close_cookies()
        self.click_dry_cat_category()

