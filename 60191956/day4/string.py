# 프로그램 : 문자열 생성, 인덱싱/슬라이싱, 연산, 포매팅, 내장함수, 메소드
# 작 성 자 : 이형석, 2024-06-27

# 1. 문자열 생성- 한 줄 생성
message1, message2 = 'hello', 'Hello'
print(message1)
print(message2)
print("우리는 '파이썬'을 프로그램한다")
print('우리는 "파이썬"을 프로그램한다')
print("우리는 \"파이썬\"을 프로그램한다")
print("우리는\t여기서 \"파이썬\"을 \n프로그램한다")
print('11\t홍길동\n22\t일지매')
print('우리는 파이썬을 \
      프로그램합니다.')
print(" ")

print('''우리는
"파이썬"을
'프로그램'합니다.
''')

msg = 'hello'
print(msg)
print(msg[0])
print(msg[-1])
print(msg[1:])

# sub= ell
sub = msg[1]+msg[2]+msg[3]
print(sub)

slice1 = msg[1:4]
print(slice1)

# 슬라이싱에는 시작점, 끝점 디폴트

slice2 = msg[0:3]
slice3 = msg[:3]

slice4 = msg[3:5]
slice5 = msg[3:]

print(slice2, slice3)
print(slice4, slice5)

slice6 = msg[0:5:1]
slice7 = msg[0:5:2]

print("step=1 : ",slice6)
print("step=2 : ",slice7)
print(msg[::2]) #처음부터 끝까지 홀수번째 출력

print('*'*20)
print("    보고서      ")
print(20*'*')
print(5*'*'*4)

name = "alice"
age = 30
greeting = "hello "+name + " you are "+ str(age) + " years old"
print(greeting)
greetingFormatted = f"hello {name} you are {age} years old" 
print(greetingFormatted)

#f-string 연습
today = "wednesday"
message = f"Happy {today}!"
print(message)

num1 = 5 
num2 = 3

sumMessage = f"the sum of {num1} and {num2} is {num1+num2}"
print(sumMessage)

num = int(input('정수는? '))

print(f'2진 표현으로는 {num:b}입니다.')
print(f'10진 표현으로는 {num:d}입니다. ')
print(f'16진 표현으로는 {num:x}입니다. ')

n1 = int(input('첫 번째 정수는? '))
n2 = int(input('두 번째 정수는? '))

avg = n1 / n2
print(f'{n1} / {n2} = {avg}')
print(f'{n1} / {n2} = {avg:f}')
print(f'{n1} / {n2} = {avg:e}')
print(f'{n1} / {n2} = {avg:g}')

num = 15
print(f'[{num:d}]')
print(f'[{num:5d}]')
print(f'[{num:<5d}]')
print(f'[{num:^5d}]')
print(f'[{12345678:5d}]')
print(f'[{num:05d}]')

PI = 3.14159265

print(f'[{PI:f}]')
print(f'[{PI:.2f}]')
print(f'[{PI:5.2f}]')
print(f'[{PI:2g}]')

#실습문제 1번 - 문장 출력
#print('\"파이썬 입문 수강생은 \'명지 \'학생 입니다.\"',end='\n\n')
msg = input()
msg_slice1 = msg[3:6]
msg_slice2 = msg[::3]
print(msg_slice1)
print(msg_slice2)
print('%'*30)

score = float(input("학점: "))
#msg + 학점 출력
print(msg+" 학점은 "+str(score)+"입니다.")