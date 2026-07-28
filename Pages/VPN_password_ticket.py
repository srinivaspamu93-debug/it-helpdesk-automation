from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.sign_in import Sign_in

class Creation_ticket:
    def __init__ (self,driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)

    def provide_input(self,input_text):
        click_button_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/form/input')))
        click_button_input.send_keys(input_text)
        send_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='chat-send-button']"))
        )
        self.driver.execute_script("arguments[0].click();", send_button)

    def ticket(self, login_url, email, password, inputs):
        login = Sign_in(self.driver)
        login.login(login_url,email,password)

        for input_text in inputs:
            self.provide_input(input_text)
        
        # Wait for some indication that the ticket process is finished if needed
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/main/div/div[2]/div[2]/div[11]/div/div[2]/div[2]')))

if __name__ == "__main__":
    driver = webdriver.Chrome()
    creation_ticket = Creation_ticket(driver)
    input1="vpn problem"
    input2="Cisco Anyconnect"
    input3="VPN Failure"
    input4="in the office"
    input5="office wifi"
    login_url = 'https://helpdesk-bot-17.emergent.host/login'
    email ='automation.user3@example.com'
    password = '12345678'
    inputs = [input1,input2,input3,input4,input5]
    creation_ticket.ticket(login_url, email, password, inputs)
