import pandas as pd
import re

# Load the CSV file
file_path = 'c:/Teckit/crawling_tutorial/대구광역시 북구_관광지주변 카페 현황_20211123.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Function to standardize operating hours
def standardize_hours(hours):
    if pd.isna(hours):
        return ""
    
    # Define regex patterns
    daily_pattern = re.compile(r'매일\s*(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')
    weekday_weekend_pattern = re.compile(r'평일\s*(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})\s*/\s*주말\s*(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')
    simple_pattern = re.compile(r'(\d{1,2}:\d{2})\s*-\s*(\d{1,2}:\d{2})')
    
    # Apply patterns
    if daily_match := daily_pattern.match(hours):
        return f"월-일 {daily_match.group(1)} - {daily_match.group(2)}"
    elif weekday_weekend_match := weekday_weekend_pattern.match(hours):
        return f"월-금 {weekday_weekend_match.group(1)} - {weekday_weekend_match.group(2)}/토-일 {weekday_weekend_match.group(3)} - {weekday_weekend_match.group(4)}"
    elif simple_match := simple_pattern.match(hours):
        return f"월-일 {simple_match.group(1)} - {simple_match.group(2)}"
    else:
        return hours

# Apply the function to the '영업시간' column
df['영업시간'] = df['영업시간'].apply(standardize_hours)

# Save the modified dataframe to a new CSV file
output_file_path = 'c:/Teckit/crawling_tutorial/대구광역시_북구_관광지주변_카페_현황_정리됨.csv'
df.to_csv(output_file_path, index=False, encoding='utf-8-sig')
