# 프로그램 : for, while문을 활용한 반복제어
# 작 성 자 : 이형석, 2024-07-01

# 실습문제 3번 : 1~100 중 입력한 수의 배수만 출력
while(True):
    Number = int(input('정수를 입력하시오: '))
    if(1<=Number and Number<=100):
        for num in range(Number,100+1,Number):
            print(f'{num},', end=' ')
        break
print(end='\n\n')

# 도전문제 1번 : 초 단위 시간 입력받아 시-분-초 형태로 출력
while(True):
    Time = int(input('변환하고자 하는 시간(초)? '))
    time = Time
    if(Time<3600):
        print('환산불가 시간 입력으로 프로그램 종료', end='\n\n')
        break

    hours = Time // 3600; Time %= 3600
    minutes = Time // 60; Time %= 60
    seconds = Time % 60
    print(f'{time}초는 {hours}시간 {minutes}분 {seconds}초이다.')

# 도전문제 2번 : 0부터 사용자가 입력한 숫자까지 중 홀수만 출력
num = int(input('정수를 입력하시오: '))
for Num in range(1, num+1, 2):
    print(f'{Num},', end=' ')
print(end='\n\n')

# 도전문제 3번 : a,b를 입력받아 1부터 500 이하의 정수 중 a,b의 공배수를 출력
while(True):
    a = int(input('첫 번째 정수를 입력하시오: '))
    b = int(input('두 번째 정수를 입력하시오: '))
    if (1<=a and a<=500) and (1<=b and b<=500):
        for Data in range(1, 500+1):
            if Data % a == 0 and Data % b == 0:
                print(f'{Data},',end=' ')
        break