# -*- coding: UTF-8 -*-
__author__ = 'Maglweb'

import unittest
from selenium import webdriver
import time
import sys
from selenium.webdriver.support import expected_conditions as ec

reload(sys)
sys.setdefaultencoding('utf-8')

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        url = 'http://www.sogou.com'
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        u'验证元素'
        self.driver.implicitly_wait(5)
        self.assertTrue(self.driver.title == u'搜狗搜索引擎 - 上网从搜狗开始')

    def test_02(self):
        self.driver.find_element_by_id('query').send_keys('selenium')
        self.driver.find_element_by_id('stb').click()
        time.sleep(5)
        self.assertIn('selenium',self.driver.title)

if __name__ == '__main__':
    unittest.main()
