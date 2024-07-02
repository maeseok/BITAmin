# 프로그램 : input으로 값을 입력받아 각각의 문제 해결 후 출력하기
# 작 성 자 : 이형석, 2024-06-26

num1, num2 = map(int, input("정수 2개를 입력해주세요 : ").split())
sum = num1 + num2
print("정수 2개의 합 : ", sum)

F_temp = int(input("변환하고자 하는 화씨온도? ")) 
C_temp = (F_temp-32)*5/9
print("화씨 100도는 섭씨 ",C_temp, "도")

time = int(input("변환하고자 하는 시간(초)? "))
Time = time
Hours = time // 3600; time%=3600
Minutes = time // 60; time%=60
Seconds = time
print(Time,"초는", Hours, "시간", Minutes, "분", Seconds, "초이다.")