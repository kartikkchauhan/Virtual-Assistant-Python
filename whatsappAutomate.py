from selenium import webdriver
import time

try:
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    name = input('Enter the name of user or group : ')
    msg = input('Enter the message : ')

    input("Scan Qr code and hint enter")
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    while True:
        time.sleep(5)
        textbox = driver.find_element_by_class_name('_3uMse')
        textbox.send_keys(msg)
        driver.find_element_by_class_name('_1U1xa').click()

except Exception as e:
    print(e)