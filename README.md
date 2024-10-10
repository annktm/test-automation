# Automation Testing of Amazon Login with Python and Selenium

This framework automates the Amazone web login in chrome browser in mac os with selenium and python. 

# Test Scenarios covered:

  Positive Scenario: Amazon web login with a valid Email and Password.
  Negative Scenario: Amazone web login with an invalid Email.
 
# Automation Environment Setup:
  * Install python: Go to python.org and download latest python version. https://www.python.org/downloads/
  * Install selenium: Run command 'pip3 install -U selenium'.
  * Download and install PyCharm IDE: https://www.jetbrains.com/pycharm/download/?section=mac
  * Chrome webdriver: As of selenium 4.10.0 the chrome webdriver manager is fully integrated. If using an older version of selenium, download and install chrome webdriver seperatelty from https://www.selenium.dev/.
  * Clone this repository and open the automation project in PyCharm.
  * Add selenium package to the project: PyCharm Settings>> project: Python Interpreter >> Search and add Selenium package.
  * Update Login credentials in configuration file: Provide a valid 'LOGIN_EMAIL' and 'LOGIN_PASSWORD' in config.py.

# Test Result Logging: 
Test execution details will be added to 'AmazonLoginReport.log' under test-automation>> amazon_ui_test folder in the below format:
  <img width="1207" alt="Screenshot 2024-10-10 at 12 03 55 PM" src="https://github.com/user-attachments/assets/9afabe23-a20a-4ced-ad1e-8b50e45c5f54">

  Positive Test Scenario Execution- Validate Amazon Login with valid credentials:
  
  https://github.com/user-attachments/assets/b669782b-3243-4ef6-bba3-16c330e67101
  

  Negative Test Scenario Execution- Validate Amazon login with invalid Email shows correct error message:
  
  https://github.com/user-attachments/assets/10af4eca-03ce-474e-b7f7-94c7d1e5194c

