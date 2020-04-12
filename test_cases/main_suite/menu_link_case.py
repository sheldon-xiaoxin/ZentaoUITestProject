import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

current = os.path.dirname(__file__)
chrome_driver_path = os.path.join( current , '../../webdriver/chromedriver' )

class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None: # 把selenium的初始化配置放入
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')

    def tearDown(self) -> None: #测试清理  浏览器关闭  注册
        time.sleep(2)
        self.driver.quit()

    def test_my_link(self):
        '''case04 验证我的地盘菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH,'//li[@data-id="my"]').click()
        self.assertTrue( EC.title_is("我的地盘 - 禅道") )

    def test_product_link(self):
        '''case05 验证产品菜单能否正确链接'''
        self.driver.find_element(By.XPATH,'//input[@id="account"]').send_keys('test01')
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys('newdream123')
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        self.driver.find_element(By.XPATH,'//li[@data-id="product"]').click()
        self.assertTrue( EC.title_is("产品主页 - 禅道") )


if __name__=='__main__':
    unittest.main()







