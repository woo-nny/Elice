import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    # soup 객체에서 추출해야 하는 정보를 찾고 반환하세요.
    tbody = soup.find("tbody")
    result =[]
    for p in tbody.find_all("p",class_="title"):
        result.append(p.get_text().replace('\n',''))
    return result
    
    


def main() :
    url = "https://music.bugs.co.kr/chart"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    # crawling 함수의 결과를 출력합니다.
    print(crawling(soup))


if __name__ == "__main__" :
    main()
