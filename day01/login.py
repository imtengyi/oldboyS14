
#Author : admanheart
import json
import getpass

with open('users.json', 'r') as f:
    users = json.load(f)
count = 0
username = input('请输入用户名： ')
while count < 3:
    passwd = getpass.getpass(prompt="请输入密码： ")
    if username not in users.keys():
        print('用户不存在！')
        break
    if users[username]['status'] == 1:
        print('用户已经被锁定，请联系管理员解锁')
        break
    elif users[username]['password'] == passwd:
        print('欢迎登陆招商银行信用卡中心系统！')
        break
    else:
        if count != 2:
            print('密码错误，请重试')
        else:
            print('您的密码已经输错三次，用户已经被锁定，解锁请找管理员！')
            users[username]['status'] = 1
            with open('users.json', 'w') as f:
                json.dump(users, f)
        count += 1