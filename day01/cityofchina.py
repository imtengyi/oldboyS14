# -*-coding: utf-8-*-
import json
import xlrd

data = xlrd.open_workbook('zh_city.xlsx')
table = data.sheet_by_name('县列表')
nrows = table.nrows
city_dict = {}

for name in range(2, nrows):
    row_values = table.row_values(name)
    if row_values[1] in city_dict.keys():
        for city in city_dict[row_values[1]]:
            if row_values[2] in city.values():
                city['area'].append(row_values[3])
                # 此处要跳出for循环，不然会有冗余数据
                break
        else:
            # 如果for循环结束还是没有，说明是新的城市，要新建
            city_dict[row_values[1]].append({'city': row_values[2], 'area': [row_values[3]]})
    else:
        city_dict[row_values[1]] = [{'city': row_values[2], 'area': [row_values[3]]}]
print(city_dict)
with open('zh_city.json', 'w') as f:
    json.dump(city_dict, f)
