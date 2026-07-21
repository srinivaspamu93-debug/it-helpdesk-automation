from selenium.webdriver.common.by import By
from selenium import webdriver
class Sign_up:
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window()

    def signup(self,driver):
        self.driver = driver

    def register(self,Reg_url,employee_id,full_name,email,password):
        self.driver.get(Reg_url)
        employee_id_input = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div[3]/div[1]/input')
        employee_id_input.send_keys(employee_id)
        full_name_input= self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div[3]/div[2]/input')
        full_name_input.send_keys(full_name)
        email_input= self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div[3]/div[3]/input')
        email_input.send_keys(email)
        password_input= self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div/form/div[3]/div[4]/input')
        password_input.send_keys(password)
        click_button_input= self.driver.find_element(By.CSS_SELECTOR,'#root > div > div > form > button')
        click_button_input.click()
