import time
from selenium import webdriver
import pytest
from pages.main_page import MainPage
from pages.cat_dry_feed_page import CatDryFeedPage
from pages.cat_dry_feed_page_all import CatDryFeedPageAll
from pages.cart_page import CartPage
from pages.order_page import OrderPage


def test_buy_feed():
    print('Start test to buy some food for my cat!')
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path='../Driver/chromedriver.exe', chrome_options=chrome_options)

    main_shop_page = MainPage(driver) #создали объект класса главной страницы
    main_shop_page.change_location() #вызвали метод смены локации на Екб
    main_shop_page.select_category_dry_cat() #вызвали метод выбора категории корма

    cat_dry = CatDryFeedPage(driver) #создали объект класса страницы с сухим кормом
    cat_dry.choose_feed() #вызвали метод выбора категории корма
    time.sleep(5)

    cat_dry_filter = CatDryFeedPageAll(driver) #создали объект класса страницы с фильтрами
    cat_dry_filter.appoint_price(115, - 15) #вызвали метод изменения хначений фильтра стоимости
    time.sleep(20)
    cat_dry_filter.appoint_weight(70, - 50) #вызвали метод изменения хначений фильтра веса
    time.sleep(10)
    cat_dry_filter.appoint_age() #вызвали метод изменения возрастной категории
    time.sleep(10)
    control_values = cat_dry_filter.to_write_filters_values() #вызвали метод, который записывает в переменную значения фильтров
    print(control_values)
    cat_dry_filter.choose_feed() #вызвали метод выбора конкретного корма
    cat_dry_filter.go_to_cart() #вызвали метод перехода в корзину

    cart = CartPage(driver) #создали объект класса страницы корзины
    cart.control_parameters(control_values) #вызвали метод проверки соответствия параметров корма значениям фильтров
    cart.make_order() #вызвали метод перехода на страницу заказа

    final = OrderPage(driver) #создали объект класса страницы с заказом
    final.enter_with_email() #ызвали метод автоиизации по email
    final.finish_order() #ызвали метод завершения заказа (дата, метод оплаты, клик на "Заказать")
    print('Test is finished!')

