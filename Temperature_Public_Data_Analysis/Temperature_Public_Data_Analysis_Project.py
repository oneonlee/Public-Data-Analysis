#!/usr/bin/env python
# coding: utf-8

# # 기온 공공 데이터 분석 프로젝트
# 데이터는 기상청이 무료로 제공하는 [기상자료개방포털](https://data.kma.go.kr) 홈페이지를 통해 다운 받을 수 있다.

# ## 서울의 기온 데이터 분석하기

# ### 데이터 출력하기

# In[2]:


import csv 
f = open('seoul.csv', 'r', encoding='cp949') 
data = csv.reader(f, delimiter=',') 
for row in data :
    print(row)

f.close() 


# ### 헤더 저장하기

# In[5]:


import csv
f = open('seoul.csv', 'r', encoding='cp949') 
data = csv.reader(f)
header = next(data)   #①
print(header)        #②
f.close()


# #### `next()` 함수 적용해보기

# In[7]:


import csv
f = open('seoul.csv', 'r', encoding='cp949') 
data = csv.reader(f)
header = next(data)
for row in data :
    print(row)
f.close()


# #### 첫 10개만 출력할 수는 없을까?

# ## 서울이 가장 더웠던 날은 언제였을까?

# ### 최고 기온을 실수(float)로 변환

# In[9]:


import csv
f = open('seoul.csv', 'r', encoding='cp949') 
data = csv.reader(f)
header = next(data)
for row in data :
    row[-1] = float(row[-1]) # 최고 기온을 실수로 변형
    print(row)
f.close()


# #### 에러 발생 원인 찾기

# In[11]:


import csv
f = open('seoul.csv', 'r', encoding='cp949') 
data = csv.reader(f)
header = next(data)
for row in data :
    print(row)
    row[-1] = float(row[-1]) # 최고 기온을 실수로 변형
f.close()


# `['1950-09-01', '108', '', '', '']`에서 원인이 발생하였다.

# ### 서울의 기온이 가장 높았던 날의 날짜와 기온 구하기

# In[12]:


import csv
max_temp = -999   # 최고 기온 값을 저장할 변수
max_date = ''       # 최고 기온이 가장 높았던 날짜를 저장할 변수
f = open('seoul.csv', 'r', encoding='cp949') 
data = csv.reader(f)
header = next(data)
for row in data :
    if row[-1] =='' :
        row[-1] = -999   # -999를 넣어 빈 문자열이 있던 자리라고 표시
    row[-1] = float(row[-1])
    if max_temp < row[-1] :
        max_date = row[0]
        max_temp = row[-1]
f.close()
print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은',max_date+'로, ', max_temp, '도 였습니다.')

