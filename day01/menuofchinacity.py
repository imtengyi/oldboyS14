import json
import sys

with open('zh_city.json') as fp:
    city_dict = json.load(fp)
province_list = list(city_dict.keys())
province_list.append('退出')
print('欢迎您进入地域选择系统！'.center(50))
while True:
    city_list = []
    area_list = []
    choice_list = []
    for index, province in enumerate(province_list, start=1):
        print(index, province)
    p_chioce = int(input('请选择你要进入的省份： ')) - 1
    p = province_list[p_chioce]
    if p == '退出':
        print('欢迎再次光临！'.center(50))
        break
    else:
        choice_list.append(p)
        for city in city_dict[p]:
            city_list.append(city['city'])
        city_list.append('返回')
        for index, cityname in enumerate(city_list, start=1):
            print(index, cityname)
        c_chioce = int(input('请选择你要进入的城市： ')) - 1
        c = city_list[c_chioce]
        if c == '返回':
            continue
        else:
            choice_list.append(c)
            area = list(city_dict[p][c_chioce]['area'])
            area.append('返回')
            for index, name in enumerate(area, start=1):
                print(index, name)
            a_chioce = int(input('请选择你要进入的区域： ')) - 1
            if area[a_chioce] == '返回':
                continue
            else:
                print('{:>50s} {} {} 欢迎您！'.format(choice_list[0], choice_list[1], area[a_chioce]))
                sys.exit(0)
