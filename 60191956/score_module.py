# 프로그램 : MJU 성적 프로그램 함수 정의
# 작 성 자 : 이형석, 2024-07-05

# <2> 평균 계산
def average_cal(math, english):
    avg = (math+english)/2
    return avg

# <3> 학점 계산
def grade_cal(avg_score):
    if avg_score >= 90:
        Grades = 'A'
    elif avg_score >= 80:
        Grades = 'B'
    elif avg_score >= 70:
        Grades = 'C'
    elif avg_score >= 60:
        Grades = 'D'
    else:
        Grades = 'F'
    return Grades

# <4> 장학금 여부
def scholarship_check(Grades, avg_score, previous_average):
    scholarship = 0
    if Grades == 'A' or (Grades == 'B' and avg_score>=previous_average+5):
        scholarship = 2000000
    return scholarship

# <5> 프린트
def print_program(avg, Grades, scholarship):
    print(f'평균은 {avg} 입니다.')
    print(f'학점은 {Grades} 입니다.')
    print(f'장학금은 {scholarship:,}원 입니다.')