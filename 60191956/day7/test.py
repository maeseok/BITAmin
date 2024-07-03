name,python,math,preAvg = input('asd').split(' ')
python = int(python)
math = int(math)
preAvg = float(preAvg)
average = (python+math)/2

print('%'*20)
print(f'{name:^20s}')
print(f'{python:<5d}')
print(f'{math:05d}')
print(f'{average:.3f}')

if average>=90:
    if python>=80 and math >=80:
        print(f'평균{average}로 우수 나머지도')
    else:
        print(f'평균{average}로 우수하나, 과목은 분발')
elif average>=70:
    print(f'평균{average}로 보통')
else:
    print(f'평균{average}로 다음 기회에')