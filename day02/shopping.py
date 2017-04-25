#Author : Duan Yuankun

import json
import sys
import os


systemlist = ['商户系统','用户系统', '退出']
exit_flag = True
return_flag = True
cus_flag = True
with open('/pypi/S14/day02/commoditylist.json', 'r') as f:
    commodity = json.load(f)
print(type(commodity))
print('欢迎登陆愉快购物系统！'.center(60))
while exit_flag:
    print('\n请选择系统：')
    for index, name in enumerate(systemlist, start=1):
        print(index, name)
    sys_choice = input('请选择>> : ')
    if sys_choice.isdigit():
        sys_choice = int(sys_choice) - 1
        if sys_choice == 0:
            while return_flag:
                print('\n请选择你要执行的操作：　')
                print('\n1 添加商品')
                print('2 修改价格')
                print('3 返回')
                b_choice = input('请选择>> : ')
                if b_choice.isdigit():
                    b_choice = int(b_choice) - 1
                    if b_choice == 0:
                       c_name = input('请输入商品名称: ')
                       c_price = input('请输入商品价格：　')
                       if c_price.isdigit():
                           commodity[c_name] = int(c_price)
                           print('%s 已添加，价格：　%s' % (c_name, c_price))
                       else:
                           print('商品价格不正确！')
                    elif b_choice == 1:
                        c_list = list(commodity.items())
                        for index, name in enumerate(c_list, start=1):
                            print('%d、　'%index, name)
                        c_choice = input('请选择你要修改价格的商品>>： ')
                        if c_choice.isdigit():
                            c_choice = int(c_choice) - 1
                            print(c_list[c_choice][0])
                            p_choice = input('你要修改的商品是%s, 请输入新价格>>:'%(c_list[c_choice][0]))
                            if p_choice.isdigit():
                                commodity[c_list[c_choice][0]] = int(p_choice)
                                print('商品%s 的新价格为　%d '%(c_list[c_choice][0],commodity[c_list[c_choice][0]]))
                            else:
                                print('价格必须是数字！')
                    elif b_choice == 2:
                        print('您的所有商品和价格如下：　')
                        for index, name in enumerate(commodity, start=1):
                            print(index, name, commodity[name])
                        with open('/pypi/S14/day02/commoditylist.json', 'w') as f:
                            json.dump(commodity, f)
                        return_flag = False
                    else:
                        print('选项不存在，请重新输入！')
                else:
                    print('无法识别字符串，请输入数字！')
        elif sys_choice == 1:
            print('欢迎光临CMBCCD　Shopping Mall!')
            if os.path.exists('shoppingcart.json'):
                with open('shoppingcart.json', 'r') as f:
                    shoppingdata = json.load(f)
                salary = shoppingdata['salary']
            else:
                s_input = input('请输入你的工资 >>: ')
                if s_input.isdigit():
                    salary = int(s_input)
                else:
                    print('工资的必须是数字！')
                shoppingdata = {'salary':salary, 'Goods':[]}
            com_list = list(commodity.items())
            while cus_flag:
                for index,name in enumerate(com_list, start=1):
                     print(index, name)
                cus_choice = input('请选择你要购买的商品(退出请输入q) >>: ')
                if cus_choice.isdigit():
                    cus_choice = int(cus_choice) - 1
                    if salary >= commodity[com_list[cus_choice][0]]:
                        shoppingdata['Goods'].append(com_list[cus_choice])
                        salary = salary - commodity[com_list[cus_choice][0]]
                    else:
                        print('你的工资余额不足')
                elif cus_choice == 'q':
                    shoppingdata['salary'] = salary
                    print('你选购的物品如下：')
                    for index,name in enumerate(shoppingdata['Goods']):
                        print(index,name)
                    with open('shoppingcart.json', 'w') as f:
                        json.dump(shoppingdata, f)
                    cus_flag = False
                else:
                    print('您的选择不正确！')
        elif sys_choice == 2:
            exit_flag = False
        else:
            print('选项不存在，请重新选择！')
    else:
        print('无法识别字符串，请输入数字！')


