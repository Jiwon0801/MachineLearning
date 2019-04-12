from selenium import webdriver
USER="ssintico88"
PASS="tnttkwk0801"

#options = webdriver.ChromeOptions()
#options.add_argument('headless')
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

browser.implicitly_wait(3)

url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")

e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e=browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭합니다.")

browser.get("https://mail.naver.com/")

mails = browser.find_element_by_css_selector(".p_info span")
print(mails)
for mail in mails:
    print("-", mail.text)

