from selenium import webdriver

CHROME_DRIVER = "C:\Development\chromedriver"
WEBSITE_URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER)

driver.get(WEBSITE_URL)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Khmer")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Motal")
email = driver.find_element_by_name("email")
email.send_keys("shelbyspecter01@gmail.com")

button = driver.find_element_by_css_selector(".btn-primary")
button.click()



# driver.quit()