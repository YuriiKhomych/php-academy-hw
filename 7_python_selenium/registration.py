from selenium import webdriver
import os

chromedriver = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver")
driver = webdriver.Chrome(chromedriver)

driver.get("https://www.work.ua/")

enter = driver.find_element_by_partial_link_text("Войти").click()
registration = driver.find_element_by_partial_link_text("Зарегистрироваться").click()
first_name = driver.find_element_by_id("first_name").send_keys("Vasya")
last_name = driver.find_element_by_xpath("//input[@name='last_name']").send_keys("Pupkin")
email = driver.find_element_by_xpath("//input[@type='email']").send_keys("test@gmail.com")
password = driver.find_element_by_xpath("//input[@name='user_pwd']").send_keys("test")
submit = driver.find_element_by_xpath("//input[@type='submit']").click()


