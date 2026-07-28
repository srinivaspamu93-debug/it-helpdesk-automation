import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P06_InternetConnectivity import InternetConnectivityTicket

@allure.feature("Helpdesk Workflows")
class TestInternetConnectivity:
    @allure.story("Internet Connectivity")
    @allure.severity(allure.severity_level.NORMAL)
    def test_internet_connectivity_success(self, driver):
        ic = InternetConnectivityTicket(driver)
        inputs = ["No internet in building B", "Floor 2", "High", "Ethernet port not working"]
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email = 'automation.user3@example.com'
        password = '12345678'
        ic.create_ticket(login_url, email, password, inputs)
