List = [i for i in range(1,11)]
print(sum(List))

List = []
result = 0
for i in range(5):
    data = int(input())
    if data%2==0:
        result += data
    List.append(data)

from random import randint
List = []
for i in range(10):
    List.append(randint(1,10))

while True:
    if List.count(3)==0:
        break
    List.remove(3)
