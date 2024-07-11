# 프로그램 : 파일 입출력, 클래스와 객체 실습
# 작 성 자 : 이형석, 2024-07-11

# 실습문제 1번 : 텍스트 파일 읽어 리스트에 저장 후 화면에 출력
def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tmp = file.read().split('\n')
    return tmp
def print_List(p):
    for item in p:
        print(item)
file_path = input('파일 경로를 입력하시오: ')
List = load_file(file_path)
print_List(List)

# 실습문제 2번 : 1번 통해 생성된 리스트에 아무것도 입력받지 않을 때까지 아이템 추가
def add_list(p):
    while True:
        item = input('새로 구입한 물건 입력: ')
        if item=='':
            break
        p.append(item)
    return p
List = add_list(List)

# 실습문제 3번 : 2번 문제 통해 생성된 리스트 새로운 파일에 저장
def save_file(p, file_path):
    with open(file_path, 'w') as file:
        for item in p:
            file.write(item+'\n')
        print('파일에 저장 완료!')
save_file(List, file_path)

# 도전문제 1번 : 텍스트 파일 읽어 리스트에 저장 후, 자료의 총합 계산
def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tmp = file.read().split('\n')
    return tmp
def sum_List(p):
    result = 0
    for i in p:
        result += int(i)
    print(f'총합: {result}')
file_path = input('파일 경로를 입력하시오: ')
List = load_file(file_path)
sum_List(List)

# 도전문제 2번 : 1번 문제 통해 생성된 리스트에 아무것도 입력 받지 않을 때까지 숫자 추가
def add_numbers(p):
    while(True):
        data = input('추가할 숫자: ')
        if data=='':
            break
        p.append(data)
    return p
List = add_numbers(List)

# 도전문제 3번 : 2번 문제 통해 생성된 리스트의 평균 파일에 추가
def avg_List(p):
    result = 0
    for i in p:
        result += int(i)
    avg = result / len(p)
    return avg
def append_file(avg, file_path):
    with open(file_path, 'w') as file:
        file.write(str(avg))
    print('파일에 저장 완료!')
avg = avg_List(List)
append_file(avg, file_path)

