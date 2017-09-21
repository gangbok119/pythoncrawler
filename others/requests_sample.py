# requests설치
# 이 파일에서 필요한 모듈 import
# 적절히 HTTP요청을해서 아래 주소의 HTML문서 내용을 받아와 source변수에 할당
# source변수에 할당되어있는 텍스트를 이용해 BeautifulSoup객체 생성
# 생성한 BeautifulSoup객체에서 prettify()메서드 실행
import requests
from bs4 import BeautifulSoup

webtoon_url = 'http://comic.naver.com/webtoon/list.nhn?titleId=651673&weekday=sat'

response = requests.get(webtoon_url)
source = response.text
soup = BeautifulSoup(source)
print(soup.prettify())


# 이 데이터를 sample.txt파일로 생성(이미 존재할경우 덮어쓰기)
with open('sample.txt', 'wt') as f:
    f.write(soup.prettify())

