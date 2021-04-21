name ="마린"
hp = 40
damage = 5

print("{0} 유닛이 생성되었습니다.".format(name))
hp = 40
damage = 5
location = 1dddd

def attack (name,location,damage) :
    print("{0}:{1} 방향으로 적군을 공격 : damage = {2}".format(name,location,damage))



class unit :
    def __init__(self,name,hp,damage) :
        self.name =name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0} , 공격력 {1}".format(self.hp, self.damage))

marine1 = unit("마린",40,5)
marine2 = unit("마린",40,5)
tank = unit("탱크",150,35)

wraith1 = unit("레이스",80,5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))


class AttackUnit :
    def __init__(self,name,hp,damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
    

    def attack(self,location) :
        print("{0} :{1} 현재 체력은 {2}입니다.".format(self.name,location,self.damage))


    def damaged(self,damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
    def damaged(self,damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
     def damaged(self,damage) :
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))

 


firebat1 = AttackUnit("파이어뱃",50,16)
firebat1
firebat1.attack("5시")
firebat1.damaged(25)


from selenium import webdriver
import time

interval = 2 ## 딜레이 시간 설정


browser = webdriver.Chrome()

browser.maximize_window()

url = "https://play.google.com/store/movies/top"

browser.get(url)


# browser.execute_script("window.scrollTo(0,1080)")

# browser.execute_script("window.scrollTo(0,2080)")

prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    
    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, "  <할인되지 않은 영화 제외>")
        continue

    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 : https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 100)


### 깃허브 오류로 업데이트가 안되서 일시적인 업데이트


import time
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option('prefs',{'download.default_directory':r'C:\Users\정지민\Desktop\python_project\python_project'})


browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame('iframeResult')



elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

print(browser.title)

time.sleep(5)

browser.quit( )

## 깃허브 오류 
