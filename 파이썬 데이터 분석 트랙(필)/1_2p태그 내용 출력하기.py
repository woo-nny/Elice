from bs4 import BeautifulSoup

# index.html을 불러와서 beautifulsoup 객체를 초기화해 soup에 저장하세요.
soup = BeautifulSoup(open("index.html"),"html.parser")

print(soup.find('p').get_text())

# soup를 사용하여 요구되는 정보를 출력해보세요.
