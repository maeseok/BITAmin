# 프로그램 : 함수 & 모듈 도전문제
# 작 성 자 : 이형석, 2024-07-05

from random import randint

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