import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.P02_SignIn import SignIn

class VpnTicket(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        super().__init__(driver)

    @allure.step("Start workflow")
    def start_workflow(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="workflow-vpn_issues"]')))
        button.click()

    @allure.step("Provide input: {input_text}")
    def provide_input(self, input_text):
        chat_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="chat-input"]')))
        chat_input.send_keys(input_text)
        send_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="chat-send-button"]')))
        self.driver.execute_script("arguments[0].click()", send_button)

    @allure.step("Create VPN ticket")
    def ticket(self, login_url, email, password, inputs):
        login = SignIn(self.driver)
        login.login(login_url, email, password)
        self.start_workflow()
        for input_text in inputs:
            self.provide_input(input_text)
        
        # Wait for some indication that the ticket process is finished if needed
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div[11]/div/div[2]/div[2]')))


