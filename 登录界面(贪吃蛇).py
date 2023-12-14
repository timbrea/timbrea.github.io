import tkinter as tk
import pygame
import random

def game():
    # 初始化 pygame
    pygame.init()

    # 设置游戏画面尺寸
    SIZE = WIDTH, HEIGHT = 800, 600

    # 定义颜色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # 创建游戏窗口
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("贪吃蛇")

    # 设置时钟对象
    clock = pygame.time.Clock()

    # 定义蛇的默认方向
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    # 定义蛇的默认位置和方向
    snake_position = [100, 100]
    snake_direction = RIGHT

    # 定义蛇的默认长度和身体坐标列表
    snake_length = 5
    snake_body = [[100, 100], [90, 100], [80, 100], [70, 100], [60, 100]]

    # 随机生成一个食物位置
    food_position = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]

    # 游戏主循环
    while True:
        # 处理游戏事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT

        # 移动蛇的身体
        for i in range(snake_length - 1, 0, -1):
            snake_body[i] = list(snake_body[i - 1])

        # 移动蛇的头部
        if snake_direction == UP:
            snake_body[0][1] -= 10
        elif snake_direction == RIGHT:
            snake_body[0][0] += 10
        elif snake_direction == DOWN:
            snake_body[0][1] += 10
        elif snake_direction == LEFT:
            snake_body[0][0] -= 10

        # 检测蛇是否吃到食物
        if snake_body[0] == food_position:
            food_position = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
            snake_length += 1
            snake_body.append([0, 0])

        # 绘制游戏背景
        screen.fill(BLACK)

        # 绘制蛇和食物
        for part in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(part[0], part[1], 10, 10))
        pygame.draw.rect(screen, WHITE, pygame.Rect(food_position[0], food_position[1], 10, 10))

        # 更新屏幕
        pygame.display.update()

        # 设置帧率
        clock.tick(12)



usernamelist=['admin\n']
passworldlist=['admin123\n']
check=''#检查名字有无重复项

#root界面

root=tk.Tk()
root.title('面包的程序')
root.geometry('240x200')

labelhome=tk.Label(root,text='欢迎来到面包的程序')
labelhome.pack(pady=15)

#root界面的用户名
labeluser1=tk.Label(root,text='用户名：')
labeluser1.place(x=25, y=56)
textuser1=tk.Text(root,width=15,height=1)
textuser1.place(x=80, y=60)

#root界面的密码
labelpassworld1=tk.Label(root,text='密码：')
labelpassworld1.place(x=36, y=96)
textpassworld1=tk.Text(root,width=15,height=1)
textpassworld1.place(x=80, y=100)

#注册界面
def signhome():
    signup=tk.Tk()
    signup.geometry('200x150')
    signup.title('注册')
    #signup界面

    #signup界面的用户名
    labeluser2=tk.Label(signup,text='用户名：')
    labeluser2.place(x=15, y=26)
    textuser2=tk.Text(signup,width=15,height=1)
    textuser2.place(x=70, y=30)
    
    #signup界面的密码
    labelpassworld2=tk.Label(signup,text='密码：')
    labelpassworld2.place(x=26, y=56)
    textpassworld2=tk.Text(signup,width=15,height=1)
    textpassworld2.place(x=70, y=60)


    def sign():
        global passworldlist
        global usernamelist
        username=str(textuser2.get('1.0','end'))
        for n in range(len(usernamelist)):
            check=False
            if usernamelist[n-1]==username:
                warn1=tk.Tk()
                warn1.title('警告')
                labelwarn1=tk.Label(warn1,text='''警告
用户名重复，换一个用户名''',height=3,)
                labelwarn1.pack()
                warn1.mainloop()
                check=True
                break
        if check==False:
            usernamelist.append(username)
            passworld=str(textpassworld2.get('1.0','end'))
            passworldlist.append(passworld)
            signup.destroy()
    #signup界面的按钮
    buttonsign2=tk.Button(signup,text='注册账号',command=sign)
    buttonsign2.place(x=75,y=100)

    signup.mainloop()

#登录
def login():
    check=False
    username=str(textuser1.get('1.0','end'))
    passworld=str(textpassworld1.get('1.0','end'))
    for n in range(len(usernamelist)):
        if usernamelist[n-1]==username:
            if passworldlist[n-1]==passworld:
                game()
            else:
                warn2=tk.Tk()
                warn2.title('警告')
                labelwarn1=tk.Label(warn2,text='''警告
密码错误''',height=3,)
                labelwarn1.pack()
                warn2.mainloop()
    if check==False:
        warn3=tk.Tk()
        warn3.title('警告')
        labelwarn1=tk.Label(warn3,text='你还没有注册',height=3,)
        labelwarn1.pack()
        warn3.mainloop()

#root界面的按钮
buttonlog1=tk.Button(root,text='登录',width=6,command=login)
buttonlog1.place(x=40,y=160)
buttonsign1=tk.Button(root,text='注册',width=6,command=signhome)
buttonsign1.place(x=150,y=160)

#主循环
root.mainloop()
