import time

i=2
c=0
n=0
f=open("质数.txt","w+")
while True:
    try:
        回答=int(input("你想要算多少以内的质数:"))
        break
    except:
        print("只能输入正整数")
start=time.time()
while i<=(回答):
    c=0
    n=0
    while c<i:
        c+=1
        if i%c==0:
            n+=1
            if n>2:
                break#优化
    if n<=2:
        print(i)
        f.write(str(i)+'\n')
    i+=1

end=time.time()
time_1=((end)-(start))*1000
print("用时:{}".format((round(time_1))/1000))
time.sleep(3600)

