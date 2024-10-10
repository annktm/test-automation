from selenium import webdriver
from amazon_ui_test import BaseClass
import time
import logging
from selenium.webdriver.common.by import By
import config


class amazonLogin(BaseClass):
    def amazon_success_login(self):
        try:
            self.driver = webdriver.Chrome()
            self.log().info("--- TEST: AMAZON SUCCESS LOGIN ---")
            self.log().info("amazon_success_login: Test execution started")
            self.driver.get(config.AMAZON_HOME_URL)
            time.sleep(10)
            self.driver.maximize_window()
            # Click on Sign in Link in Home page
            self.driver.find_element("id", 'nav-link-accountList-nav-line-1').click()
            # Enter Email and click Continue button
            self.driver.find_element("id", 'ap_email').send_keys(config.LOGIN_EMAIL)
            self.driver.find_element("id", 'continue').click()
            self.driver.find_element("id", 'ap_password').send_keys(config.LOGIN_PASSWORD)
            self.driver.find_element("id", 'signInSubmit').click()
            time.sleep(3)
            navigation_text = self.driver.find_element("id", 'nav-link-accountList-nav-line-1').text
            if navigation_text == "Hello":
                self.log().info("amazon_success_login: Test execution completed successfully")
            else:
                self.log().info("amazon_success_login: Test failed")
            self.driver.quit()
        except:
            self.log().info("--- amazon_success_login:An exception occurred! ---")

    def amazon_invalid_email_login(self):
        try:
            self.driver = webdriver.Chrome()
            self.log().info("--- TEST: AMAZON INVALID EMAIL LOGIN ---")
            self.log().info("amazon_invalid_email_login: Test execution started")
            self.driver.get(config.AMAZON_HOME_URL)
            time.sleep(10)
            self.driver.maximize_window()
            # Click on Sign in Link in Home page
            self.driver.find_element("id", 'nav-link-accountList-nav-line-1').click()
            # Enter Email and click Continue button
            self.driver.find_element("id", 'ap_email').send_keys(config.INVALID_EMAIL)
            self.driver.find_element("id", 'continue').click()
            time.sleep(3)
            alert_text = self.driver.find_element(By.XPATH,'//*[@id="auth-email-invalid-claim-alert"]/div/div').text
            if alert_text == "Enter a valid email address or phone number":
                self.log().info("amazon_invalid_email_login: Test execution completed successfully")
            else:
                self.log().info("amazon_invalid_email_login: Test failed, Wrong text:"+alert_text)
            self.driver.quit()
        except:
            self.log().info("--- amazon_invalid_email_login:An exception occurred! ---")


s = amazonLogin()
s.amazon_invalid_email_login()