import pandas as pd
import re

# Load the CSV file
file_path = 'c:/Teckit/crawling_tutorial/3대구광역시_북구_관광지주변 음식점 현황_20211123.csv'
encodings = ['utf-8-sig', 'utf-16', 'euc-kr', 'iso-8859-1']
for enc in encodings:
    try:
        df = pd.read_csv(file_path, encoding=enc)
        print(f"Successfully loaded with encoding: {enc}")
        break
    except UnicodeDecodeError as e:
        print(f"Failed to load with encoding {enc}: {e}")

import re
import pandas as pd

def standardize_hours(hours):
    if pd.isna(hours):
        return ""
    
    # 정규 표현식 패턴 정의
    daily_pattern = re.compile(r'매일\s*(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')
    weekday_pattern = re.compile(r'평일\s*(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')
    # '월-금' 범위를 처리하기 위한 정규 표현식 패턴 추가
    weekday_range_pattern = re.compile(r'(월|화|수|목|금)-?(월|화|수|목|금)\s*(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')
    weekend_pattern = re.compile(r'주말\s*(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')
    simple_pattern = re.compile(r'(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')
    
    # 패턴 적용
    if daily_match := daily_pattern.match(hours):
        return f"월 {daily_match.group(1)} - {daily_match.group(2)}, 화 {daily_match.group(1)} - {daily_match.group(2)}, 수 {daily_match.group(1)} - {daily_match.group(2)}, 목 {daily_match.group(1)} - {daily_match.group(2)}, 금 {daily_match.group(1)} - {daily_match.group(2)}, 토 {daily_match.group(1)} - {daily_match.group(2)}, 일 {daily_match.group(1)} - {daily_match.group(2)}"
    elif weekday_match := weekday_pattern.match(hours):
        weekdays = "월 {0} - {1}, 화 {0} - {1}, 수 {0} - {1}, 목 {0} - {1}, 금 {0} - {1}".format(weekday_match.group(1), weekday_match.group(2))
        return weekdays
    elif weekend_match := weekend_pattern.match(hours):
        weekend = "토 {0} - {1}, 일 {0} - {1}".format(weekend_match.group(1), weekend_match.group(2))
        return weekend
    elif simple_match := simple_pattern.match(hours):
        return f"월 {simple_match.group(1)} - {simple_match.group(2)}, 화 {simple_match.group(1)} - {simple_match.group(2)}, 수 {simple_match.group(1)} - {simple_match.group(2)}, 목 {simple_match.group(1)} - {simple_match.group(2)}, 금 {simple_match.group(1)} - {simple_match.group(2)}, 토 {simple_match.group(1)} - {simple_match.group(2)}, 일 {simple_match.group(1)} - {simple_match.group(2)}"
    # 패턴 적용
    elif weekday_range_match := weekday_range_pattern.match(hours):
        start_day, end_day, start_time, end_time = weekday_range_match.groups()
        days = ["월", "화", "수", "목", "금"]
        start_index = days.index(start_day)
        end_index = days.index(end_day) + 1
        result = ", ".join(f"{day} {start_time} - {end_time}" for day in days[start_index:end_index])
        return result
    else:
        return hours

# Apply the function to the '영업시간' column
df['영업시간'] = df['영업시간'].apply(standardize_hours)

# Save the modified dataframe to a new CSV file with utf-8-sig encoding
output_file_path = 'c:/Teckit/crawling_tutorial/4대구광역시_북구_관광지주변 음식점 현황_20211123.csv'
df.to_csv(output_file_path, index=False, encoding='utf-8-sig')

# Display the first few rows of the dataframe to check the result
print(df.head())
