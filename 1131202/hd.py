import pandas as pd

# 文件路径
file_path = 'D:/OneDrive/Documents/HTML/1131202/基于高度的净树木覆盖变化（公顷）.csv'

# 读取上传的 CSV 文件
uploaded_data = pd.read_csv(file_path)

# 映射表 (根据用户提供的信息)
country_mapping = {
    "AFG": "阿富汗", "XAD": "阿克罗提利与德凯利亚", "ALB": "阿尔巴尼亚", "DZA": "阿尔及利亚", "ASM": "美属萨摩亚",
    "AND": "安道尔", "AGO": "安哥拉", "AIA": "安圭拉", "ATA": "南极洲", "ATG": "安提瓜和巴布达",
    "ARG": "阿根廷", "ARM": "亚美尼亚", "ABW": "阿鲁巴", "AUS": "澳大利亚", "AUT": "奥地利",
    "AZE": "阿塞拜疆", "BHS": "巴哈马", "BHR": "巴林", "BGD": "孟加拉国", "BRB": "巴巴多斯",
    "BLR": "白俄罗斯", "BEL": "比利时", "BLZ": "伯利兹", "BEN": "贝宁", "BMU": "百慕大",
    "BTN": "不丹", "BOL": "玻利维亚", "BES": "博内尔、圣尤斯特歇斯和萨巴", "BIH": "波斯尼亚和黑塞哥维那",
    "BWA": "博茨瓦纳", "BVT": "布韦岛", "BRA": "巴西", "IOT": "英属印度洋领地", "VGB": "英属维尔京群岛",
    "BRN": "文莱", "BGR": "保加利亚", "BFA": "布基纳法索", "BDI": "布隆迪", "KHM": "柬埔寨",
    "CMR": "喀麦隆", "CAN": "加拿大", "CPV": "佛得角", "CYM": "开曼群岛", "CAF": "中非共和国",
    "TCD": "乍得", "CHL": "智利", "CHN": "中国", "CXR": "圣诞岛", "XCL": "克利珀顿岛",
    "CCK": "科科斯群岛", "COL": "哥伦比亚", "COM": "科摩罗", "COK": "库克群岛", "CRI": "哥斯达黎加",
    "HRV": "克罗地亚", "CUB": "古巴", "CUW": "库拉索", "CYP": "塞浦路斯", "CZE": "捷克共和国",
    "CIV": "科特迪瓦", "COD": "刚果民主共和国", "DNK": "丹麦", "DJI": "吉布提", "DMA": "多米尼克",
    "DOM": "多米尼加共和国", "TLS": "东帝汶", "ECU": "厄瓜多尔", "EGY": "埃及", "SLV": "萨尔瓦多",
    "GNQ": "赤道几内亚", "ERI": "厄立特里亚", "EST": "爱沙尼亚", "ETH": "埃塞俄比亚", "FLK": "福克兰群岛",
    "FRO": "法罗群岛", "FJI": "斐济", "FIN": "芬兰", "FRA": "法国", "GUF": "法属圭亚那",
    "PYF": "法属波利尼西亚", "ATF": "法属南部领地", "GAB": "加蓬", "GMB": "冈比亚", "GEO": "格鲁吉亚",
    "DEU": "德国", "GHA": "加纳", "GIB": "直布罗陀", "GRC": "希腊", "GRL": "格陵兰",
    "GRD": "格林纳达", "GLP": "瓜德罗普", "GUM": "关岛", "GTM": "危地马拉", "GGY": "根西岛",
    "GIN": "几内亚", "GNB": "几内亚比绍", "GUY": "圭亚那", "HTI": "海地", "HMD": "赫德岛和麦克唐纳群岛",
    "HND": "洪都拉斯", "HKG": "中国香港", "HUN": "匈牙利", "ISL": "冰岛", "IND": "印度",
    "IDN": "印度尼西亚", "IRN": "伊朗", "IRQ": "伊拉克", "IRL": "爱尔兰", "IMN": "马恩岛",
    "ISR": "以色列", "ITA": "意大利", "JAM": "牙买加", "JPN": "日本", "JEY": "泽西岛",
    "JOR": "约旦", "KAZ": "哈萨克斯坦", "KEN": "肯尼亚", "KIR": "基里巴斯", "XKO": "科索沃",
    "KWT": "科威特", "KGZ": "吉尔吉斯斯坦", "LAO": "老挝", "LVA": "拉脱维亚", "LBN": "黎巴嫩",
    "LSO": "莱索托", "LBR": "利比里亚", "LBY": "利比亚", "LIE": "列支敦士登", "LTU": "立陶宛",
    "LUX": "卢森堡", "MAC": "中国澳门", "MKD": "马其顿", "MDG": "马达加斯加", "MWI": "马拉维",
    "MYS": "马来西亚", "MDV": "马尔代夫", "MLI": "马里", "MLT": "马耳他", "MHL": "马绍尔群岛",
    "MTQ": "马提尼克", "MRT": "毛里塔尼亚", "MUS": "毛里求斯", "MYT": "马约特", "MEX": "墨西哥",
    "FSM": "密克罗尼西亚联邦", "MDA": "摩尔多瓦", "MCO": "摩纳哥", "MNG": "蒙古", "MNE": "黑山",
    "MSR": "蒙塞拉特", "MAR": "摩洛哥", "MOZ": "莫桑比克", "MMR": "缅甸", "NAM": "纳米比亚",
    "NRU": "瑙鲁", "NPL": "尼泊尔", "NLD": "荷兰", "NCL": "新喀里多尼亚", "NZL": "新西兰",
    "NIC": "尼加拉瓜", "NER": "尼日尔", "NGA": "尼日利亚", "NIU": "纽埃", "NFK": "诺福克岛",
    "PRK": "朝鲜", "XNC": "北塞浦路斯", "MNP": "北马里亚纳群岛", "NOR": "挪威", "OMN": "阿曼",
    "PAK": "巴基斯坦", "PLW": "帕劳", "PSE": "巴勒斯坦", "PAN": "巴拿马", "PNG": "巴布亚新几内亚",
    "PRY": "巴拉圭", "PER": "秘鲁", "PHL": "菲律宾", "PCN": "皮特凯恩群岛", "POL": "波兰",
    "PRT": "葡萄牙", "PRI": "波多黎各", "QAT": "卡塔尔", "COG": "刚果共和国", "REU": "留尼汪",
    "ROU": "罗马尼亚", "RUS": "俄罗斯", "RWA": "卢旺达", "SHN": "圣赫勒拿岛", "KNA": "圣基茨和尼维斯",
    "LCA": "圣卢西亚", "SPM": "圣皮埃尔和密克隆", "VCT": "圣文森特和格林纳丁斯", "BLM": "圣巴泰勒米",
    "MAF": "圣马丁岛", "WSM": "萨摩亚", "SMR": "圣马力诺", "STP": "圣多美和普林西比",
    "SAU": "沙特阿拉伯", "SEN": "塞内加尔", "SRB": "塞尔维亚", "SYC": "塞舌尔", "SLE": "塞拉利昂",
    "SGP": "新加坡", "SXM": "荷属圣马丁", "SVK": "斯洛伐克", "SVN": "斯洛文尼亚", "SLB": "所罗门群岛",
    "SOM": "索马里", "ZAF": "南非", "SGS": "南乔治亚和南桑威奇群岛", "KOR": "韩国", "SSD": "南苏丹",
    "ESP": "西班牙", "LKA": "斯里兰卡", "SDN": "苏丹", "SUR": "苏里南", "SJM": "斯瓦尔巴群岛和扬马延岛",
    "SWZ": "斯威士兰", "SWE": "瑞典", "CHE": "瑞士", "SYR": "叙利亚", "TJK": "塔吉克斯坦",
    "TZA": "坦桑尼亚", "THA": "泰国", "TGO": "多哥", "TKL": "托克劳", "TON": "汤加",
    "TTO": "特立尼达和多巴哥", "TUN": "突尼斯", "TUR": "土耳其", "TKM": "土库曼斯坦",
    "TCA": "特克斯和凯科斯群岛", "TUV": "图瓦卢", "UGA": "乌干达", "UKR": "乌克兰", "ARE": "阿拉伯联合酋长国",
    "GBR": "英国", "USA": "美国", "UMI": "美国本土外小岛屿", "URY": "乌拉圭", "UZB": "乌兹别克斯坦",
    "VUT": "瓦努阿图", "VAT": "梵蒂冈", "VEN": "委内瑞拉", "VNM": "越南", "VIR": "美属维尔京群岛",
    "WLF": "瓦利斯和富图纳", "ESH": "西撒哈拉", "YEM": "也门", "ZMB": "赞比亚", "ZWE": "津巴布韦",
    "ALA": "奥兰群岛"
}


# 使用已知映射替换 'iso' 列对应的国家名称
uploaded_data['国家'] = uploaded_data['iso'].map(country_mapping)

# 再次保存文件
output_path = "D:/OneDrive/Documents/HTML/1131202/高度.csv"
uploaded_data.to_csv(output_path, index=False, encoding='utf-8-sig')
output_path

