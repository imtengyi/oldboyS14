#Author : Duan Yuankun

import json


systemlist = ['商户系统','用户系统', '退出']
with open('/pypi/S14/day02/commoditylist.json', 'r') as f:
    commodity = json.load(f)

print('欢迎登陆愉快购物系统！'.center(60))
print('请选择系统：')
for index, name in enumerate(systemlist):
    print(index, name)
sys_choice = input('请选择>> : ')
if sys_choice.isdigit():
    sys_choice = int(sys_choice)
    if sys_choice >= 0 and sys_choice <3:


