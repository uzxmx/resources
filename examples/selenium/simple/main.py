#!/usr/bin/env python

import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Main:
    @classmethod
    def run(cls, no_headless=False, wait_infinitely=False):
        options = Options()
        options.headless = not wait_infinitely and not no_headless

        driver = webdriver.Chrome(options=options)

        driver.get('https://www.baidu.com')
        assert '百度' in driver.title
        elem = driver.find_element(By.NAME, 'wd')
        elem.clear()
        elem.send_keys("百度")
        elem.send_keys(Keys.RETURN)

        print('Find elements by class name')
        elements = WebDriverWait(driver, timeout=10).until(lambda d: d.find_elements(By.CLASS_NAME, 'c-title'))
        print('Found %d elements' % len(elements))
        assert len(elements) > 0
        for e in elements:
            assert e.tag_name == 'h3'
            assert '百度' in e.text

        print('Find elements by xpath')
        elements = WebDriverWait(driver, timeout=10).until(lambda d: d.find_elements(By.XPATH, '//div[contains(@class, "result-op")]//h3[contains(@class, "c-title")]'))
        print('Found %d elements' % len(elements))
        assert len(elements) > 0
        for e in elements:
            assert e.tag_name == 'h3'
            assert '百度' in e.text

        if wait_infinitely:
            WebDriverWait(driver, timeout=3600).until(lambda d: False)

        driver.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--no-headless', action='store_true', default=False, help='No headless')
    parser.add_argument('-W', '--wait-infinitely', action='store_true', default=False, help='Wait infinitely so you can inspect the page. This implies `--no-headless`')
    args = parser.parse_args()
    Main.run(no_headless=args.no_headless, wait_infinitely=args.wait_infinitely)
