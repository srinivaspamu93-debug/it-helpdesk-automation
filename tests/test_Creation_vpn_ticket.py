import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P05_VPNTicket import VpnTicket

@allure.feature("Helpdesk Workflows")
class TestCreationVpnTicket:
    @allure.story("VPN Connectivity")
    @allure.severity(allure.severity_level.NORMAL)
    def test_creation_ticket_success(self, driver):
        ct = VpnTicket(driver)
        input1 = "Cisco Anyconnect"
        input2 = "VPN Failure"
        input3 = "in the office"
        input4 = "office wifi"
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email = 'automation.user3@example.com'
        password = '12345678'
        inputs = [input1, input2, input3, input4]
        ct.ticket(login_url, email, password, inputs)

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    creation_ticket = VpnTicket(driver)
    input1 = "Cisco Anyconnect"
    input2 = "VPN Failure"
    input3 = "in the office"
    input4 = "office wifi"
    login_url = 'https://helpdesk-bot-17.emergent.host/login'
    email = 'automation.user3@example.com'
    password = '12345678'
    inputs = [input1, input2, input3, input4]
    creation_ticket.ticket(login_url, email, password, inputs)
