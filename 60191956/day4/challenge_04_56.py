# 프로그램 : 입력, 형변환, 문자열 포매팅, split을 활용한 프로그램
# 작 성 자 : 이형석, 2024-06-27

#도전 문제 1번 - 학번과 이름을 _로 구분하여 분리해서 출력
#studentNumber, name =input("학번과 이름을 _로 구분하여 입력: ").split("_")
studentNumber = input("학번: ")
name = input("이름: ")
result = studentNumber+"_"+name
print("학번과 이름은",result)

#도전 문제 2번 - 반지름을 입력 받아 원의 넓이 계산 후 출력
radius = float(input("원의 반지름은? "))
area = radius**2*3.14
print(f'반지름 {radius}인 원의 넓이는 {area:.2f}입니다.',end="\n\n")