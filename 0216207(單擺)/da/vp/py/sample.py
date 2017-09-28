from visual import *
g=9.8               #重力加速度 9.8 m/s^2
size = 0.05         #球半徑 0.05 m
L = 1.0             #細線長 1.0m
theta = 15 * pi / 180  #單擺起始角度 = 15 degrees
omega = 0           #初角速度 = 0

scene = display(width=1200, height=1000,center = (0, -L/2, 0), background=(0.5,0.5,0))     #設定畫面
ceiling = box(length=2, height=0.001, width=2, color=color.blue)    #畫天花板
ball = sphere(radius = size,  color=color.red)                      #畫球
string = cylinder(pos=(0,0,0), radius=0.003)                           #畫細線，一端在(0,0,0)          

dt = 0.001   
while True:
    rate(1000)

    alpha = 
    omega += 
    theta += 
#(用你的物理知識，把這三行未完的程式補完整)
    
    ball.pos = vector(L * sin(theta), -L*cos(theta), 0)
    string.axis = ball.pos - string.pos
