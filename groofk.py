# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import time
import unittest
from nose.plugins.attrib import attr


class TestRutr(unittest.TestCase):

    def setUp(self):
        #need login and password
        self.login = ""
        self.password = ""
        self.cat_name = u"Доктор Хаус / House M.D."
        self.text_5 = "House M.D."
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://rutracker.org")

    def auth(self):
        a = None
        try:
            a = self.driver.find_element_by_name("login_username")
        except:
            return True

        a.send_keys(self.login)
        self.driver.find_element_by_name("login_password").send_keys(self.password)
        self.driver.find_element_by_name("login").click()

        try:
            self.driver.find_element_by_name("login_username")
            return False
        except:
            print "No element"
            return True

    @attr(__test__ = True)
    @attr('case1')
    def test_search(self):

        self.auth();

        self.driver.find_element_by_name("nm").send_keys(self.text_5)
        self.driver.find_element_by_css_selector("input.med").click()
        self.driver.find_element_by_link_text(self.cat_name).click()
        elements = self.driver.find_element_by_css_selector("p.med.bold").text
        elem = int(elements[20:-11])
        print elem
        n = elem/50 + 1
        print "n = " + str(n)
        table = self.driver.find_element_by_id("tor-tbl").text
        #print table
        count = 0
        while(True):
            try:
                count = count + 1
                print count
                self.driver.find_element_by_link_text(u"След.").click()
                table = self.driver.find_element_by_id("tor-tbl").text
                print table
            except:
                break
        print n
        print "count=" + str(count)
        if n != count:
            raise Exception('the number of pages is bad or counter is broken')
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
