from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# 1. Excel 파일에서 '도서명' 읽어오기
file_path = './popular_books_with_analysis.xlsx'
df = pd.read_excel(file_path)

# 2. '도서명'에서 ':' 기준으로 split 후 첫 번째 부분 저장
df['검색용 도서명'] = df['도서명'].apply(lambda x: x.split(':')[0] if ':' in x else x)

# 셀레니움 설정 및 알라딘 접속
driver = webdriver.Chrome()  # 크롬 드라이버 경로를 설정해주세요.
driver.get('https://www.aladin.co.kr/home/welcome.aspx')

# 도서명 리스트 생성
book_titles = df['검색용 도서명'].tolist()

# 결과 저장 리스트 초기화
results = []

# 3. 도서명 검색 및 4. 결과 추출
for title in book_titles:
    search_box = driver.find_element('id', 'SearchWord')
    search_box.clear()
    search_box.send_keys(title)
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(1)  # 페이지 로드 대기
    
    try:
        # cover_area_other 아래의 이미지에 걸린 링크 클릭
        cover_image_link = driver.find_element('css selector', '.cover_area_other a img').find_element('xpath', '..')
        cover_image_link.click()
        
        time.sleep(1)  # 페이지 로드 대기
        
        # 상세 페이지에서 도서명 추출
        book_name = driver.find_element('css selector', '.Ere_bo_title').text.strip()
        
        # 상세 페이지에서 평점 추출 (주어진 클래스 사용) -> 평점 부분만 고치면 됨
        book_rating = driver.find_element('css selector', '.Ere_sub_pink.Ere_fs16.Ere_str').text.strip()
        
        results.append({'검색한 도서명': title, '결과 도서명': book_name, '평점': book_rating})
        
        # 검색 페이지로 돌아가기
        driver.back()
        time.sleep(1)
        
    except Exception as e:
        results.append({'검색한 도서명': title, '결과 도서명': None, '평점': None})
        print(f"{title}에 대한 검색 결과를 가져오는 데 문제가 발생했습니다: {e}")

# 작업 완료 후 드라이버 종료
driver.quit()

# 결과 출력
for result in results:
    print(result)
