# 프로그램 : 함수 정의와 호출
# 작 성 자 : 이형석, 2024-07-04

# 함수 정의
def show_message():
    print('hello world')
    print('good job!')

print('시작')
show_message()
print('마침')

def plus(v1, v2):
    result=0
    result=v1+v2
    return result

print('plus() 함수 실행')
sum = plus(100,200)
print(sum)

def plus2(v1, v2, v3):
    result = 0
    result = v1+v2+v3
    return result

sum2 = plus2(100,200,300)
print(sum2)

def show_message(msg, name):
    print(msg, name, '님')
print('시작')
show_message('안녕', '이찬수')
print('마침')

def show_message(msg, name):
    print(msg, name, '님')
    return 'good bye!!'
print('시작')
ret = show_message('안녕', '이찬수')
print(ret)
print('마침')

def plus3(v1, v2, v3):
    return v1+v2+v3

sum = plus3(3,4,5)
print(sum)

def make_message():
    name = input('당신의 이름은? ')
    msg = '반가워요' + name
    print(msg)

def make_message(name):
    msg = '반가워요' + name
    print(msg)

def make_message():
    name = input('당신의 이름은? ')
    msg = '반가워요' + name
    return msg

def make_message(name):
    msg = '반가워요' + name
    return msg 
input_name = input('이름을 입력하시오: ')
result = make_message(input_name)
print(result)
#print(msg)


def first():
    msg = '안녕'
    print(msg)
    second()
    print(msg)

def second():
    msg='반가워'
    print(msg)
first()

# 실습문제 3번 : 반지름 전달받아 원의 넓이 계산하여 반환하는 함수 작성
def show_circle_area(radius):
    area = radius**2*3.14
    return area

while(True):
    radius = int(input('넓이를 구하고자 하는 원의 반지름은?: '))
    if radius==-1:
        break
    area = show_circle_area(radius)
    print(f'반지름 {radius}인 원의 넓이: 3.14*{radius}*{radius}={area}', end='\n\n')