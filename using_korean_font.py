# -*- coding: utf-8 -*-
"""using_korean_font.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sHXBM1qzcXxumfAnjUU8tIEHD8v_zKGf

# Google Colab에서 한글 폰트 사용하는 코드 (아래 복사)
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

"""## 잘 작동하는지 테스트 해보기 (안되면 런타임 재실행)
단, 런타임을 재실행하면 변수들이 초기화 되니 주의해야한다.
"""

import matplotlib.pyplot as plt
plt.plot([10, 20, 30, 40], 'hotpink')
plt.title('한글 작동여부 테스트')
plt.show()
