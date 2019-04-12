from selenium import webdriver

url = "https://www.naver.com/"


options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe', chrome_options = options)

#browser = webdriver.PhantomJS('C:/phantomjs-2.1.1-windows/bin/phantomjs.exe')

browser.implicitly_wait(3)

browser.get(url)

browser.save_screenshot('Website1.png')

browser.quit()