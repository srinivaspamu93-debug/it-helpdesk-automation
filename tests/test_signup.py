import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import allure
from Pages.P01_SignUp import SignUp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("User Registration")
class Test_register:
    @allure.story("Successful User Registration")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_up_success (self, driver):
        sign = SignUp(driver)
        reg_url = "https://helpdesk-bot-17.emergent.host/register"
        # Using a potentially new employee ID and email to avoid conflict
        import random
        rand_id = str(random.randint(1000, 9999))
        employee_id = rand_id
        full_name = "johnson"
        email = f"automation.user{rand_id}@example.com"
        password = "12345678"
        sign.register(reg_url, employee_id, full_name, email, password)
        
        # Wait for URL to change from register page
        WebDriverWait(driver, 10).until(EC.url_changes(reg_url))

        allure.attach(driver.get_screenshot_as_png(), name="signup_failure", attachment_type=allure.attachment_type.PNG)
        
        assert "register" not in driver.current_url.lower(), f"signup failed, still on signup page:{driver.current_url}"

    @allure.story("Failed User Registration")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sign_up_failed(self, driver):
            sign = SignUp(driver)
            reg_url = "https://helpdesk-bot-17.emergent.host/register"
            employee_id = "153"
            full_name = "johson"
            email = "automation.user3@example.com" # Already exists
            password = "12345678"
            sign.register(reg_url, employee_id, full_name, email, password)
            assert "register" in driver.current_url.lower(), "Should still be on the register page after failed registration"

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    sign_up = SignUp(driver)
    reg_url = "https://helpdesk-bot-17.emergent.host/register"
    sign_up.register(reg_url, "123", "John Doe", "john@example.com", "password")


