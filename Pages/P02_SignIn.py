import allure
from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignIn(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        super().__init__(driver)


    @allure.step("Login with email: {email}")
    def login(self, login_url, email, password):
        self.driver.get(login_url)
        email_input = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[2]/form/div[2]/div[1]/input')))
        email_input.send_keys(email)
        password_input = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[2]/form/div[2]/div[2]/input')))
        password_input.send_keys(password)
        click_button_input = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[2]/form/button')))
        click_button_input.click()



