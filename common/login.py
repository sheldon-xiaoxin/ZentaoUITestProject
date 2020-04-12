from selenium.webdriver.common.by import By

def login(driver,username,passwd):
    driver.find_element(By.XPATH, '//input[@id="account"]').send_keys(username)
    driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(passwd)
    driver.find_element(By.XPATH, '//button[@id="submit"]').click()