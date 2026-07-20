from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sign_in:
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

    def signin(self,driver):
        self.driver = driver

    def login(self, login_url, email, password):
        self.driver.get(login_url)
        # time.sleep(5)
        email_input =self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/form/div[2]/div[1]/input')
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/form/div[2]/div[2]/input')
        password_input.send_keys(password)
        # time.sleep(5)
        click_button_input = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/form/button')
        click_button_input.click()


