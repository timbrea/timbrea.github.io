import random
import time

# 各种字符的资源库
list_1 = '1234567890'
list_2 = 'abcdefghijklmnopqrstuvwxyz'
list_3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_4 = '!@#$%^&*'

# 用户输入想要包含哪种类型的字符
y = input('''
你想要生成包含以下哪些的密码:(不要重复)
[1]数字
[2]小写字母
[3]大写字母
[4]符号
请输入:''')
s=len(y)

# 用户输入想要生成的密码长度
z = int(input('''你想要生成几位的密码(大于等于4)
请输入:'''))

# 用户输入想要生成的密码数量
c = int(input('''你想要生成几个密码
请输入:'''))

# 打开文件准备写入密码
file = open('密码.txt','w+')

#平均数和余数
i=z%s
x=int((z-i)/s)

#生成密码
for _ in range(c):
    item=''
    if '1' in y:
        for _ in range(x):
                item+=(random.choice(list_1))
    if '2' in y:
        for _ in range(x):
            item+=(random.choice(list_2))
    if '3' in y:
        for _ in range(x):
            item+=(random.choice(list_3))
    if '4' in y:
        for _ in range(x):
            item+=(random.choice(list_4))
    for _ in range(i):
        item+=(random.choice(list_1))
    #输出列表
    item=str(item)
    item=list(item)
    random.shuffle(item)
    password=''.join(item)
    print(password)
    file.write(password+'\n')

print('密码已保存到密码.txt文件中')
time.sleep(3)
