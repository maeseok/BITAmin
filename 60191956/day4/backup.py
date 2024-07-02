# 프로그램 : 
# 작 성 자 : 이형석, 2024-06-27

#실습문제 1번 - 문장 출력
#print('\"파이썬 입문 수강생은 \'명지 \'학생 입니다.\"',end='\n\n')
msg = input()
msg_slice1 = msg[3:6]
msg_slice2 = msg[::3]
print('%'*30)
print(msg_slice2)
print('%'*30)
#학점 입력?
score = float(input("학점: "))

#msg + 학점 출력
print(msg,"학점은",str(score))


#실습문제 2번 - 이름 입력받고 성과 이름 분리
fullName = input('당신의 이름을 입력하시오: ')
firstName = fullName[:1]  
lastName = fullName[1:]

print("성: ", firstName)
print("이름: ", lastName, end="\n\n")

#실습문제 3번 - 신장과 체중을 입력받아 BMI 계산 후 출력
weight = float(input('몸무게를 kg단위로 입력: '))
height = float(input('키를 미터 단위로 입력: '))
BMI = weight/height**2
print(f'{weight}kg몸무게와 {height}m키의 BMI: {BMI:.2f}', end="\n\n")

#도전 문제 1번 - 학번과 이름을 _로 구분하여 분리해서 출력
studentNumber, name =input("학번과 이름을 _로 구분하여 입력: ").split("_")
print(f'학번: {int(studentNumber):8d}')
print("이름: "+name, end="\n\n")

#도전 문제 2번 - 반지름을 입력 받아 원의 넓이 계산 후 출력
radius = float(input("원의 반지름은? "))
area = radius**2*3.14
print(f'반지름 {radius}인 원의 넓이는 {area:.2f}입니다.',end="\n\n")

#도전 문제 3번 - 이름과 학년을 입력 받아 하나의 문자열로 연결하여 출력
Name = input("이름: ")
grade = int(input("학년: "))
print(f'{Name}은(는) 내년에 {grade+1}학년입니다.', end="\n\n")