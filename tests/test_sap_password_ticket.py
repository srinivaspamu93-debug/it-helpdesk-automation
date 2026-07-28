import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P03_SAPPassword import SapPasswordTicket

@allure.feature("Helpdesk Workflows")
class TestSapPasswordTicket:
    @allure.story("SAP Password Reset")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sap_password_ticket_success(self, driver):
        sap = SapPasswordTicket(driver)
        inputs = ["johnson456", "locked now", "yes. successfully logged in", "company's laptop"]
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email = 'automation.user3@example.com'
        password = '12345678'
        sap.sap_login(login_url, email, password, inputs)

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    sap_password = SapPasswordTicket(driver)
    inputs = ["johnson456", "locked now", "yes. successfully logged in", "company's laptop"]
    login_url = 'https://helpdesk-bot-17.emergent.host/login'
    email = 'automation.user3@example.com'
    password = '12345678'
    sap_password.sap_login(login_url, email, password, inputs)