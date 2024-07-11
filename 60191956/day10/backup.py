# 프로그램 : 함수 & 모듈 도전문제
# 작 성 자 : 이형석, 2024-07-05

# 실습문제 1번 : 두 개의 주사위의 합을 출력하는 프로그램
from random import randint
def sum_dice(num1, num2):
    result = num1 + num2
    print(f'두 개의 주사위 눈금의 합: {result}', end='\n\n')
dice1 = randint(1,6)
dice2 = randint(1,6)
sum_dice(dice1, dice2)

# 실습문제 2번 : 주사위 20번 굴려 주사위 눈금 총합 계산
result=0
for i in range(20):
    dice = randint(1,6)
    print(f'{i+1}번째 주사위 눈금: {dice}')
    result += dice
print(f'주사위 20번 굴린 눈금의 총합: {result}', end='\n\n')

# 실습문제 3번 : 두 개의 주사위 합과 사용자가 입력한 숫자만큼 주사위 굴려 총합 출력
def two_dice():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    result = dice1 + dice2
    print(f'두 개의 주사위 눈금의 합: {result}')
def n_rolling_dice(n):
    result = 0
    for i in range(n):
        dice = randint(1,6)
        print(f'{i+1}번째 주사위 눈금: {dice}')
        result += dice
    print(f'주사위 {n}번 굴린 눈금의 총합: {result}',end='\n\n')
two_dice()
num = int(input('주사위를 굴릴 횟수: '))
n_rolling_dice(num)

# 도전문제 1번 : 1~45 사이의 로또 번호 6개 출력
def lotto():
    lotto_number=[]
    for i in range(6):
        number = randint(1,45)
        lotto_number.append(number)
    print('이번주 로또 번호: ')
    print(*lotto_number, end='\n\n')
lotto()

# 도전문제 2번 : 1~15 사이의 숫자를 가진 룰렛 돌려 구슬이 놓인 칸의 색 출력
def roulette():
    number = randint(1,15)
    print(f'선택된 룰렛 번호: {number}')
    if number%3==1:
        print('빨간색 당첨')
    elif number%3==2:
        print('파란색 당첨')
    else:
        print('노란색 당첨')
roulette()
print()

# 도전문제 3번 : 폭과 높이 입력받아 삼각형, 사각형 넓이 계산 후 출력
def area_triangle(height, width):
    area = height*width/2
    print(f'삼각형의 넓이는 {area}')

def area_rectangle(height, width):
    area = height*width
    print(f'사각형의 넓이는 {area}')

Height = int(input('높이 입력: '))
Width = int(input('폭 입력: '))

area_triangle(Height, Width)
area_rectangle(Height, Width)