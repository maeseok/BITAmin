## 복합 자료형 - 리스트, 튜플, 딕셔너리
## 생성, 요소 접근, 수정, 삭제, 삽입

## 리스트 생성
nums = [11, 22, 33, 44, 55]
print(nums)
print(nums[1:3])


nums[0] = -1
nums[1:3] = [100,200,300]
print(nums)

nums[1] = 4
# 주의 : 요소에 리스트 자체가 삽입된다.
nums[1] = [100,200,300]

## 얕은 복사, 깊은 복사
## 얕은 복사 : 같은 것을 가리킴 (같은 메모리 주소를 공유)
## 깊은 복사 : 리스트 요소 하나하나가 복사되는 것 (다른 메모리 공간)

nums1 = [11,22,33]
nums2 = nums1
nums2[0] = 0
print(nums1)
print(nums2)

print(id(nums1))
print(id(nums2))

# 리스트의 연결 연산 +, *
nums1 = [11,22,33]
nums2 = [44,55]
nums3 = nums1 + nums2
print(nums3)

len(nums1)

# 리스트에 추가 삽입 - append insert
nums=[11,22,33]
nums.append(55)
print(nums)
nums.insert(3, 44)
print(nums)

# 리스트 삭제 - 인덱스 이용 삭제 (del), 값 이용 삭제 (remove)
nums = [11,22,33,0,11,22,33]
del nums[1]
print(nums)
nums.clear()

nums = [11,22,33,44,55]
print( 22 in nums)
print( 66 not in nums)


heroes = ['아이언맨', '토르', '헐크', '스칼렛 위치']
for hero in heroes:
    print(hero)
for hero in range(0,4,2):
    print(heroes[hero])

d = {'python' : '파이썬', 'basic':'기초'}
for i in d:
    print(i)

for i in d.keys():
    print(i)

for i in d.values():
    print(i)

for a,b in d.items():
    print(a,b)

