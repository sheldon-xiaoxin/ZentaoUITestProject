import os
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import set_driver
from common import login


class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None: # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None: #测试清理  浏览器关闭  注册
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        '''case03 使用test01  newdream12 测试能否登录'''
        login.login(self.driver,'test01','newdream12')
        self.assertTrue( WebDriverWait(self.driver,10).until(EC.alert_is_present()) )

if __name__=='__main__':
    unittest.main()







