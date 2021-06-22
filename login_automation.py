from selenium import webdriver

Username='test@orangetoolz.com'
Password="8Kh8nTe*^jdk"

driver=webdriver.Chrome('chromedriver.exe')
driver.get('http://159.89.38.11/login')
user_input=driver.find_element_by_id("email-1")
user_input.send_keys(Username)
user_pass=driver.find_element_by_id("password-1")
user_pass.send_keys(Password)

login = driver.find_element_by_id("m_login_signin_submit")
login.click()
