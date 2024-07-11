# 프로그램 : 모듈 연습, 리스트 (복합 자료형), 지역 변수 vs 전역 변수
# 작 성 자 : 이형석, 2024-07-08

## 지역 변수 vs 전역 변수 - 변수 이름이 같지만, 전역변수만 유지 하려는 경우

# 함수 정의
def get_circle_area(radius):
    global area
    area = 3.14 * radius **2
    print(f'함수의 area 값: {area}')
data = float(input('넓이를 구할 원의 반지름? '))
area = 0
# 함수 호출
get_circle_area(data)
print(f'주 프로그램의 area 값: {area}')

import calc_area
calc_area.get_circle_area(10)
calc_area.get_rect_area(10,20)

#from calc_area import get_circle_area as get_CA

import hello
hello.make_message()
name = input('이름을 입력하시오: ')
print(hello.make_message_let(name))

# 표준 모듈 - 난수 (random)
import random
#dir(random)
a = random.randint(1,6)
print(a)

def roll_dice():
    return random.randint(1,6)
print(roll_dice())

n = random.randint(1,45)
print(n)

from calendar import *
cal = month(2024, 7)
print(cal)

#help('modules')

list1 = [11,22,33,44,55]
list2 = ['단출하게', '단아하게', '당당하게']
list3 = []
print(list1)
print(list2)
print(list3)

list4 = [11, '홍길동', 19, 180, 5]
list5 = [11, '홍길동', [10,10,92,100]]
print(list4)
print(list5)

print(list4[1], '님의 키는', list4[-1], 'cm입니다.')
sub_list = list[1:3]
print(sub_list)
print(sub_list[0])

nums = [11,22,33,44,55]
nums[0] = -1
print(nums)

nums[1:3] = [100,200,300]
print(nums)

nums = [11,22,33,44,55]
nums[1:2] = [100,200,300]

nums1 = [11,22,33]
nums2 = []

id(nums1)
id(nums2)

# 얕은 복사
nums2 = nums1
nums2[0] = 0
print(nums1)
print(nums2)

# 깊은 복사
nums1 = [11,22,33]
nums3 = nums1[:]
nums3[0] = 0
print(f'nums1 = {nums1}')
print(f'nums3 = {nums3}')

print(id(nums1))
print(id(nums3))

nums1 = [11,22,33]
nums2 = [44,55]
nums3 = nums1 + nums2
print(nums3)

nums4 = nums1 * 2
print(nums4)

nums = [11,22,33,44,55]
n = len(nums)
print(n)

nums = [11,22,33]
nums.append(55)
print(nums)

nums.insert(3,44)
print(nums)

nums.insert(-1,50)
print(nums)

nums = [11,22,33,0,11,22,33]
del nums[1]
print(nums)

del nums[2:4]
print(nums)

nums.remove(33)
print(nums)

nums = [11,22,33,44,55]
nums[1:4] = []
print(nums)

nums.clear()
print(nums)

nums = [11,22,33,44,55]
nums.index(33)
nums.count(33)

print(22 in nums)
print(66 not in nums)

heroes = ['아이언맨', '토르', '헐크', '스칼렛 위치']
for hero in heroes:
    print(hero)

for hero in range(0, 4, 2):
    print(heroes[hero])

msgs = ['단출하게', '단아하게', '당당하게']
for i in range(len(msgs)):
    print(f'msgs[i]/', end='')

for i in range(len(msgs)-1, -1, -1):
    print(f'msgs[i]/', end='')
    