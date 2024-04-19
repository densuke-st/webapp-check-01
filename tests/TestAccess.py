from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
import unittest
import sys


# リモートサーバーのアドレス
REMOTE_URL = 'http://selenium:4444/wd/hub'

CHECK_WORD = "Hello,PHP"

class SampleTest(unittest.TestCase):
    def setUp(self):
            self.driver = webdriver.Remote(REMOTE_URL, options=webdriver.ChromeOptions())
            assert self.driver is not None

    def tearDown(self):
        self.driver.quit()

    def test_Hello_using_PHP(self):
         """./public/hello.phpを読み込み、
         PHPのコードを示す'<?php'が含まれていることを確認する"""
         with open('./public/hello.php') as f:
             php_code = f.read()
             self.assertIn('<?php', php_code)

    def test_Hello(self):
        """http://web/hello.php へアクセスし、
        最初のpタグにCHECK_WORD変数と同じ文字列があることをテストする
        """
        self.driver.get('http://web/hello.php')
        time.sleep(2)
        p = self.driver.find_element(by=By.TAG_NAME, value='p')
        self.assertEqual(p.text, CHECK_WORD)

if __name__ == '__main__':
    unittest.main()
