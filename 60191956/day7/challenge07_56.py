# 프로그램 : 반복문 복습 - while, for
# 작 성 자 : 이형석, 2024-07-02

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
