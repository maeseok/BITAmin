# 프로그램 : 복합 자료형 리스트 실습
# 작 성 자 : 이형석, 2024-07-08

from random import randint

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