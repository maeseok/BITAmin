from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

text = "파이썬 명지대학교 워드클라우드 ICT 파이썬 명지대학교 정보통신공학과 정보통신 워드클라우드 파이썬 라이브러리 ICT 파이썬 워드클라우드 ICT 명지대학교 워드클라우드  명지대학교  데이터 분석  워드클라우드    "
split_text = text.split()
Counter(split_text)

wordcloud = WordCloud(font_path=os.path.join(DATA_IN_PATH, 'NanumGothic.ttf')).generate(" ".join(train_review))
#wordcloud = WordCloud(font_path='~/Library/Fonts/KoPubWorld Dotum_Pro Medium.otf',background_color='white').generate(text)

split_text
Counter(split_text)



from konlpy.tag import Okt
import pandas as pd
import re

# Okt 형태소 분석기 초기화
okt = Okt()

# 불용어 정의 (예: 조사, 일반적인 불필요한 단어들)
stopwords = ['있다', '하다', '되다', '에', '의', '가', '을', '를', '이', '은', '는', '하다', '과', '와', '에', '에서', '로', '으로']

# 크롤링한 데이터 예제 (각 기사 제목 및 본문 포함)
data = {
    'title': ["제목1: 어떤 범죄 사건이 발생했다", "제목2: 또 다른 사건으로 인해 논란"],
    'content': [
        "서울에서 발생한 이번 사건은 사회적으로 큰 충격을 주고 있다. 많은 사람들이 이에 대해 우려를 표명하고 있다.",
        "이번 사건은 큰 사회적 이슈가 되었으며 많은 언론에서 주목하고 있다."
    ]
}
df = pd.DataFrame(data)

# 텍스트 전처리 함수 정의
def preprocess_text(text):
    # 특수 문자 제거
    text = re.sub(r'[^가-힣\s]', '', text)
    
    # 형태소 분석 후 불용어 제거
    tokens = okt.pos(text, stem=True)  # 품사 태깅 후 원형으로 변환
    filtered_tokens = [word for word, tag in tokens if tag in ['Noun', 'Adjective'] and word not in stopwords]
    
    # 결과를 공백으로 연결하여 반환
    return ' '.join(filtered_tokens)

# 제목과 본문에 대해 전처리 진행
df['processed_title'] = df['title'].apply(preprocess_text)
df['processed_content'] = df['content'].apply(preprocess_text)

# 결과 출력
print(df[['title', 'processed_title', 'content', 'processed_content']])
