# 프로그램 : input과 형변환을 이용해 값을 입력받아 문제 해결하기
# 작 성 자 : 이형석, 2024-06-26

#산술 대입 연산 연습문제
x = int(input('자료를 입력하시오: '))
add = x +10
print(add)

radius = float(input('반지름을 입력하시오: '))
area = (radius**2)*3.141592
print(area, end='\n\n')

#실습문제 1번 - 두 정수 입력의 연산
num1, num2 = map(int, input('정수 2개를 입력해주세요 : ').split())
sum = num1 + num2
print('정수 2개의 합 : ', sum, end='\n\n')

#실습문제 2번 - 화씨온도 섭씨온도로 변환
F_temp = int(input('변환하고자 하는 화씨온도? ')) 
C_temp = (F_temp-32)*5/9
print('화씨 100도는 섭씨 ',C_temp, '도', end='\n\n')

#실습문제 3번 - 초를 입력받아 시-분-초로 출력
time = int(input('변환하고자 하는 시간(초)? '))
Time = time
Hours = time // 3600; time%=3600
Minutes = time // 60; time%=60
Seconds = time
print(Time, '초는', Hours, '시간', Minutes, '분', Seconds, '초이다.', end='\n\n')

#도전 문제 1번 - 숫자 3개 입력받아 평균 출력
num1 = int(input('첫번째 수 : '))
num2 = int(input('두번째 수 : '))
num3 = int(input('세번째 수 : '))
sum = num1 + num2 + num3
avg = sum / 3
print('평균: ',avg, end='\n\n')

#도전 문제 2번 - 평단위 값을 제곱미터 값으로 계산
square_footage = float(input('변환하고자 하는 평수는? '))
square_meter = square_footage * 3.305785
print(square_footage, '평은', square_meter, '제곱미터', end='\n\n')

#도전 문제 3번 - 금액을 입력받아 동전의 개수를 출력
money = int(input('동전으로 교환하고자 하는 금액은? '))
count_500won = money // 500; money %= 500
count_100won = money // 100; money %= 100
count_50won = money // 50; money %= 50
count_10won = money // 10; money %= 10

print('500원 동전의 개수: ', count_500won)
print('100원 동전의 개수: ', count_100won)
print('50원 동전의 개수: ', count_50won)
print('10원 동전의 개수: ', count_10won)