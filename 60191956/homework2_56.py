# 프로그램 : 반복문, 함수 연습 및 MJU 성적 프로그램 실행
# 작 성 자 : 이형석, 2024-07-05

from my_string import * 
from score_module import * 

# [1] MJU 성적 프로그램 실행
print('*'*10 + ' MJU 성적 프로그램 '+ '*'*10)
print('<1> 자료 입력')
print('<2> 평균 계산')
print('<3> 학점(등급) 계산')
print('<4> 장학금 여부')
print('<5> 프린트')
print('<0> 종료')

while(True):
    choice = int(input('메뉴를 선택하시오: '))
    if choice==1:
        math_score = int(input('수학 점수를 입력하시오: '))
        english_score = int(input('영어 점수를 입력하시오: '))
    elif choice==2:
        avg_score = average_cal(math_score, english_score)
        print('평균 계산이 완료되었습니다!')
    elif choice==3:
        Grade = grade_cal(avg_score)
        print('등급 계산이 완료되었습니다!')
    elif choice==4:
        previous_average = float(input('이전 평균을 입력하시오: '))
        scholarship = scholarship_check(Grade, avg_score, previous_average)
        print('장학금 금액이 계산이 완료되었습니다!')
    elif choice==5:
        print_program(avg_score, Grade, scholarship)
    elif choice==0:
        print('프로그램을 종료합니다.')
        break
    else:
        print('다시 입력해주세요.')
    print()
print('*'*39)

# [2] 명지투데이 뉴스 이용해 각 모듈 함수 실행
import requests
from bs4 import BeautifulSoup as bs

req = 'https://www.mju.ac.kr/mjukr/302/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGbWp1a3IlMkYxNjYlMkYyMTI5ODclMkZhcnRjbFZpZXcuZG8lM0ZwYWdlJTNEMiUyNnNyY2hDb2x1bW4lM0QlMjZzcmNoV3JkJTNEJTI2YmJzQ2xTZXElM0QlMjZiYnNPcGVuV3JkU2VxJTNEJTI2cmdzQmduZGVTdHIlM0QlMjZyZ3NFbmRkZVN0ciUzRCUyNmlzVmlld01pbmUlM0RmYWxzZSUyNmlzVmlldyUzRHRydWUlMjZwYXNzd29yZCUzRCUyNg%3D%3D'
response = requests.get(req)
soup = bs(response.content, 'html.parser')
content_div = soup.find('div', class_='artclView')
message = content_div.get_text(strip=True)

Size(message)
Exist(message, '이형석')
Count(message, 'MJ')