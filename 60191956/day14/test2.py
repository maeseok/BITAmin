def load_file(file_path):
    List=[]
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tmp = line
            List.append(tmp.strip('\n'))
    return List
def print_List(p):
    for i in p:
        print(i)

#file_path = input('파일 경로 ')
#List = load_file(file_path)
#print_List(List)

def add_list(p):
    while True:
        data = input('새로운 물건 ')
        if data=='':
            break
        p.append(data)
    return p
#List = add_list(List)
#print(List)

def save_file(p, file_path):
    with open(file_path, 'w') as file:
        for i in p:
            file.write(i+'\n')
    print('저장 완료')
#save_file(List,file_path)


def load_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        List=[]
        for line in file:
            List.append(line.strip('\n'))
    return List
def sum_List(p):
    result = 0
    for i in p:
        result += int(i)
    print(result)
    return result
def add_numbers(p):
    while True:
        num = input()
        if num=='':
            break
        p.append(num)
    return p
def append_file(avg, file_path):
    with open(file_path, 'w') as file:
        file.write(str(avg))
    print('저장')

file_path = input('파일 경로 ')
List = load_file(file_path)
sum_List(List)
List = add_numbers(List)
Sum = sum_List(List)
avg = Sum/len(List)
append_file(avg, file_path)
