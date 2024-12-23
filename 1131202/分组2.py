import pandas as pd

# 加載第二個上傳的文件
file_path_2 = 'D:/OneDrive/Documents/HTML/1131202/转换后的大洲分类.csv'
data_iso = pd.read_csv(file_path_2)

# 用戶指定需要保留的 ISO 代碼
iso_codes_to_keep = [
    "RUS", "BRA", "CAN", "USA", "IDN", "COD", "PRY", "MOZ", "ARG", "CHN",
    "TZA", "BOL", "ZMB", "AGO", "COL", "KHM", "SWE", "CIV", "AUS", "NGA",
    "MMR", "MEX", "MYS", "GIN", "VEN", "THA", "FIN", "VNM", "LAO", "UGA",
    "CAF", "MDG", "PER", "ETH", "TCD", "IND", "CMR", "NIC", "GHA", "SSD",
    "GTM", "CHL", "FRA", "SLE", "NOR", "ZWE", "NZL", "BEN", "ZAF", "UKR",
    "ECU", "POL", "PHL", "MLI", "COG", "BLR", "KEN", "HND", "LBR", "GBR",
    "TUR", "JPN", "ESP", "DEU", "MNG", "PNG", "LVA", "PAN", "PRT", "MWI",
    "EST", "LKA", "GNB", "ITA", "PRK", "TGO", "KOR", "CUB", "BLZ", "CZE",
    "BFA", "CRI", "GAB", "AUT", "DOM", "HUN", "LTU", "BGD", "URY", "SEN",
    "ROU", "GUY", "IRL", "GRC", "SDN", "SUR", "SVK", "NPL", "HRV"
]

# 篩選數據，只保留指定 ISO 代碼的行
filtered_data = data_iso[data_iso['iso'].isin(iso_codes_to_keep)]

# 將篩選後的數據保存為新的 CSV 文件
output_path = 'D:/OneDrive/Documents/HTML/1131202/篩選後的樹木覆蓋損失數據.csv'
filtered_data.to_csv(output_path, index=False, encoding='utf-8-sig')

# 輸出保存的文件路徑
print(f"篩選後的文件已保存至: {output_path}")
