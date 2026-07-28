import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.P02_SignIn import SignIn
from Pages.Basepage import BasePage

class WindowsPasswordTicket(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        super().__init__(driver)

    @allure.step("Start workflow")
    def start_workflow(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="workflow-windows_password_reset"]')))
        button.click()

    @allure.step("Provide input: {input_text}")
    def provide_input(self, input_text):
        chat_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="chat-input"]')))
        chat_input.send_keys(input_text)
        send_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="chat-send-button"]')))
        self.driver.execute_script("arguments[0].click()", send_button)

    @allure.step("Resolve Windows password issue")
    def password_issue(self, login_url, email, password, inputs):
        login = SignIn(self.driver)
        login.login(login_url, email, password)
        self.start_workflow()
        for input_text in inputs:
            self.provide_input(input_text)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    w_password = WindowsPasswordTicket(driver)
    input1 = "johnson456"
    input2 = "locked now"
    input3 = "yes. successfully logged in"
    input4 = "company's laptop"
    login_url = 'https://helpdesk-bot-17.emergent.host/login'
    email = 'automation.user3@example.com'
    password = '12345678'
    inputs = [input1, input2, input3, input4]
    w_password.password_issue(login_url, email, password, inputs)