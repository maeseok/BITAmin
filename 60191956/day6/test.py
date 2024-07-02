Time = 5000
while(Time>=3600):
    Time = int(input('변환하고자 하는 시간(초)? '))
    time = Time

    hours = Time // 3600; Time %= 3600
    minutes = Time // 60; Time %= 60
    seconds = Time % 60
    print(f'{time}초는 {hours}시간 {minutes}분 {seconds}초이다.')
if(Time<3600):
    print('환산불가 시간 입력으로 프로그램 종료', end='\n\n')