import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P04_WindowsPassword import WindowsPasswordTicket

@allure.feature("Helpdesk Workflows")
class TestWindowsPasswordTicket:
    @allure.story("Windows Password Reset")
    @allure.severity(allure.severity_level.NORMAL)
    def test_windows_password_ticket_success(self, driver):
        wp = WindowsPasswordTicket(driver)
        inputs = ["johnson456", "locked now", "yes. successfully logged in", "company's laptop"]
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email = 'automation.user3@example.com'
        password = '12345678'
        wp.password_issue(login_url, email, password, inputs)
