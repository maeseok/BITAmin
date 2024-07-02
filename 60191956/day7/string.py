# 프로그램 : 반복문 복습 - while, for
# 작 성 자 : 이형석, 2024-07-02

password = ''
while password != '#1234*':
    password = input('암호를 입력하시오')
print('어서 오세요, 문이 열렸습니다. ')

count = 0 # 초기값
while count<5: # 조건
    print(f'{count}')
    count+=1 # 증가

# for 구문 - for 변수 in 순서있는것(시퀀스 - 그룹 - ex:문자열, range, 리스트)
message = 'hello'
for ch in message:
    print(f'{ch}/,',end=' ')
print()

for i in [1,2,3,4,5]:
    print(f'{i} - 방문을 환영합니다.')

for i in ['123','456','789','878']:
    print(f'파이썬 프로그래밍 입문 학생 : {i}')

for i in range(1,10+1): # range 이용해서 범위 지정
    print(f'{i}',end=' ')

for i in [10]:
    print(i)

total = 0
for n in range(1,11): 
    total = total + n
print(f'1부터 10까지 정수의 합은 {total}이다.')

total = 0
cnt=1
while cnt<=10:
    total += cnt
    cnt += 1
print(f'1부터 10까지 정수의 합은 {total}이다.')

while(True):
    a = int(input('첫 번째 정수를 입력하시오: '))
    b = int(input('두 번째 정수를 입력하시오: '))
    if (1<=a and a<=500) and (1<=b and b<=500):
        for Data in range(1, 500+1):
            if Data % a == 0 and Data % b == 0:
                print(f'{Data},',end=' ')
        break

# << 중첩 제어 - for 안에 for >>
for height in range(0,5):
    for width in range(0,4):
        print('*', end='')
    print()

for i in range(1,10):
    for j in range(1,10):
        print(f'{i}X{j}={i*j}')
    print()

while(True):
    pwd=input('비밀번호를 입력하시오: ')
    if pwd=='#1234*':
        print('어서오세요, 문이 열렸습니다!')
        break

# << 보조 제어문 - continue : 반복 구문내에서 .. 바로 다음으로 넘어가는 것 >>
for i in range(0,100):
    if i%2==0:
        continue
    print(i)

# 함수
# <<함수 정의 >>
def show_message():
    print('hello world')
    print('good job')

print('시작')
show_message()
print('마침')

