# 프로그램 : 변수/연산자/조건문 연습 
# 작 성자 : 이형석, 2024-06-28

#[1] 변수 선언 - 사용자 입력
name = input("이름을 입력하시오: ")
year = int(input("현재 년도를 입력하시오: "))
math_score1, math_score2, math_score3 = map(int,input("최근 3회의 수학 점수를 입력하시오: ").split())
english_score1, english_score2, english_score3 = map(int,input("최근 3회의 영어 점수를 입력하시오: ").split())
previous_average = float(input("이전 평균을 입력하시오: "))

#[1] 변수 선언 - 과목점수들의 총점과 평균 계산 및 출력
sum_score = float(math_score1 + math_score2 + math_score3 + english_score1 + english_score2 + english_score3)
avg_score = sum_score / 6

# 보고서 출력 [1]
print('\n' + ' - '*15 + '보고서' + ' - '*15)
print(f'이름 : {name:^30s}')
print(f'수학 점수1 : {math_score1:<5d}, 수학 점수2 : {math_score2:<5d}, 수학 점수3 : {math_score3:<5d}')
print(f'영어 점수1 : {english_score1:<5d}, 영어 점수2 : {english_score2:<5d}, 영어 점수3 : {english_score3:<5d}')
print(f'평균 : {avg_score:.2f} 점')

#[2] 성적 등급 값 결정 및 출력
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

# 보고서 출력 [2]
print(f'등급 : {Grades}')

#[3] 장학금 조건 설정 후 장학금 결정 및 금액 출력
scholarship = 0
if Grades == 'A' or (Grades == 'B' and avg_score>=previous_average+5):
    scholarship = 2000000

# 보고서 출력 [3]
print(f'장학금 : {scholarship:,}원')

#[4] 현재 년도를 다 합한 값이 짝수 인지 판단 및 출력
tmp_year = str(year)
sum_year = int(tmp_year[0]) + int(tmp_year[1]) + int(tmp_year[2]) + int(tmp_year[3])
if sum_year %2 == 0:
    res = '짝수'
else:
    res = '홀수'
# 보고서 출력 [4]
print(f'태어난 년도를 다 합치면 {sum_year}로 {res} 이다.')

# 보고서 마무리
print(' - '*33 + '\n')

#[5] 명지 투데이 - 문자열 메소드 연습 및 출력
text = '''
    명지대학교(총장 유병진)가 22일 서울 서대문구 바비엥2교육센터 그랜드볼룸에서 전국의 수험생, 학부모, 교사들을 대상으로 ‘MJ대입공감’ 1차 행사를 개최했다.
이번 행사는 대입을 준비하는 수험생과 학부모, 교사들에게 무전공(자율전공) 모집단위 도입 등 2025학년도 대입의 주요 트렌드와 함께 수시모집 지원전략에 관한 구체적인 정보를 제공하기 위해 마련되었으며, 온라인으로도 참여할 수 있어 정보 소외지역을 포함한 전국 각지의 수험생, 학부모, 교사들의 주목을 받았다.
행사는 이정환 명지대 입학처장의 환영사를 시작으로 △2025학년도 대입 트렌드 및 수시모집 지원전략 △2025학년도 명지대학교 전형 안내 및 지원전략 순으로 진행되었다.
이정환 명지대 입학처장은 환영사를 통해 “이번 MJ대입공감 1차 행사는 자율전공·광역 모집단위의 신설 등 대입 전형의 큰 변화 속에서 전국의 수험생들과 학부모, 교사들에게 정확하고 구체적인 정보를 드리고자 준비했다”며 “앞으로도 명지대학교 입학처는 교육 수요자의 니즈에 맞춘 양질의 대입 정보를 제공하여 전국의 많은 수험생과 학부모들에게 도움이 되고자 한다”고 전했다.
한편, 명지대학교는 대대적인 학사구조개편을 통해 2025학년도 입학정원의 약 50%를 자율전공·광역모집으로 선발하며, 미래 첨단 산업 분야의 인재 양성을 위해 경상·통계학부 응용통계학전공과 융합소프트웨어학부 인공지능전공을 신설하는 등 새로운 변화를 시도한다.
명지대학교 입학처 인재발굴팀은 공정하고 투명한 입학전형 운영을 위해 위촉사정관·전임사정관의 평가 전문성 교육을 실시하고 있으며, MJ대입공감, MJ교사연수, MJ대입포럼 등 교육 현장에 도움이 되는 다양한 프로그램을 운영하여 수험생과 학부모의 입시 부담 완화에 기여하고 있다.
'''
find_data = text.find('입학처',10)
count_data = text.count('명지대')
index_data = text.index('수험생')
print(f'text에서 10 이후 입학처의 첫 위치 : {find_data}')
print(f'text에서 \'명지대\'의 개수 : {count_data} 개')
print(f'text에서 \'수험생\'의 첫 위치 : {index_data}')