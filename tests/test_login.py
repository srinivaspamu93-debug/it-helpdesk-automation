import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P02_SignIn import SignIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("User Authentication")
class TestLogin:
    @allure.story("Successful Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self, driver):
        login = SignIn(driver)
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email ='automation.user3@example.com'
        password = '12345678'
        login.login(login_url, email, password)
        
        # Wait for URL to change from login page
        WebDriverWait(driver, 10).until(EC.url_changes(login_url))
        
        assert "login" not in driver.current_url.lower(), f"Login failed, still on login page: {driver.current_url}"

    @allure.story("Failed Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_failed(self, driver):
        login = SignIn(driver)
        login_url = 'https://helpdesk-bot-17.emergent.host/login'
        email ='automation.user4@example.com'
        password = '12345678'
        login.login(login_url, email, password)
        # For failed login, we expect to stay on the login page
        assert "login" in driver.current_url.lower(), "Should still be on the login page after failed login"


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    sign_in = SignIn(driver)
    login_url = 'https://helpdesk-bot-17.emergent.host/login'
    email ='automation.user3@example.com'
    password = '12345678'
    sign_in.login(login_url,email,password)