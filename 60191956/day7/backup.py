# 프로그램 : 반복문 복습 - while, for
# 작 성 자 : 이형석, 2024-07-02

# 실습문제 1번 : 정수 1개를 입력받아 팩토리얼 계산 후 출력
n = int(input('정수 1개를 입력하시오: '))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(f'입력한 정수 {n}!은 {factorial}이다.', end='\n\n')

# 실습문제 2번 : 2!~5! 계산 결과 출력
factorial2 = 1
for i in range(2,5+1):
    for j in range(1,i+1):
        factorial2 *= j
    print(f'{i}!의 결과: {factorial2}')
    factorial2 = 1
print()

# 실습문제 3번 : a,b 입력받아 조건 만족하는 값 출력
while(True):
    a = int(input('첫 번째 정수를 입력하시오: '))
    b = int(input('두 번째 정수를 입력하시오: '))
    if (1<=a and a<=100) and (1<=b and b<=100):
        for i in range(1,100+1):
            if i%a==0 and i%b!=0:
                print(f'{i},',end=' ')
        break
print(end='\n\n')

# 실습문제 4번 : n을 입력받아 1부터 n까지 홀수와 짝수의 총합 계산 후 출력
num = int(input('정수 1개를 입력하시오: '))
sum_even = 0
sum_odd = 0
for i in range(1,num+1):
    if i%2==0:
        sum_even += i
    else:
        sum_odd += i
print(f'홀수의 합은 {sum_odd}, 짝수의 합은 {sum_even}이다.', end='\n\n')

# 실습문제 5번 : 계좌번호를 입력할 때 -를 제거하고 숫자만 나오도록
account_number = input('계좌번호를 입력하시오: ')
result =''
for i in account_number:
    if i!='-':
        result += i
print(f'계좌번호는 {result}입니다.', end='\n\n')

# 도전문제 1번 : 중첩 for문 사용해 구구단 2,5,8단 출력
for i in range(2,8+1,3):
    for j in range(1,9+1):
        print(f'{i}*{j}={i*j}')
    print()

# 도전문제 2번 : n을 입력받아 1부터 n까지 조건 만족하는 총합 출력
number = int(input('정수 1개를 입력하시오: '))
Sum = 0
for i in range(1,number+1):
    if i%3==0 and i%7!=0:
        Sum += i
print(f'3의 배수면서 7의 배수가 아닌 수의 총합은 {Sum}다.', end='\n\n')

# 도전문제 3번 : 2~10사이 입력받아 특정 조건에 맞는 값 출력
while(True):
    Number = int(input('2~10사이의 정수 1개를 입력하시오: '))
    if 2<=Number and Number<=10:
        for i in range(2,Number+1,2):
            factorial3 = 1 
            for j in range(1,i+1):
                factorial3 *= j
            print(f'{i}!은 {factorial3}다. ')
        break
