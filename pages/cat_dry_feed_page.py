import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base import Base


class CatDryFeedPage(Base):
    # Locators
    a_view_all = '//div[@class="categories-wrapper"]/ul/li[1]/div[1]/a[1]'

    # Getters
    def get_a_view_all(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.a_view_all)))

    # Actions
    def click_a_view_all(self):
        self.get_a_view_all().click()
        print('Click button to view all products in category.')

    # Methods
    def choose_feed(self): #Попытка кликнуть на кнопку для просмотра всех товаров категории
        self.close_all_window_widget()
        self.close_ad_down_bonuses()
        try:
            self.click_a_view_all()
        except TimeoutException as exception: #Если возникают какие-то проблемы, обновление страницы и закрытие баннеров
            self.driver.refresh()
            time.sleep(5)
            self.close_all_window_widget()
            self.close_ad_down_bonuses()
            self.click_a_view_all()
        time.sleep(5)
        self.assert_url('https://www.petshop.ru/catalog/cats/syxkor/all/') #Проверяем, туда ли перешли по ссылке
