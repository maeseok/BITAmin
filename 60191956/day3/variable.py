# 프로그램 : 변수 연습, 표준 출력/입력 연습
# 작 성 자 : 이형석, 2024-06-26

''' 프로그램 :
    변수 ... '''

strName = '''중국어
 수업
 기본'''

print(strName)

var2 = 200
var1 = var2
var1 = 100 + 100 #오른쪽에 
var1 = var1 + 100
var1 = var2 = var3 = var4 = 100

#type() 함수 - 변수의 타이(정수, 실수, 불 등)
boolVar = True
print(type(boolVar))

nStudent, nProfessor = 9, 3
print(nStudent)
print(nProfessor)

boolVar = True
intVar = 0

boolVar, intVar = True, 0
print('boolVar', '=', boolVar)
print('intVar', '=', intVar)

#print('intVar'+'='+ intVar) TypeError

#print 키워드 인수 sep
print('안녕', '여러분')
# sep - 디폴트로 안하고 .. 선택
print('안녕', '여러분', sep=',')
print('안녕', '여러분', sep='###')
# end - 디폴트로 안하고 .. 선택
print('안녕', '여러분', end='!!!\n') #default - \n
print('파이썬 세계에 오신 것을 환영합니다.')

# 표준 입력 함수 input()
#print('당신의 이름은 ?', end='')
#name = input()
#print(name)

name = input('당신의 이름은? ')
print('반가워요!!', name)

# 숫자 입력 - int() 함수를 이용해서 문자 변환
n1 = input('정수를 입력하세요 : ')
n1 = int(n1)
print('n1= ', n1)

n2 = int(input('정수를 입력하세요 : '))
print('n2= ', n2)

fNum = float(input('실수를 입력하세요 : '))
print('fNum= ', fNum)