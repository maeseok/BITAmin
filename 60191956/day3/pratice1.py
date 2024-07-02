# 프로그램 : input과 형변환을 이용해 값을 입력받아 몫과 나머지 구하기
# 작 성 자 : 이형석, 2024-06-26

Dividend = int(input("피젯수를 정수로 입력하세요: "))
Divisor = int(input("젯수를 정수로 입력하세요: "))

Quotient = Dividend // Divisor
Remainder = Dividend % Divisor
print("몫 = ", Quotient)
print("나머지 = ", Remainder)