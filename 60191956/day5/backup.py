# 프로그램 : 제어구조와 조건평가식을 활용한 문제 해결
# 작 성 자 : 이형석, 2024-06-28

# 실습문제 1번 - 홀수, 짝수 판단
number = int(input('정수를 입력하시오: '))
if number%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
print("프로그램 종료.", end="\n\n")

# 실습문제 2번 - 윤년 판단 
year = int(input('년도를 입력하시오: '))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f'{year}은 윤년입니다.')
else:
    print(f'{year}은 윤년이 아닙니다.')
print("프로그램 종료.", end="\n\n")

# 실습문제 3번 - 표준 체중 구하고 저체중, 표준, 과체중 판단
height = float(input('당신의 키를 입력하시오: '))
weight = float(input('당신의 몸무게를 입력하시오: '))
standard = (height-100)*0.9

if (standard-3)>weight:
    print("저체중 입니다.")
elif (standard+3)<weight:
    print("과체중 입니다.")
else:
    print("표준체중 입니다.")
print()

# 도전문제 1번 - 0을 기준으로 수식1, 수식2 나누어 출력
input_number = int(input('숫자를 입력하시오: '))
if input_number>0:
    result = input_number**2+2*input_number+1
else:
    result = input_number**3-input_number
print(f'계산결과: {result}', end="\n\n")

# 도전문제 2번 - 3 또는 7의 배수인지 판단 후 출력
Number = int(input('숫자를 입력하시오: '))
if Number%3==0 or Number%7==0:
    print("행운의 숫자")
print("프로그램 종료", end="\n\n")

# 도전문제 3번 - 가창력과 연기력 수치에 따라 4개의 메시지 중 하나 출력
acting = int(input('연습생의 연기력을 입력하시오: '))
singing = int(input('연습생의 가창력을 입력하시오: '))
if singing>=80 and acting >=80:
    print("만능 엔터테이너로서의 자질을 가지고 있습니다.")
elif acting>=80:
    print("배우로서의 자질을 가지고 있습니다.")
elif singing>=80:
    print("가수로서의 자질을 가지고 있습니다.")
else:
    print("연예인으로서의 자질이 없습니다.")