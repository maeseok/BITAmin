d = {'python':'파이썬', 'basic':'기초', 'programing':'프로그래밍'}
print(d)

type(d)
print(d['python'])

print(d.get('python'))

key ='c'
if key in d:
    print(d[key])
else:
    print('오류')

del d['basic']
print(d)

d.clear()

d = {'python':'파이썬', 'basic':'기초', 'programing':'프로그래밍'}
print(d.keys())
print(d.values())
print(d.items())

for key in d.keys():
    print(key, d[key])

d['code'] = '코드'

def dict_append(dic, key, value):
    if key in dic:
        return False
    dic[key] = value
    return True

dict_append(d, 'c', '씨')
dict_append(d, 'python', 'sss')

if dict_append(d, 'python', 'sss'):
    print('추가 성공')
else:
    print('추가 실패')

print(d)

file = open('example.txt', 'r')
file.close()
print('파일 열고 닫기 완료')

row = []
for i in range(5):
    value = 1
    row.append(value)
print(row)

matrix = []
for x in range(3):
    row = []
    for i in range(5):
        value = 1
        matrix.append(value)
    matrix.append(row)
print(matrix)

import os
file_path = os.getcwd()
os.listdir(file_path)
file_path = 'example.txt'
if os.path.exists(file_path):
    file = open(file_path, 'r')
    file.close()
    print('파일 열고 닫기 완료')
else:
    print('ERROR')
print('end')

with open('example.txt', 'r') as file:
    pass
print('파일 열고 닫기')

num = 2
name = '홍길동'
with open('example_angi.txt', 'w') as file:
    file.write('1 이찬수\n')
    file.write(f'{num} {name}\n')
print('끝')

#cp949, euc-kr, ansi 같은 계열, utf-8은 다른 계열
with open('example_angi.txt', 'r', encoding='ansi') as file:
    all = file.read()
print(all)

#lines=[]
#with open('example.txt', 'r', encoding='utf-8') as file:
    #while(True):
    #    line = file.readline()
    #    if line=='':
    #        break
    #    lines.append(line)
#print(lines)

#lines = []
#with open('example.txt', 'r') as file:
#    for line in file:
#        lines.append(line.strip('\n'))

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.PI = 3.141592
    def getCircumference(self):
        result = 2 * self.PI * self.radius
        return result
    def getArea(self):
        result = self.PI * self.radius**2
        return result

small_circle = Circle(1)
a=small_circle.getCircumference()
b=small_circle.getArea()
print(a,b)

big_circle = Circle(10)
c=big_circle.getCircumference()
d=big_circle.getArea()
print(c,d)