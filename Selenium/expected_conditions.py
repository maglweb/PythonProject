# -*- coding: UTF-8 -*-
__author__ = 'Maglweb'

import sys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Firefox()
driver.get('http://www.sogou.com')
text = driver.find_element_by_link_text(u'学习形式管理')
WebDriverWait(driver,10).until(ec.visibility_of(text))
text.click()