# -*- coding: utf-8 -*-
"""visualize_public_subway_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1roId8XcgxWZ4L2c59gCzlErnqyqD-GCZ

한글 폰트 사용
"""

!apt-get update -qq
!apt-get install fonts-nanum* -qq

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings(action='ignore') 

path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf' # 나눔 고딕
font_name = fm.FontProperties(fname=path, size=10).get_name() # 기본 폰트 사이즈 : 10
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus']=False
fm._rebuild()

"""# 대중교통 데이터 시각화하기

## 유임 승차 비율이 가장 높은 역은 어디일까?

데이터 확인
"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)

for row in data :
    print(row)

"""header 분리"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)

for row in data :
    row[4] = int(row[4])
    print(row)

"""### 4번 열부터 7번 열까지 정수(`int`)로 바꿔줌"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    print(row)

"""승차 인원이 0으로 집계되는 데이터가 있는 경우 때문에 `ZeroDivisionError` 발생"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    rate = row[4] / row[6]
    if rate > mx :
        mx = rate
print(mx)

"""무임승차 인원이 0명인 역들 출력"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] == 0 :
        print(row)

"""### `row[6]`에 대한 예외처리 (0이 아닌 경우)"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] != 0 :
        rate = row[4] / row[6]
        if rate > mx :
            mx = rate
            print(row, round(rate,2))

"""### 비율 계산 방식 변경 <br>& 유무임 승차 인원의 합이 100,000명 이상인 경우만 찾는 조건 추가"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4] + row[6]) >100000 :
        rate = row[4] / (row[4] + row[6])
        if rate > mx :
            mx = rate
            print(row, round(rate,2))

"""### 비율이 0.94보다 큰 역들 출력하기"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4] + row[6]) >100000 :
        rate = row[4] / (row[4] + row[6])
        if rate > 0.94 :
            mx = rate
            print(row, round(rate,2))

"""### 유임 승차 비율이 가장 높은 역 출력"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
mx = 0
rate = 0
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    if row[6] !=0 and (row[4] + row[6]) >100000 :
        rate = row[4] / (row[4] + row[6])
        if rate > mx :
            mx = rate
            mx_station = row[3] + ' ' + row[1]

print(mx_station, round(mx * 100,2))

"""---
## 유무임 승하차 인원이 가장 많은 역은 어디일까?
"""

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
mx = [0] * 4
mx_station = [''] * 4

for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > mx[i-4] :
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] + ' ' + row[1]
            
for i in range(4) :
    print(mx_station[i], mx[i])

import csv
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
mx = [0] * 4
mx_station = [''] * 4
label = ['유임승차','유임하차','무임승차','무임하차']
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > mx[i-4] :
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] + ' ' + row[1]
for i in range(4) :
    print(label[i] + ' : ' + mx_station[i], mx[i])

"""## 모든 역의 유무임 승하차 비율은 어떻게 될까?

### `pie()` 함수 사용하여 파이 차트로 나타내기

지하철 역 별로 각각 파이 차트가 생성되므로 약 7분 정도의 실행시간 소요
"""

import csv
import matplotlib.pyplot as plt
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
label = ['유임승차','유임하차','무임승차','무임하차']
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    #plt.figure(dpi = 300)
    plt.pie(row[4:8])
    plt.axis('equal')
    plt.show()

"""#### 파이 차트에 제목 추가, label 추가, 색상 변경 등
지하철 역 별로 각각 파이 차트가 생성되므로 약 7분 정도의 실행시간 소요
"""

import csv
import matplotlib.pyplot as plt
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
label = ['유임승차','유임하차','무임승차','무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
# plt.rc('font', family = 'Malgun Gothic')
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi = 300)
    plt.title(row[3] + ' ' + row[1])
    plt.pie(row[4:8], labels = label, colors = c, autopct = '%1.f%%')
    plt.axis('equal')
    plt.show()

"""#### `savefig()` 함수로 그래프 이미지 저장
지하철 역 별로 각각 파이 차트가 생성되므로 약 7분 정도의 실행시간 소요
"""

import csv
import matplotlib.pyplot as plt
f = open('subwayfee.csv', encoding="cp949")
data = csv.reader(f)
next(data)
label = ['유임승차','유임하차','무임승차','무임하차']
c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
# plt.rc('font', family = 'Malgun Gothic')
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
    plt.figure(dpi = 300)
    plt.title(row[3] + ' ' + row[1])
    plt.pie(row[4:8], labels = label, colors = c, autopct = '%1.f%%')
    plt.axis('equal')
    plt.savefig(row[3] + ' ' + row[1] + '.png')
    plt.show()

"""Google Colab 내에 저장된 png 이미지 파일들을 하나의 zip 파일로 압축"""

!zip subway_data.zip *

"""압축 후 `subway_data.zip` 다운로드 (sample_data 폴더가 함께 압축되므로 참고)"""