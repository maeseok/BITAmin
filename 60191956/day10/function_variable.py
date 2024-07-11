# 프로그램 : 함수 & 모듈
# 작 성 자 : 이형석, 2024-07-05

def sum(num1, num2):
    result = num1 + num2
    return result

sumvalue = sum(100,200)
print(sumvalue)

# << 리턴값이 없는 유형 >>
def make_message():
    name = input('name? ')
    message = '반가워요' + name
    print(message)

print('start')
make_message()
print('end')

def make_message(name):
    message = '반가워요' + name
    print(message)

print('start')
name = input('name? ')
make_message(name)
print('end')

def make_message(name):
    message = '반가워요' + name
    return message

print('start')
name = input('name? ')
result = make_message(name)
print(result)
print('end')

# 전역변수와 지역변수의 이름이 같을 때
# 함수에서 지역변수 사용하는 경우 - 문제x, 전역변수 값이 사용
# 함수에서 전역변수와 같은 이름의 지역변수 할당 - 문제o, 이름은 같아도 서로 다른 존재

def get_circle_area(radius):
    global area
    area = 3.14*radius**2 # 지역변수
    print(f'함수내 area: {area}')
r = float(input('넓이를 구할 원의 반지름은? '))
area = 0 # 전역변수
get_circle_area(r)
print(f'주 프로그램에서 area: {area}')