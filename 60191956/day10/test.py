from random import randint
result = 0
for i in range(2):
    result += randint(1,6)
print(result)


#import dice

List = []
for i in range(6):
    data =randint(1,45)
    List.append(data)
print(*List)

x = randint(1,15)
if x%3==1:
    print('빨')
elif x%3==2:
    print('파')
else:
    print('노')

    