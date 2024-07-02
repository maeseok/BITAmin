# 프로그램 : 문자열 인덱싱 슬라이싱 포매팅 함수/메소드
# 작 성 자 : 이형석, 2024-06-28

msg = 'abcdefghij'
print(msg[0])
print(msg[-1])
print(msg[2:5])

print(msg[2:10])
print(msg[2:])

print(msg[2:10:1])
print(msg[::])
print(msg[::2])
print(msg[::-1])

letters= 'happy prince'
print(letters[-7:-12:-1])

text = "20200430Rainy"
year = text[:4]
month = text[4:6]
day = text[6:8]
weather = text[8:]
print(f'{year} {month} {day} {weather}')

#주의
a="Pithon"
a=a.replace("i","y")
print(a)

print('*'*5)
print(5*'*')
print(4*'*'*5)

name = 'alice'
age = 30

greeting = f'Hello, {name}! You are {age} years old.'
print(greeting)

num = 15
print(f'number={num}')
print(f'number={num:d}')
print(f'number={num:5d}')
print(f'number={num:<5d}')
print(f'number={num:^5d}')
print(f'number={num:05d}')

PI = 3.14159265

print(f'[{PI}]')
print(f'[{PI:f}]')
print(f'[{PI:e}]')
print(f'[{PI:.2f}]')
print(f'[{PI:5.2f}]')
print(f'[{PI:<5.2f}]') #왼쪽 정렬

text= 'python'
print('t' in text)
print('T' in text)
print('th' in text)
print('E' not in text)

print(type(text))# 변수의 자료형 리턴하는 함수
print(len(text))# 변수의 문자 갯수를 정수로 반환

#a = "life is too short"
#print(a.split())
#a= input("년 월 일 날씨를 입력하시오 ")
#w1, w2, w3, w4 = a.split('/')
#print(f'w1={w1}, w2={w2}, w3={w3}, w4={w4}')

week = '월화수목금금금'
n = week.count('금')
print(f'\'금\'의 개수: {n}')

pos = week.find('금')
print(f'{week}의 금의 위치 : {pos}')

pos = week.find('금',5)
print(f'{week}의 5이후의 금의 위치 : {pos}')

#first = int(input("첫번째 자료를 입력하세요: "))
#second = int(input("두번째 자료를 입력하세요: "))
#ds = first>=second
#print("첫번째 숫자가 두번째 숫자보다 큰가: ",ds)

#first = int(input("첫번째 자료를 입력하세요: "))
#second = int(input("두번째 자료를 입력하세요: "))
#ds = first==second
#print("첫번째 숫자와 두번째 숫자가 같은가: ",ds)

# 논리연산 - and, or, not
age = int(input('당신의 나이는? '))

result = age>=0 and age<=120
print(f'{age}은(는) 유효한 나이인가? {result}')

result = age<0 or age>150
print(f'{age}은(는) 유효한 나이가 아닌가? {result}')
print(f'{age}은(는) 유효한 나이인가? {not result}')

num1 = int(input('첫 번째 점수는? '))
num2 = int(input('두 번째 점수는? '))

if num1 > num2:
    print(f'{num1}은(는) {num2} 보다 크다')
    print('크다')
print('end')

age = int(input("나이를 입력하시오: "))
toeic = int(input("토익점수를 입력하시오: "))
if age<=30 or toeic >=800:
    print("입사가능.")
else:
    print("입사불가능")
print("프로그램 종료.")

score = int(input("점수를 입력하시오:")) 
if score >= 90: 
    print('A학점 입니다.') 
elif score >= 80: 
    print('B학점 입니다.') 
elif score >= 70: 
    print('C학점 입니다.') 
elif score >= 60: 
    print('D학점 입니다.') 
else: 
    print('F학점 입니다.')