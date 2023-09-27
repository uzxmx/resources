#!/usr/bin/env python

import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Main:
    @classmethod
    def run(cls, opts):
        options = Options()
        options.headless = not opts.wait_infinitely and not opts.no_headless

        if opts.user_agent:
            options.add_argument('--user-agent=%s' % opts.user_agent)
        else:
            options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')

        if opts.proxy_server:
            options.add_argument('--proxy-server=%s' % opts.proxy_server)

        options.add_argument('--user-data-dir=%s' % os.path.join(os.getcwd(), 'user_data'))

        if opts.remote:
            driver = webdriver.Remote(
               command_executor=opts.remote_url,
               options=options
            )
        else:
            driver = webdriver.Chrome(options=options)

        try:
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

            def find_input(d):
                print('Find input')
                e = d.find_element(By.ID, 'kw')
                if e.tag_name == 'input':
                    print('Found input')
                    return e
                else:
                    print('Not found input')

            result = WebDriverWait(driver, timeout=10).until(find_input)
            print(result)
            print(type(result))

            import code
            code.interact(local=locals())

            if opts.wait_infinitely:
                WebDriverWait(driver, timeout=3600).until(lambda d: False)

            driver.close()
        finally:
            # Close the session.
            driver.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--no-headless', action='store_true', default=False, help='No headless')
    parser.add_argument('-W', '--wait-infinitely', action='store_true', default=False, help='Wait infinitely so you can inspect the page. This implies `--no-headless`')
    parser.add_argument('-r', '--remote', action='store_true', default=False, help='Use remote webdriver')
    parser.add_argument('--remote-url', default='http://127.0.0.1:4444/wd/hub', help='The url for the remote webdriver')
    parser.add_argument('-u', '--user-agent', help='The user agent')
    parser.add_argument('-p', '--proxy-server', help='The proxy server, e.g. http://127.0.0.1:8080')
    args = parser.parse_args()
    Main.run(args)
