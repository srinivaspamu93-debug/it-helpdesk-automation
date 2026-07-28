import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P07_EmailOutlook import EmailOutlookTicket

@allure.feature("Helpdesk Workflows")
class TestEmailOutlook:
    @allure.story("Email/Outlook Issue")
    @allure.severity(allure.severity_level.NORMAL)
    def test_email_outlook_success(self, driver):
        eo = EmailOutlookTicket(driver)
        inputs = ["Outlook keeps crashing", "john.doe@example.com", "Medium", "Reinstalled but same issue"]
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email = 'automation.user3@example.com'
        password = '12345678'
        eo.create_ticket(login_url, email, password, inputs)



