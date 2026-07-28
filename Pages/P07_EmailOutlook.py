import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.P02_SignIn import SignIn
from Pages.Basepage import BasePage

class EmailOutlookTicket(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        super().__init__(driver)

    @allure.step("Start workflow")
    def start_workflow(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="workflow-email_outlook"]')))
        button.click()

    @allure.step("Provide input: {input_text}")
    def provide_input(self, input_text):
        chat_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="chat-input"]')))
        chat_input.send_keys(input_text)
        send_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="chat-send-button"]')))
        self.driver.execute_script("arguments[0].click()", send_button)

    @allure.step("Create Email/Outlook ticket")
    def create_ticket(self, login_url, email, password, inputs):
        login = SignIn(self.driver)
        login.login(login_url, email, password)
        self.start_workflow()
        for input_text in inputs:
            self.provide_input(input_text)
