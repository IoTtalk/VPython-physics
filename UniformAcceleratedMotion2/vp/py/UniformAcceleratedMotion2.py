####################################程式開始###################################
#from visual import *

#  1. 參數設定
#a = -9.8                 	#加速度值，在x、z方向為0，在y方向為g=-9.8 m/s^2
#vy = 0.0                  	#球的y方向初速
size = 0.5                	#球的半徑
h = 10.0                	#球的初始高度        		    #畫面更新的時間間隔，單位為s
t = 0             		    #模擬所經過的時間 ，單位為s，初始值為0

#  2. 畫面設定
scene = display(title='one-dimensional acceleration',width=800, height=800, center = vector(0, h/2, 0), background=vector(0.5,0.6, 0))
floor = box(pos=vector(0,-0.005/2,0), length=50, height=0.005, width=5)
#ball = sphere(pos =vector(0, h, 0), radius=size, color=color.blue)

scene.range=18
camera_x1=0.8
camera_x2=0.0
scene.forward= vector(camera_x1,camera_x2,-1)
scene.center= vector(5,4,0)

#  3. 描述物體的運動

def ballfall(spd):
    if spd == 9.8: ball = sphere(pos =vector(5, h, 0), radius=size, color=color.red)
    elif spd == 19.6: ball = sphere(pos =vector(6, h, 0), radius=size, color=color.orange)
    elif spd == 30: ball = sphere(pos =vector(7, h, 0), radius=size, color=color.yellow)
    elif spd == 50: ball = sphere(pos =vector(8, h, 0), radius=size, color=color.green)
    elif spd == 99: ball = sphere(pos =vector(9, h, 0), radius=size, color=color.blue)
    elif spd == 500: ball = sphere(pos =vector(10, h, 0), radius=size, color=color.white)
    elif spd == 1000: ball = sphere(pos =vector(11, h, 0), radius=size, color=color.black)
    else : ball = sphere(pos =vector(spd, h, 0), radius=size, color=color.blue)
    #ball = sphere(pos =vector(spd, h, 0), radius=size, color=color.blue)
    ball.velocity = vector(0,0,0)
    playFlag=1
    a = -spd
    dt = 0.001

    def fall():
        rate(1000,fall)
        #ball.velocity.y = ball.velocity.y + a * dt
        ball.pos = ball.pos + ball.velocity * dt

        if ball.pos.y <= size:
            ball.velocity.y = abs(ball.velocity.y)
        else:
            ball.velocity.y = ball.velocity.y + a * dt
        
    fall()

def handler(data):
    #ballfall(data)
    rate(1, progress)
    if data != None:
        ballfall(data)
    
def progress():
    csmPull(df,handler)

df = 'Acceleration-O'
profile = {
    'dm_name': 'UniformAcceleratedMotion2',
    'df_list': [df]
}
csmRegister(profile)

rate(1, progress)
