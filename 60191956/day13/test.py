List=[]
for i in range(2):
    tmp =[]
    for j in range(2):
        data = int(input())
        tmp.append(data)
    List.append(tmp)
    
def comp_dic(dic):
    while True:
        a = input()
        if a=='0':
            break
        b = input()
        dic[a]=b
    return dic

def find_dic(dic):
    a = input()
    if a not in dic.keys():
        print('x')
        return False
    name = dic[a]
    
def del_dic(dic):
    a = input()
    if a not in dic.keys():
        print('x')
        return False
    del dic[a]
    return True
