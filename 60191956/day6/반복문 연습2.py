#!/usr/bin/env python
# coding: utf-8

# ## 프로그램 : 반복문 연습 - while, for 연습
# ## 작 성 자 : 이형석, 2024-07-01

# << while 반복 제어 연습 >>

# In[2]:


pwd = input('비밀번호? ')
while pwd != '#1234*':
    pwd = input('비밀번호? ')
print('어서오세요, 문이 열렸습니다!')


# In[3]:


pwd = ''
while pwd != '#1234*':
    pwd = input('비밀번호? ')
print('어서오세요, 문이 열렸습니다!')


# 횟수 반복 - while 구문으로 할 경우

# In[5]:


count = 0
while count < 5:
    count += 1 
    print(count)


# In[6]:


count = 0 
while count < 10:
    count += 1
    print('hello wolrd')


# << for 변수 in 시퀀스 - 시퀀스가 정수인 이용 예제 >>

# In[10]:


msg = 'hello'
for ch in msg:
    print(f'{ch}')
print('for 구문이 완료되었습니다.')


# << for 변수 in 시퀀스 - 시퀀스가 리스트를 이용 예제 >>

# In[12]:


for i in [1,2,3,4,5]:
    print(f'{i} : 방문을 환영합니다. ')
print('\nfor 구문이 완료되었습니다. ')


# << 구구단 출력 >>

# In[13]:


for i in [1,2,3,4,5]:
    print(f'9 x {i} = {9*i}')


# << for 변수 in 시퀀스 - 시퀀스가 range() 함수 이용 - 초기값, 끝값+1, 스텝 >>

# In[17]:


for i in range(1, 11, 1):
    print(f'{i}', end=' ')


# In[18]:


for i in range(10, 0, -1):
    print(f'{i}', end=' ')


# In[19]:


for i in range(1, 11, 2):
    print(f'{i}', end=' ')


# In[24]:


total = 0
for n in range(0,11):
    total+=n
print(f'1부터 10까지 정수의 합은 {total}이다.')


# In[25]:


total = 0
for n in range(0,11,2):
    total+=n
print(f'1부터 10까지 짝수 정수의 합은 {total}이다.')


# In[26]:


total = 0
for n in range(1,11,2):
    total+=n
print(f'1부터 10까지 홀수 정수의 합은 {total}이다.')


# In[27]:


total = 0
for n in range(0,11):
    if n%2==0:
        total+=n
print(f'1부터 10까지 짝수 정수의 합은 {total}이다.')


# In[28]:


total = 0
for n in range(0,11):
    if n%2!=0:
        total+=n
print(f'1부터 10까지 홀수 정수의 합은 {total}이다.')


# In[ ]:




