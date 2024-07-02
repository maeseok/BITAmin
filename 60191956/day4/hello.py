# 프로그램 : 키보드 입력, 변환, 연산자 연습
# 작 성 자 : 이형석, 2024-06-27

# 1. -숫자 세 개 입력 받아 평균 계산 후 화면 출력
num1 = int(input('첫번째 수 : '))
num2 = int(input('두번째 수 : '))
num3 = int(input('세번째 수 : '))
sum = num1 + num2 + num3
avg = sum / 3
print('평균: ',avg, end='\n\n')

# 2. - 입력한 평단위 값을 제곱미터로 계산 후 화면 출력
square_footage = float(input('변환하고자 하는 평수는? '))
square_meter = square_footage * 3.305785
print(square_footage, '평은', square_meter, '제곱미터', end='\n\n')
#print(square_footage+ '평은'+ square_meter+ '제곱미터', end='\n\n') TypeError

# 3. - 동전 교환 문제
money = int(input('동전으로 교환하고자 하는 금액은? '))
count_500won = money // 500; money %= 500
count_100won = money // 100; money %= 100
count_50won = money // 50; money %= 50
count_10won = money // 10; money %= 10

print('500원 동전의 개수: ', count_500won)
print('100원 동전의 개수: ', count_100won)
print('50원 동전의 개수: ', count_50won)
print('10원 동전의 개수: ', count_10won)