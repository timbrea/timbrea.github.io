import tkinter as tk
import random

# 各种字符的资源库
list=''
list_1='1234567890'
list_2='abcdefghijklmnopqrstuvwxyz'
list_3='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_4='!@#$%^&*'
password=''
bool1=0
bool2=0
bool3=0
bool4=0

#函数
def A():
    global password,list,list_1,list_2,list_3,list_4
    if bool1==1:
        list+=list_1
    if bool2==1:
        list+=list_2
    if bool3==1:
        list+=list_3
    if bool4==1:
        list+=list_4
    try:
        for _ in range(12):
            password+=random.choice(list)
    except:
        print('报错,至少选择一个')
    entry.delete(0, tk.END)
    entry.insert(0,password)
    list=''
    password=''

def c1_():
    global bool1
    if bool1==0:
        bool1=1
    else:
        bool1=0

def c2_():
    global bool2
    if bool2==0:
        bool2=1
    else:
        bool2=0

def c3_():
    global bool3
    if bool3==0:
        bool3=1
    else:
        bool3=0

def c4_():
    global bool4
    if bool4==0:
        bool4=1
    else:
        bool4=0

#主循环窗口
root=tk.Tk()
root.title('密码生成器plus2.0版')
root.geometry('200x150')

#文本输入控件
entry = tk.Entry(root)
entry.pack()

#按钮控件
button=tk.Button(root,text='生成密码',command=A)
button.pack()

#包含各种类型的多选框
c1=tk.Checkbutton(root,text='包含数字',command=c1_)
c1.pack()
c2=tk.Checkbutton(root,text='包含小写字母',command=c2_)
c2.pack()
c3=tk.Checkbutton(root,text='包含大写字母',command=c3_)
c3.pack()
c4=tk.Checkbutton(root,text='包含符号',command=c4_)
c4.pack()

#轮滑控件


#主循环
root.mainloop()