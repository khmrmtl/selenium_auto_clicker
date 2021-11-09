from selenium import webdriver
import time



CHROME_DRIVER = "C:\Development\chromedriver"
WEBSITE_URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

driver.get(WEBSITE_URL)

cookie = driver.find_element_by_css_selector("#cookie")


def cookie_click():
    timeout = time.time() + 5
    while not time.time() > timeout:
        cookie.click()
    print(10)



while True:
    cookie_click()
    product_price = driver.find_elements_by_css_selector("#rightPanel #store b")
    product_price.pop()
    products = driver.find_elements_by_css_selector("#rightPanel div")
    prices = [int(product.text.split(" - ")[1].replace(',', "")) for product in product_price]
    buy_index = 0

    for price in range(0, len(prices)):
        money = driver.find_element_by_css_selector("#money")
        if int(money.text.replace(',', "")) > prices[price]:
            buy_index = price

    products[buy_index].click()
    print(f"click {buy_index}")
