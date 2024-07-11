# 프로그램 : 복합 자료형 리스트 실습
# 작 성 자 : 이형석, 2024-07-08

# 실습문제 1번 : 리스트 만들고 1~10 저장 후 총합 출력
List=[i for i in range(1,11)]
print(f'List: {List}')
print(f'총합: {sum(List)}', end='\n\n')

# 실습문제 2번 : 리스트 만들고 5개 정수 입력받아 짝수 총합 출력
List2 = []
result = 0
for i in range(5):
    data=int(input('정수입력: '))
    if data%2==0:
        result+=data
    List2.append(data)
print(f'리스트 안의 짝수 총합은 {result}이다.', end='\n\n')

# 실습문제 3번 : 리스트 만들고 짝수 총합 계산 (0 입력할 때까지 반복)
List3 = []
result = 0
while(True):
    data = int(input('정수입력: '))
    if data==0:
        break
    if data%2==0:
        result+=data
    List3.append(data)
print(f'리스트 안의 짝수 총합은 {result}이다.', end='\n\n')
    
# 실습문제 4번 : 리스트 만들고 1~5사이의 임의의 정수 10개 저장한 결과와 3 삭제한 결과 출력
from random import randint
List4 = []
for i in range(10):
    data = randint(1,5)
    List4.append(data)
print(f'List: {List4}')
while(True):
    if List4.count(3)==0:
        break
    List4.remove(3)
print(f'3을 삭제한 List: {List4}', end='\n\n')

# 도전문제 1번 : 리스트 만들고 1~12 사이 임의 숫자 7개 저장 후 총합 계산 후 출력
List5 = []
result = 0
for i in range(7):
    data = randint(1,12)
    result += data
    List5.append(data)
print(f'List: {List5}')
print(f'생성된 임의의 수 총합: {result}', end='\n\n')

# 도전문제 2번 : 리스트 만들고 사용자가 입력한 실수 저장 후 짝수 번째 요소 총합 계산 후 출력
List6 = []
result = 0
cnt = 1
while(True):
    data = float(input('실수입력: '))
    if data<0:
        break
    if cnt%2==0:
        result += data
    cnt+=1
print(f'리스트 안의 짝수 번째 요소의 총합은 {result:.1f}이다.', end='\n\n')

# 도전문제 3번 : 리스트 만들고 1~9사이의 임의의 홀수 10개 저장 후 결과와 5를 삭제하고 리스트 내용 출력
List7 = []
while(True):
    data = randint(1,9)
    if len(List7)==10:
        break
    if data%2==1:
        List7.append(data)
print(f'List: {List7}')
while(True):
    if List7.count(5)==0:
        break
    List7.remove(5)
print(f'5를 제거한 List 내용: {List7}')