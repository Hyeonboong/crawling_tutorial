from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeOptions 설정
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # 창 최대화
chrome_options.add_argument("--disable-infobars")  # 정보 바 비활성화
chrome_options.add_argument("--disable-extensions")  # 확장 프로그램 비활성화

# 크롬드라이버 설정 및 브라우저 열기
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 네이버지도 페이지 열기
driver.get("https://map.naver.com")

# 검색창 찾기
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input.input_search'))
)

# 검색어 입력
search_box.send_keys('카페')

# 검색 실행
search_box.send_keys(Keys.RETURN)

# 검색 결과 로딩 대기
results = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li._1EKsQ'))
)

# 첫 번째 검색 결과 클릭
results[0].click()

# 가게 이름과 주소 추출
place_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'span.Fc1rA'))
).text

address = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'span.LDgIH'))
).text

print(f"가게 이름: {place_name}")
print(f"주소: {address}")

# 브라우저 닫기
driver.quit()
