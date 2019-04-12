import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = "SAGOL"
PASS = "1234"

session = requests.session()

login_info = {
    "memberId" : USER,
    "password" : PASS
}

url_login = "http://localhost:8080/blogs/login"
res = session.post(url_login, data = login_info)
res.raise_for_status()

print(res.text)

#마이페이지 접근하기
url_mypage = "http://localhost:8080/blogs/view?page="
res = session.get(url_mypage)
print(res.text)

#마일리지와 이코인 가져오기
#soup = BeautifulSoup(res.text, "html.parser")
#mileage = soup.select_one(".mileage_section1 span").get_text()
#ecoin = soup.select_one(".mileage_section2 span").get_text()

#print("마일리지: "+ mileage)
#print("이코인: "+ ecoin)
