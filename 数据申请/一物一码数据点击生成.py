__author__ = 'joker_jiang'

from selenium import webdriver
import time
import xlrd
# import  subprocess
from selenium.webdriver.common.action_chains import ActionChains  #点击事件
from selenium.webdriver.support.ui import WebDriverWait

def login (browser):
    browser.get("http://marketing.wochacha.com/index.php?s=/Admin/Login/index")
    print ('现在将浏览器最大化')
    browser.maximize_window()

    # options = webdriver.ChromeOptions()
    # prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'E:\aveeno\test\ceshi'}
    # options.add_experimental_option('prefs', prefs)


    pagename = browser.title
    browser.implicitly_wait(30)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/input').clear
    browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/input').send_keys(usename)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input').clear
    browser.find_element_by_xpath('//*[@id="loginForm"]/div[2]/input').send_keys(password)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div[3]/input').clear
    browser.find_element_by_xpath('//*[@id="loginForm"]/div[3]/input').send_keys(yaoqingma)
    # time.sleep(3)
    browser.find_element_by_xpath('//*[@id="loginForm"]/input[2]').click()
    time.sleep(1)
    a=browser.find_element_by_xpath('.//*[@id="side-menu"]/li[3]/a')
    ActionChains(browser).double_click(a).perform()
    time.sleep(1)
    b=browser.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[1]/a')
    ActionChains(browser).double_click(b).perform()
    b=browser.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[1]/ul/li[1]/a')
    ActionChains(browser).double_click(b).perform()
    time.sleep(1)
    browser.switch_to_frame("iframe175")
    # browser.find_element_by_id("save").click()
    time.sleep(1)
    # n = 4
    for i in range(0, 10):
        # browser.switch_to_frame("iframe19")
        if i == 0:
            browser.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div[2]/table/tbody/tr[5]/td[6]/a[1]").click()
            browser.implicitly_wait(30)
        # browser.switch_to_alert().accept()

        browser.find_element_by_id("codeNum").click()
        browser.find_element_by_id("codeNum").send_keys("50000")
        browser.find_element_by_id("createCode").click()
        time.sleep(30)
        # browser.implicitly_wait(60)
        # browser.switch_to_alert().accept()
        browser.maximize_window()
        browser.implicitly_wait(120)
        # browser.get('http://http://marketing.wochacha.com/')
        # browser.switch_to_alert().accept()







if __name__ == "__main__":
   browser = webdriver.Chrome()
   usename="wclfirst@163.com"
   password="123456"
   yaoqingma="11111111"
   login(browser)


