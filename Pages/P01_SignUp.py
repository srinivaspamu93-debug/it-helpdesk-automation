import allure
from Pages.Basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUp(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(driver, 10)
        super().__init__(driver)

    @allure.step("Register new user with employee ID: {employee_id}")
    def register(self, reg_url, employee_id, full_name, email, password):
        self.driver.get(reg_url)
        employee_id_input = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/form/div[3]/div[1]/input')))
        employee_id_input.send_keys(employee_id)
        full_name_input = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/form/div[3]/div[2]/input')))
        full_name_input.send_keys(full_name)
        email_input = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/form/div[3]/div[3]/input')))
        email_input.send_keys(email)
        password_input = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/form/div[3]/div[4]/input')))
        password_input.send_keys(password)
        click_button_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#root > div > div > form > button')))
        click_button_input.click()




