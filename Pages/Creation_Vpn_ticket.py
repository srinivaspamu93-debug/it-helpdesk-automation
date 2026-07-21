from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sign_in import Sign_in

class Creation_ticket:
    def __init__ (self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

    def provide_input(self,input):
        click_button_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/form/input')))
        click_button_input.send_keys(input)
        send_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='chat-send-button']"))
        )
        self.driver.execute_script("arguments[0].click();", send_button)
        # send_button.click()


    def ticket(self, login_url, email, password, inputs):
        login = Sign_in(self.driver)
        login.login(login_url,email,password)

        # new_chat_input= self.driver.find_element(
        #     By.XPATH,'//*[@id="root"]/div/div/main/div/div[2]/div[1]/button')
        # new_chat_input.click()
        for input in inputs:
            self.provide_input(input)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div[11]/div/div[2]/div[2]')))




