import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base import Base


class CartPage(Base):
    # Locators
    make_order_button = '//div[@class="FullCart_order_btn_wrap__gHX9x"]/button[1]'
    price = '(//span[@data-testid="Price__val"])[4]'
    weight = '//div[@class="CartTotal_weight__GaOFL"]'

    # Getters
    def get_make_order_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.make_order_button)))

    def get_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_weight(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.weight)))

    # Actions
    def click_make_order_button(self):
        self.get_make_order_button().click()
        print('Click button to make order.')

    # Methods
    def make_order(self): #Переход на страницу заказа
        time.sleep(5)
        self.get_screenshot()  # чтобы потом проверить, купили ли мы правильный корм
        self.get_current_url()
        time.sleep(4)
        self.click_make_order_button()

    def control_parameters(self, values): #Проверка соответствия параметров корма тем самым значениям фильтров со страницы с фильтрами
        time.sleep(5)
        assert values[1] > int(self.get_price().text.replace(' ', '')) > values[0]
        print('Price is correct for filter.')
        assert values[2] < float(self.get_price().text[:3]) < values[3]
        print('Weight is correct for filter.')
