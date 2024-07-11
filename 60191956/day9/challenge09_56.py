# 프로그램 : 함수 정의와 호출
# 작 성 자 : 이형석, 2024-07-04

# 도전문제 1번 : 정수 2개를 입력 받아 총합을 계산한 후, 계산 결과 출력하는 함수
def sum_two_integer(num1, num2):
    result = num1 + num2
    print(f'사용자가 입력한 두 정수 {num1}과 {num2}의 합은 {result}이다.', end='\n\n')

a=int(input('첫 번째 정수 입력: '))
b=int(input('두 번째 정수 입력: '))
sum_two_integer(a,b)

# 도전문제 2번 : 화씨온도를 입력 받아서 섭씨온도 계산 후 화면에 출력
def fahrenheit_to_celsius(fahrenheit):
    C = (fahrenheit-32)*5/9
    return C

F = int(input('변환하고자 하는 화씨온도? '))
C = fahrenheit_to_celsius(F)
print(f'화씨 {F}도는 섭씨 {C} 도', end='\n\n')

# 도전문제 3번 : 반지름과 높이 입력 받아 원기둥 부피 계산한 후 계산 결과 화면에 출력
def get_real(prompt):
    tmp = float(input(prompt))
    return tmp
def get_volume_cylinder(radius, height):
    result = radius**2*3.14*height
    return result

radius = get_real('원기둥 밑면 원의 반지름은? ')
height = get_real('원기둥의 높이는? ')
result = get_volume_cylinder(radius, height)
print(f'원기둥의 부피는 {result}')