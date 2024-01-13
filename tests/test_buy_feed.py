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
    driver = webdriver.Chrome(executable_path='C:\\Py\\Resourse\\chromedriver.exe', chrome_options=chrome_options)

    main_shop_page = MainPage(driver)
    main_shop_page.change_location()
    main_shop_page.select_category_dry_cat()

    cat_dry = CatDryFeedPage(driver)
    cat_dry.choose_feed()
    time.sleep(5)

    cat_dry_filter = CatDryFeedPageAll(driver)
    cat_dry_filter.appoint_price(115, - 15)
    time.sleep(20)
    cat_dry_filter.appoint_weight(70, - 50)
    time.sleep(10)
    cat_dry_filter.appoint_age()
    time.sleep(10)
    control_values = cat_dry_filter.to_write_filters_values()
    print(control_values)
    cat_dry_filter.choose_feed()
    cat_dry_filter.go_to_cart()

    cart = CartPage(driver)
    cart.control_parameters(control_values)
    cart.make_order()

    final = OrderPage(driver)
    final.enter_with_email()
    final.finish_order()
    print('Test is finished!')




