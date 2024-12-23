

import pandas as pd

# 加載 Excel 文件
file_path = 'D:/OneDrive/Documents/HTML/1131202/基于高度的净树木覆盖变化（公顷）.'  # 確保提供正確的路徑
data = pd.ExcelFile(file_path)

# 檢查可用工作表
print(data.sheet_names)

# Load the specific sheet to preview its contents
sheet_name = '按地区划分的树木覆盖丧失（公顷）'
df = data.parse(sheet_name)

# Display the first few rows of the data to understand its structure
df.head()


# Group data by the '年度樹木覆蓋損失' column and sum the numeric columns
# Assuming the first column is the year column
grouped_df = df.groupby('年度樹木覆蓋損失').sum(numeric_only=True).reset_index()

# Display the processed data
grouped_df.head()
