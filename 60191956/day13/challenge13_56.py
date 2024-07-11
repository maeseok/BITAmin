## 프로그램 : 리스트, 튜플, 딕셔너리 프로그래밍 실습
## 작 성 자 : 이형석, 2024-07-10

# 실습문제 1번 : 정수 4개 입력받아 리스트에 저장한 후 화면에 출력
def input_List():
    List = []
    for i in range(4):
        num = int(input(f'{i+1}번째 정수: '))
        List.append(num)
    return List
def print_List(p):
    for i in range(len(p)):
        print(f'리스트의 {i+1}번째 요소 {p[i]}')

#List = input_List()
#print_List(List)
#print()

# 실습문제 2번 : 2X2 크기 행렬 입력받아 리스트에 저장 후 출력
List2 = []
for i in range(2):
    tmp = []
    for j in range(2):
        num = int(input(f'{i+1}행 {j+1}열 저장될 자료: '))
        tmp.append(num)
    List2.append(tmp)
for i in range(len(List2)):
    print(*List2[i])
print()


# 실습문제 3-1번 : 빈 딕셔너리에 사용자로부터 입력받은 값 추가하는 프로그램
def comp_dic(dic):
    while(True):
        student_number = input('학생의 학번: ')
        if student_number == '0':
            break
        student_name = input('학생의 이름: ')
        dic[student_number] = student_name
#dic={}
#comp_dic(dic)

# 실습문제 3-2번 : 사용자가 입력한 학번에 해당하는 이름을 출력하는 프로그램
def find_dic(dic):
    find_student = input('학번을 입력하시오: ')
    if find_student not in dic.keys():
        print('해당 학번 존재하지 않음')
        return False
    print(f'{find_student}학번 학생의 이름은 {dic[find_student]}이다.')

#dic={}
#comp_dic(dic)
#find_dic(dic)
#print()

# 도전문제 1번 : 정수 4개 입력받아 리스트에 저장 후 자료의 총합 계산 후 출력
def input_List():
    List = []
    for i in range(4):
        num = int(input(f'{i+1}번째 정수: '))
        List.append(num)
    return List
def sum_List(p):
    result = 0
    for i in range(len(p)):
        result += p[i]
    return result

#List = input_List()
#result = sum_List(List)
#print(f'리스트 내 모든 요소의 총합: {result}')
#print()

# 도전문제 2번 : 2x2 크기 행렬 입력받아 저장한 후 각 행의 합을 출력
List2 = []
for i in range(2):
    tmp = []
    for j in range(2):
        num = int(input(f'{i+1}행 {j+1}열 저장될 자료: '))
        tmp.append(num)
    List2.append(tmp)
for i in range(len(List2)):
    result = 0
    for j in range(len(List2[i])):
        result += List2[i][j]
    print(f'{i+1}행 자료의 총합: {result}')
print()

# 도전문제 3번 : 사용자가 입력한 학번에 해당하는 이름 삭제 후 출력
def del_dic(dic):
    del_student = input('삭제할 학생의 학번을 입력하시오: ')
    if del_student not in dic.keys():
        print('해당 학번 존재하지 않음')
    del dic[del_student]

dic={}
comp_dic(dic)
del_dic(dic)
print(f'현재 딕셔너리: {dic}')









        
                               
