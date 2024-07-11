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
#print(f'리스트 안의 짝수 총합은 {result}이다.', end='\n\n')
    
# 실습문제 4번 : 리스트 만들고 1~5사이의 임의의 정수 10개 저장한 결과와 3 삭제한 결과 출력
from random import randint
List4 = []
for i in range(10):
    data = randint(1,5)
    List4.append(data)
#print(f'List: {List4}')
while(True):
    if List4.count(3)==0:
        break
    List4.remove(3)
#print(f'3을 삭제한 List: {List4}', end='\n\n')

def create_list(exist):
    for i in range(10):
        data = randint(1,5)
        exist.append(data)

def remove_3_in_list(exist):
    while(True):
        if List4.count(3)==0:
            break
        List4.remove(3)

lst = []
#create_list(lst)
#remove_3_in_list(list)

import random
#1~5 중 10개 랜덤
exlist = random.choices(range(1,6), k=10)
#print(exlist)

while 5 in exlist:
    exlist.remove(5)
#print(exlist)

def input_list(lst):
    name = input('name: ')
    num = input('번호: ')
    lst.append(name)
    lst.append(num)

#userinfo = []
#input_list(userinfo)
#print(userinfo)

def input_list():
    name = input('name: ')
    num = input('번호: ')

    lst=[]
    lst.append(name)
    lst.append(num)
    return lst
userinfo = input_list()
print(userinfo)

# split 2
name, number = input_list()
print(f'name = {name}, number = {number}')

scores = [
    ['이찬수',95,85],
    ['홍길동',90,80]
]

print(scores)
print(scores[0])
print(scores[0][0])

for item in scores:
    print(item)

for item in scores:
    for i in item:
        print(i, end='/')
    print()

# 튜플 연습
f1 = (11,22,33)
print(f1[0], f1[0:2])
f2 = (44, 55)
f3 = f1+f2
print(f3)
f4 = f2*3
print(f4)

f3 = (11)
f4 = 11
print(type(f3))
print(type(f4))

f5 = (11,)
f6 = 11,
print(type(f5))
print(type(f6))

f1 = (11,22,33,)
#f1[0] = 1 - 요소 변경 x
f1 = (55,66,)

dic = {'python':'파이썬', 'basic':'기초', 'programing':'프로그래밍'}
print(dic)

dic['python']

#딕셔너리의 함수(메소드)를 이용가능- get
dic.get('python')

key = 'python'
if key in dic:
    print(dic[key])
else:
    print(f'{key} - 유효한 키가 아닙니다.')

dic['code'] = '코드'
print(dic)

del dic['code']

dic['basic'] = '생기초'
print(dic)
dic.clear()

d = {'python':'파이썬', 'basic':'기초', 'programing':'프로그래밍'}
print(d.keys())
print(d.values())
print(d.items())

# for 이용해서 반복시 2가지 방식 - 키 리스트를 이용, 딕셔너리 자체 이용
for i in d.keys():
    print(f'키 :{i}, 값 : {d[i]}')