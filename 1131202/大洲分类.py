import pandas as pd

# 文件路径
file_path = 'D:/OneDrive/Documents/HTML/1131202/按地区划分的树木覆盖丧失（公顷）.csv'

# 读取 CSV 文件
uploaded_data = pd.read_csv(file_path)

# 大洲映射表（包含所有国家）
continent_mapping = {
    "亚洲": ["AFG", "ARM", "AZE", "BHR", "BGD", "BTN", "BRN", "KHM", "CHN", "CYP", 
             "GEO", "IND", "IDN", "IRN", "IRQ", "ISR", "JPN", "JOR", "KAZ", "KWT", 
             "KGZ", "LAO", "LBN", "MYS", "MDV", "MNG", "MMR", "NPL", "PRK", "OMN", 
             "PAK", "PHL", "QAT", "KOR", "SAU", "SGP", "LKA", "SYR", "TJK", "THA", 
             "TUR", "TKM", "ARE", "UZB", "VNM", "YEM"],
    "欧洲": ["ALB", "AND", "AUT", "BLR", "BEL", "BIH", "BGR", "HRV", "CYP", "CZE", 
             "DNK", "EST", "FRO", "FIN", "FRA", "DEU", "GIB", "GRC", "GGY", "VAT", 
             "HUN", "ISL", "IRL", "IMN", "ITA", "JEY", "LVA", "LIE", "LTU", "LUX", 
             "MLT", "MDA", "MCO", "MNE", "NLD", "MKD", "NOR", "POL", "PRT", "ROU", 
             "RUS", "SMR", "SRB", "SVK", "SVN", "ESP", "SWE", "CHE", "UKR", "GBR"],
    "非洲": ["DZA", "AGO", "BEN", "BWA", "BFA", "BDI", "CPV", "CMR", "CAF", "TCD", 
             "COM", "COD", "COG", "CIV", "DJI", "EGY", "GNQ", "ERI", "SWZ", "ETH", 
             "GAB", "GMB", "GHA", "GIN", "GNB", "KEN", "LSO", "LBR", "LBY", "MDG", 
             "MWI", "MLI", "MRT", "MUS", "MYT", "MAR", "MOZ", "NAM", "NER", "NGA", 
             "REU", "RWA", "SHN", "STP", "SEN", "SYC", "SLE", "SOM", "ZAF", "SSD", 
             "SDN", "TZA", "TGO", "TUN", "UGA", "ESH", "ZMB", "ZWE"],
    "北美洲": ["ATG", "BHS", "BRB", "BLZ", "CAN", "CRI", "CUB", "DMA", "DOM", "SLV", 
              "GRD", "GLP", "GTM", "HTI", "HND", "JAM", "MTQ", "MEX", "MSR", "ANT", 
              "NIC", "PAN", "PRI", "KNA", "LCA", "SPM", "VCT", "TTO", "TCA", "VIR", 
              "USA"],
    "南美洲": ["ARG", "BOL", "BRA", "CHL", "COL", "ECU", "FLK", "GUY", "PRY", "PER", 
              "SUR", "URY", "VEN"],
    "大洋洲": ["ASM", "AUS", "COK", "FJI", "PYF", "GUM", "KIR", "MHL", "FSM", "NRU", 
              "NCL", "NZL", "NIU", "NFK", "PLW", "PNG", "WSM", "SLB", "TKL", "TON", 
              "TUV", "VUT", "WLF"],
    "南极洲": ["ATA", "BVT", "SGS", "HMD"]
}

# 创建反向映射
continent_reverse_mapping = {
    code: continent
    for continent, codes in continent_mapping.items()
    for code in codes
}

# 为每个国家分配大洲
uploaded_data['大洲'] = uploaded_data['iso'].map(continent_reverse_mapping)

# 保存结果
output_path = "D:/OneDrive/Documents/HTML/1131202/转换后的大洲分类.csv"
uploaded_data.to_csv(output_path, index=False, encoding='utf-8-sig')

output_path
