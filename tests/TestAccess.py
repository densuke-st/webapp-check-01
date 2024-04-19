from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest
import sys

# リモートサーバーのアドレス
REMOTE_URL = 'http://selenium:4444/wd/hub'

class SampleTest(unittest.TestCase):
    def setUp(self):
            self.driver = webdriver.Remote(REMOTE_URL, options=webdriver.ChromeOptions())
            assert self.driver is not None

    def tearDown(self):
        self.driver.quit()

    def test_access(self):
        self.driver.get('http://web/')
        time.sleep(2)
        self.driver.save_screenshot('screenshot.png')

    def test_title_fail(self):
        self.driver.get('http://web/')
        time.sleep(2)
        self.assertTrue('PhP' in self.driver.title)

    def test_title_PHP(self):
        self.driver.get('http://web/')
        time.sleep(2)
        self.assertTrue('PHP' in self.driver.title)

if __name__ == '__main__':
    unittest.main()
