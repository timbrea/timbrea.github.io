import tkinter as tk
import random
list1 = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*~'
list2 = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
password = ''

#主运行框
root = tk.Tk()
root.title('密码生成器plus版')
root.geometry('300x200')

item = ''

def fuhao():
    global c1bool
    if c1bool == 0:
        c1bool = 1
    else:
        c1bool = 0
def dian():
    global item
    for _ in range(12):
        if c1bool == 1:
            item += random.choice(list1)
        else:
            item += random.choice(list2)
    password = (item)
    item = '' 
    entry.delete(0, tk.END)
    entry.insert(0,password)

#多选框
c1bool = tk.BooleanVar()
c1bool = 0
c1 = tk.Checkbutton(root,text='包含符号',variable=c1bool,command=fuhao)
c1.pack()

#文本输入控件
entry = tk.Entry(root)
entry.pack(pady=20)

#生成密码按钮
button = tk.Button(root,text='生成密码',command=dian)
button.pack(pady=20)

#主循环
root.mainloop()
