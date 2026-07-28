import sys
# import os
import os
import allure
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P09_HardwareRequest import HardwareRequestTicket

@allure.feature("Helpdesk Workflows")
class TestHardwareRequest:
    @allure.story("Hardware Request")
    @allure.severity(allure.severity_level.NORMAL)
    def test_hardware_request_success(self, driver):
        hr = HardwareRequestTicket(driver)
        inputs = ["Need new monitor", "27 inch 4K", "Medium", "Current monitor is flickering"]
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email = 'automation.user3@example.com'
        password = '12345678'
        hr.create_ticket(login_url, email, password, inputs)
