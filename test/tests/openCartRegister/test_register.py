import time

from selenium import webdriver

from test.pageObject.pageObjectModel.OpenCart.RegisterPageObjects import RegisterPage
from selenium.webdriver.chrome.options import Options


class TestRegister:
  def test_register(self):

    # self.chrome_options = Options()
    # # self.chrome_options.add_argument("--incognito")
    # # self.chrome_options.add_argument("--start-minimized")
    # self.chrome_options.add_argument("--window-size=600,500")

    # self.driver.execute_script("document.body.style.zoom='80%'")


    self.driver = webdriver.Chrome()
    self.driver.get("https://demo.opencart.com/en-gb?route=account/register")
    self.driver.maximize_window()
    # self.driver.execute_script("document.body.style.zoom='80%'")
    time.sleep(3)
    # # self.driver.execute_script("document.body.style.zoom='80%'")
    # self.driver.execute_script("document.querySelector('input.form-check-input').click()")
    # self.driver.execute_script("document.querySelector('.form-check-inline > .form-check-input').click()")
    #self.driver.execute_script("document.querySelector('button.btn.btn-primary').click()")



    self.lp = RegisterPage(self.driver)
    self.lp.setFistName("Shubham")
    time.sleep(2)

    self.lp.setLastName("Sharma")
    time.sleep(2)
    self.lp.setEmail("Shubham649@gmail.com")
    time.sleep(2)
    self.lp.setPassword("Shubham123@")
    time.sleep(4)

    # self.driver.execute_script("document.querySelector('button.btn.btn-primary').scrollIntoView({behavior:'smooth'})")

    self.lp.clickPrivacyPolicyButton()
    time.sleep(1)
    self.lp.clickContinueButton()


    #self.act_title = self.driver.title
    # self.driver.execute_script("document.querySelector('button.btn.btn-primary').click()")
    time.sleep(2)




    # self.driver.close()
    self.act_title = self.driver.title
    #
    assert self.act_title == "Your Account Has Been Created!"

    # #
    # #
    self.driver.close()
