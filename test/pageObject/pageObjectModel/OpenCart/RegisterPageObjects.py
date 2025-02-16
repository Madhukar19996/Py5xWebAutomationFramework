import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


from selenium import webdriver
from selenium.webdriver.common.by import By

class RegisterPage:

    #Lacotors
    txtbox_firstname_id="input-firstname"
    txtbox_lastname_id="input-lastname"
    txtbox_email_id="input-email"
    txtbox_password_id="input-password"
    # txtbox_info_xpath="//h5[normalize-space()='Information']"
    policy_button=privacy_policy_button_xpath="//input[@name='agree']"
    continue_button=continue_button_xpath=("//button[normalize-space()='Continue']")




    # constructor
    def __init__(self, driver):
        self.driver = driver



    # action methods
    def setFistName(self, firstname):
        firstnametxt = self.driver.find_element(By.ID, self.txtbox_firstname_id)
        firstnametxt.clear()
        firstnametxt.send_keys(firstname)

    def setLastName(self, lastname):
        lastnametxt = self.driver.find_element(By.ID, self.txtbox_lastname_id)
        lastnametxt.clear()
        lastnametxt.send_keys(lastname)

    def setEmail(self, email,):
        emailtxt = self.driver.find_element(By.ID, self.txtbox_email_id)
        emailtxt.clear()
        emailtxt.send_keys(email)

    def setPassword(self, pwd):
        passwordtxt = self.driver.find_element(By.ID, self.txtbox_password_id)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)

    # def clickInfo(self):
    #     self.driver.find_element(By.XPATH, self.txtbox_info_xpath).click()



    def clickPrivacyPolicyButton (self):

        self.driver.execute_script("document.querySelector('button.btn.btn-primary').scrollIntoView({behavior:'smooth'})")
        # self.driver.execute_script("arguments[0].scrollIntoView();", self.policy_button)
        time.sleep(2)

        self.driver.find_element(By.XPATH,self.policy_button).click()
    # #     # flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
    #     self.driver.execute_script("arguments[0].scrollIntoView();",self.policy_button).click()

    def clickContinueButton (self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()