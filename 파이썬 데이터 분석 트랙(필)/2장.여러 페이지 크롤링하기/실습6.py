import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    # 기사에서 내용을 추출하고 반환하세요.
    div = soup.find('div',class_="_article_body_contents")

    result = div.get_text().replace('\n','').replace('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}','').replace('\t','')
    return result

def get_href(soup) :
    ul = soup.find("ul",class_= "type06_headline")
    result=[]
    for a in ul.find_all("a",class_= "nclicks(fls.list)"):
        result.append(a["href"])

    return result

def get_request(section) :
    # 입력된 분야에 맞는 request 객체를 반환하세요.
    # 아래 url에 쿼리를 적용한 것을 반환합니다.
    url = "https://news.naver.com/main/list.nhn"
    sections = {
        "정치" :100,
        "경제" : 101,
        "사회" : 102,
        "생활" : 103,
        "세계" : 104,
        "과학" : 105

    }
    req = requests.get(url,params={"sid1":sections[section]})
    return req
    

def main() :
    list_href = []
    result = []
    
    # 섹션을 입력하세요.
    section = input('"정치", "경제", "사회", "생활", "세계", "과학" 중 하나를 입력하세요.\n  > ')
    
    req = get_request(section)
    soup = BeautifulSoup(req.text, "html.parser")
    
    list_href = get_href(soup)
    
    for href in list_href :
        href_req = requests.get(href)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result.append(crawling(href_soup))
    print(result)


if __name__ == "__main__" :
    main()
