import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P08_SoftwareInstallation import SoftwareInstallationTicket

@allure.feature("Helpdesk Workflows")
class TestSoftwareInstallation:
    @allure.story("Software Installation")
    @allure.severity(allure.severity_level.NORMAL)
    def test_software_installation_success(self, driver):
        si = SoftwareInstallationTicket(driver)
        inputs = ["Need Visual Studio Code", "For development project", "Low", "Approved by manager"]
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email = 'automation.user3@example.com'
        password = '12345678'
        si.create_ticket(login_url, email, password, inputs)
