# 프로그램 : 문자열을 처리하는 함수를 만들고 모듈화
# 작 성 자 : 이형석, 2024-07-05

# <1> size 함수
def Size(message):
    print(f'문자열의 길이: {len(message)}')

# <2> exist 함수
def Exist(message, data):
    print(f'문자열 속 {data} 존재 여부: {data in message}')
          
# <3> count 함수
def Count(message, data):
    print(f'문자열 속 {data}의 개수: {message.count(data)}')